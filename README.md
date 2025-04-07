# flood_mapping_intercomparison

NOTE: This repository is in active development. All notebooks here are subject to change and do not include full documentation. 

Welcome to SERVIR's Flood Mapping Intercomparison Github! This code repository will introduce you to different flood mapping products and packages produced by researchers such as ESA (The European Space Agency) and NASA (The US National Aeronautics and Space Administration), and NOAA (The US National Oceanic and Atmospheric Administration). These flood mapping products map surface water in near real time from satellite observations. In order to work with this code, you will need the following accounts:

PREREQUISITES 

To run this code, you will need 
* a Google Earth Engine account
* A Google Earth Engine project linked to the above Google Earth Engine account. See [this page](https://developers.google.com/earth-engine/guides/access)
* A NASA Earthdata account. To create a new account: click [here](https://urs.earthdata.nasa.gov/users/new)
* A Global Flood Mapping (GFM) Account. 

The flood products considered for this study include the following products. For a complete overview of the products and their official citations, please see the document called "flood_product_specifications", which is located in the "resources" folder of this repository. 

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

The repository consists of both "sections" and "modules". Both of these are .ipynb files and can be found in the notebooks folder of the Github. The "modules" are designed to be reused by you. The "sections" are code that we used in our research, but are not designed to be replicated. This is because they either contain once-used calculations to aid in statistical analysis or access commercial imagert that we used for validation. In order to run the modules, you will need a time period of interest, and a region of interest. for a flood event.You can run the modules sequentially (i.e module 1, module 2, module 3....) to replicate our workflow. Below you can find a description of what each script and module will do. 

Sections

* Section A: Case Study Search. This script will take a file containing flood events and output a file showing the satellite overpass and cloud cover information for each flood event. We used this section to obtain a handful of flood events that we examined in this project.
* Section A1: Data Cleaning. This script will assist you in formatting a CSV to feed to Section A as an input. 
* Section B: Obtaining reference imagery. This script will help you determine areas where we can order high-resolution commercial satellite imagery for data validation
* Section C: Slope and Elevation Analysis. This script was used to determine the slope and elevation classes used in the sampling design

Modules

* Module 1 -- Data Availability: This module will show where the Sentinel-1 overpass and the Harmonized Landsat Sentinel overpass overlap. This intersection will serve as the area of interest for the remainder of our modules. 
* Module 2 -- Product Access: This module will access the MCDWD, VFM, GFM, DSWx-HLS, and DSWx-S1 products, and run the HYDRAFloods and HYDROSAR software for the region of interest during a single day of interest.
* Module 2A -- Traditional Product Access: This module will do the same thing as Module 2, but will guide you to accessing the products via their respective online repositories rather than using their Python API's. It is recommended to follow Module 2 rather than Module 2A. 
* Module 3 -- Harmonization & Validation: This module will harmonize all available products to a single classification schema.
* Module 4 -- Sampling Design: This module will distribute sample points that we will use to validate the flood products.
* Module 5 -- Reference Data Collection: This module will teach you how to create a project in Collect Earth Online and collect points
* Module 6 --Accuracy Assessment. This module will calculate accuracy statistics of each flood product.


If you intend to replicate the entire workflow, you can run the sections and modules in the following order: Section A1 --> Section A --> Module 1 --> Module 2 OR Module 2A --> Module 3 --> Section B --> Module 4 --> Section C --> Module 5. PLEASE NOTE: These modules were written with the intent of use for flood events where all seven products are available (i.e. there are cloud-free overpasses for VIIRS and MODIS, and there is an HLS & Sentinel-1 overpass on the day of interest). In order to apply this workflow to different flood events where one or more products are not available, the workflow may have to be modified. 

  For a full overview of these products, including the products full names, documentation, spatial extent/resolution, temporal extent/resolution, latency, and more, please see the spreadsheet called "flood_product_info.csv" located in the "resources" folder of this Github. This folder also contains links to papers and resources for different flood products. 
