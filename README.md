# flood_mapping_intercomparison

NOTE: This repository is in active development. All notebooks here are subject to change and do not include full documentation. 

Welcome to SERVIR's Flood Mapping Intercomparison Github! This code repository will introduce you to different flood mapping products and packages produced by researchers such as ESA (The European Space Agency) and NASA (The US National Aeronautics and Space Administration), and NOAA (The US National Oceanic and Atmospheric Administration). These flood mapping products map surface water in near real time from satellite observations. The flood products considered for this study include the following products. For a complete overview of the products and their official citations, please see the spreadsheet in this repository titled "flood_products": 

* VFM (VIIRS flood Map)
     * Based on VIIRS (optical) satellite observations.
     * Produced by NOAA
* GFM (Global Flood Monitor)
     * Based on Sentinel-1 (Synthetic Aperture Radar) satellite observations.
     * Produced by ESA Copernicus Program. 
* MCDWD (MODIS Combined Water Detection Product).
     * Based on MODIS (optical) satellite observations.
     * Produced by NASA
* DSWx-HLS (Dynamic Surface Water Extent - Harmonized Landsat Sentinel Product).
     * Based on HLS (optical) observations.
     * Produced by NASA 
* DSWx-S1 (Dynamic Surface Water Extent - Sentinel-1)
    * Based on Sentinel-1 (SAR) observations.
    * Produced by NASA
* HYDRAFloods. Based on Sentinel-1 observations.
     * Produced by SERVIR (A joint NASA-USAID program)
* HYDROSAR. Based on Sentinel-1 (SAR) observations.
     * Produced by NASA and others

This repository allows you to do the following for a given flood event of interest: 
  1. Determine if there was a Sentinel-1 and/or HLS overpass on your date of interest. If there are both, it will return the overlapping footprint of Sentinel-1 and HLS.
  2. Quantify the cloud cover percentage in your area of interest for the various optical sensors. This will allow you to determine which optical product has the best view of ground conditions, as the optical products are acquired at different times of day.
  3. Obtain up to 7 flood products (depending on temporal extent and resolution of products) for a given day during a flood event.
  4.  Distribute sampling points in order to evaluate the accuracy of the various flood products based on reference data obtained from high-resolution imagery.

The repository consists of both "sections" and "modules". Both of these are .ipynb files. The "modules" are designed to be reused by you. The "sections" are code that we used in our research, but are not designed to be replicated. This is because they either contain once-used calculations to aid in statistical analysis or access commercial imagert that we used for validation. In order to run the modules, you will need a time period of interest, and a region of interest. for a flood event.You can run the modules sequentially (i.e module 1, module 2, module 3....) to replicate our workflow. Below you can find a description of what each script and module will do. 

Sections

* Section A: Case Study Search. This script will take a file containing flood events and output a file showing the satellite overpass and cloud cover information for each flood event. We used this section to obtain a handful of flood events that we examined in this project. 
* Section B: Obtaining reference imagery. This script will help you determine areas where we can order high-resolution commercial satellite imagery for data validation
* Section C: Slope and Elevation Analysis. This script was used to determine the slope and elevation classes used in the sampling design

Modules

* Module 1: Data Availability. This module will show where the Sentinel-1 overpass and the Harmonized Landsat Sentinel overpass overlap. This intersection will serve as the area of interest for the remainder of our modules. 
* Module 2: HydroSAR: This module will obtain the HydroSAR flood product for the region of interest during a single day of interest. 
* Module 3: HydraFloods: This module will obtain the HYDRAFloods flood product for the region of interest during a single day of interest. 
* Module 4: Product Access. This module will access the MCDWD, VFM, GFM, DSWx-HLS, and DSWX-S1 products (if they are available) for the region of interest during a single day of interest.
* Module 5: Harmonization & Validation. This module will harmonize all available products to a single classification schema.
* Module 6: Sampling Design: This module will distribute sample points that we will use to validate the flood products.
* (Under Construction) Module 7 : Reference Data Collection: This module will teach you how to create a project in Collect Earth Online and collect points
* Module 8: Accuracy Assessment. This module will calculate accuracy statistics of each flood product.


If you intend to replicate the entire workflow, you can run the sections and modules in the following order: Section A --> Modules 1 - 5 --> Section B --> Modules 6 & 7 --> Section C --> Module 8

  For a full overview of these products, including the products full names, documentation, spatial extent/resolution, temporal extent/resolution, latency, and more, please see the spreadsheet called "flood_product_info.csv" located in the main folder of this Github. The notebooks folder contains several Google Colaboratory notebooks that will allow you to replicate our workflow. 
