# flood_mapping_intercomparison

NOTE: This repository is in active development. All notebooks here are subject to change and do not include full documentation. 

Welcome to SERVIR's Flood Mapping Intercomparison Github! This code repository will introduce you to different flood mapping products and packages produced by researchers including ESA and NASA. These flood mapping products map surface water in near real time from Satellite Observations. The flood products considered for this study include the following 

* VFM (VIIRS flood Map). Based on VIIRS (optical) satellite observations.
* GFM (Global Flood Monitor). Based on Sentinel-1 (SAR) satellite observations.
* MCDWD (MODIS Combined Water Detection Product). Based on MODIS (optical) satellite observations.
* DSWx-HLS (Dynamic Surface Water Extent - Harmonized Landsat Sentinel Product). Based on HLS (optical) observations.
* DSWx-S1 (Dynamic Surface Water Extent - Sentinel-1). Based on Sentinel-1 (SAR observations). 
* HYDRAFloods. Based on Sentinel-1 and other observations.
* HYDROSAR. Based on Sentinel-1 (SAR) observations.

This repository allows you to do the following for a given flood event of interest: 
  1. Determine if there was a Sentinel-1 and/or HLS overpass on your date of interest. If there are both, it will return the overlapping footprint of Sentinel-1 and HLS.
  2. Quantify the cloud cover percentage in your area of interest for the various optical sensors. This will allow you to determine which optical product has the best view of ground conditions, as the optical products are acquired at different times of day.
  3. Obtain up to 7 flood products (depending on temporal extent and resolution of products) for a given day during a flood event.
  4.  Distribute sampling points in order to evaluate the accuracy of the various flood products based on reference data obtained from high-resolution imagery. 

  For a full overview of these products, including the products full names, documentation, spatial extent/resolution, temporal extent/resolution, latency, and more, please see the spreadsheet located in the main folder of this Github. The notebooks folder contains several Google Colaboratory notebooks that will allow you to replicate our workflow. 
