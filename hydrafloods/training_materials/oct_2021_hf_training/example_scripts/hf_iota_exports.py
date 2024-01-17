#!/usr/bin/env python
# coding: utf-8

# 0 6 * * * /home/Socrates/kmarkert/miniconda3/envs/hydra/bin/python /home/Socrates/kmarkert/hydra_runs/hf_iota_exports.py

import ee

ee.Initialize()

import datetime
import hydrafloods as hf
from hydrafloods import ml


# area where overlap is known
region = ee.FeatureCollection(
    [
        hf.country_bbox("Guatemala"),
        hf.country_bbox("Belize"),
        hf.country_bbox("Honduras"),
        hf.country_bbox("El Salvador"),
        hf.country_bbox("Nicaragua"),
    ]
).geometry(100)

lsib = (
    ee.FeatureCollection("USDOS/LSIB_SIMPLE/2017")
    .filterBounds(region)
    .geometry(100)
    .intersection(region, 100)
)


tiles = hf.tile_region(region, grid_size=1.0, intersect_geom=lsib)


n = tiles.size().getInfo()

# elevation data for terrain corrections
elv = ee.Image("JAXA/ALOS/AW3D30/V2_2").select("AVE_DSM")
hand = ee.Image("MERIT/Hydro/v1_0_1").select(["hnd"], ["HAND"]).unmask(0)

# get the previous 5 years of permenant water for context
permanent_water = (
    ee.ImageCollection("JRC/GSW1_2/YearlyHistory")
    .filterDate("2010-01-01", "2021-01-01")
    .limit(5, "system:time_start", False)
    .map(lambda x: x.select("waterClass").eq(3))
    .sum()
    .unmask(0)
    .gt(0)
)


def hf_export(region, start_time, end_time):
    region_buff = region.buffer(50000)
    s1 = hf.Sentinel1(region_buff, start_time, end_time)

    n_sar = s1.n_images

    # check to make sure the collection has data
    if n_sar > 0:
        s1 = (
            s1.apply_func(hf.slope_correction, elevation=elv, buffer=60)
            .apply_func(lambda x: x.updateMask(hand.lt(60)))
            .apply_func(hf.gamma_map)
        )
        sar_img = s1.collection.median()

        sar_water = hf.edge_otsu(
            sar_img,
            band="VV",
            initial_threshold=-16,
            edge_buffer=300,
            scale=90,
            region=region_buff,
        )

        water_img = sar_water.Or(permanent_water)

        stimestr = start_time.strftime("%Y%m%d")
        etimestr = end_time.strftime("%Y%m%d")

        tcoords = region.coordinates().get(0).getInfo()
        xmin = int(tcoords[0][0])
        ymax = int(tcoords[2][1])

        xstr = f"{abs(xmin):03d}W" if xmin < 0 else f"{xmin:03d}E"
        ystr = f"{abs(ymax):02d}S" if ymax < 0 else f"{ymax:02d}N"

        out_img = water_img.add(1).add(permanent_water).unmask(0).uint8()

        out_path = f"hydrafloods_sentinel1_{xstr}_{ystr}_{stimestr}"
        export_desc = f"hydrafloods_centralamerica_export_{xstr}_{ystr}"
        print(out_path)

        task = ee.batch.Export.image.toDrive(
            image=out_img,
            description=export_desc,
            folder="iota_water_maps",
            fileNamePrefix=out_path,
            region=region,
            scale=30,
            maxPixels=1e13,
            fileDimensions=[35840, 55296],
            formatOptions={"cloudOptimized": True},
        )
        task.start()


# month where we know coincident data
now_time = datetime.datetime.now().replace(hour=0, microsecond=0, second=0, minute=0)

# for i in range(2,19):
end_time = now_time - datetime.timedelta(1)  # datetime.datetime(2020,11,i)#

start_time = end_time - datetime.timedelta(1)

print(start_time, " - ", end_time)


tile_list = tiles.toList(n)
for i in range(n):
    tile = ee.Feature(tile_list.get(i)).geometry(10)
    hf_export(tile, start_time, end_time)
