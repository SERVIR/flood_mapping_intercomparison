# FMI -- Flood Mapping Intercomparison

<img width="191" height="20" alt="image" src="https://github.com/user-attachments/assets/5a6c0151-139e-4442-a7fa-5b6593173907" />


## **Introduction**

Welcome to SERVIR's Flood Mapping Intercomparison (FMI) code repository! This repo will introduce you to different flood mapping products and packages produced by researchers at ESA (The European Space Agency), NASA (The US National Aeronautics and Space Administration), and NOAA (The US National Oceanic and Atmospheric Administration). These flood mapping products map surface water in near real time from satellite observations.

This repository contains two folders: "notebooks" and "resources". In the notebooks folder, you will find code that will allow you to automatically access and harmonize these flood maps, as well as replicate our accuracy assessment workflow. In the resources folder, you will find a spreadsheet listing all of the characteristics of each product, as well as links to further training materials and documentation for each product. If you encounter an issue working with this code, feel free to post in the "Issues" Section here, or email me at mrm0065@uah.edu.

In order to work with the code located in the notebooks folder, you will need the following accounts:

## **PREREQUISITES** 

To run this code, you will need 
* A Google Earth Engine account
* A Google Earth Engine project linked to the above Google Earth Engine account. See [this page](https://developers.google.com/earth-engine/guides/access)
* A NASA Earthdata account. To create a new account, click [here](https://urs.earthdata.nasa.gov/users/new)
* A Global Flood Mapping (GFM) Account. To create a new account, click [here](https://portal.gfm.eodc.eu/register)

The flood products considered for this study include the following products. For a complete overview of the products and their official citations, please see the document called "flood_product_specifications", which is located in the "resources" folder of this repository. 

* VFM (VIIRS flood Map)
     * Based on VIIRS (optical) satellite observations.
     * Produced by NOAA
* GFM (Global Flood Monitor)
     * Based on Sentinel-1 (SAR) satellite observations.
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
* HYDRAFloods.
     * Based on Sentinel-1 (SAR)observations.
     * Produced by SERVIR (A joint NASA-USAID program)
* HYDROSAR.
     * Based on Sentinel-1 (SAR) observations.
     * Produced by a NASA-funded team at Alaska Satellite Facility, NASA Goddard Space Flight Center, and NASA
       Marshall Space Flight Center


This repository allows you to do the following for a given flood event of interest: 
  1. Determine if there was a Sentinel-1 and/or HLS overpass on your date of interest. If there are both, it will return the overlapping footprint of Sentinel-1 and HLS.
  2. Quantify the cloud cover percentage in your area of interest for the various optical sensors. This will allow you to determine which optical product has the best view of ground conditions, as the optical products are acquired at different times of day.
  3. Obtain up to 7 flood products (depending on temporal extent and resolution of products) for a given day during a flood event.
  4.  Distribute sampling points in order to evaluate the accuracy of the various flood products based on reference data obtained from high-resolution imagery.

The repository consists of both "sections" and "modules". Both of these are .ipynb files and can be found in the notebooks folder of the Github. The "modules" are designed to be reused by you. The "sections" are code that we used in our research, but are not designed to be replicated. This is because they either contain once-used calculations to aid in statistical analysis or access commercial imagery that we used for validation of flood products. In order to run the modules, you will need a time period of interest, and a region of interest for a flood event. The modules assume that this time period and region of interest have HLS and Sentinel-1 overpasses on the same day so that all flood products can be accessed. If that is not the case, further edits must be made to the code. You can run the modules sequentially (i.e module 1, module 2, module 3....) to replicate our workflow. Below you can find a description of what each script and module will do. 

Modules

* Module 1 -- Data Availability: This module will show where the Sentinel-1 overpass and the Harmonized Landsat Sentinel overpass overlap. This intersection will serve as the area of interest for the remainder of our modules. 
* Module 2 -- Product Access: This module will access the MCDWD, VFM, GFM, DSWx-HLS, and DSWx-S1 products, and run the HYDRAFloods and HYDROSAR software for the region of interest during a single day of interest.
* Module 2A -- Traditional Product Access: This module will do the same thing as Module 2, but will guide you to accessing the products via their respective online repositories rather than using their Python API's. It is recommended to follow Module 2 rather than Module 2A. 
* Module 3 -- Harmonization & Validation: This module will harmonize all available products to a single classification schema.
* Module 4 -- Sampling Design: This module will distribute sample points that we will use to validate the flood products.
* Module 5 -- Reference Data Collection: This module will teach you how to create a project in Collect Earth Online and collect points
* Module 6 -- Accuracy Assessment. This module will calculate accuracy statistics of each flood product. This includes overall accuracy, precision, recall, F1 score, and the Normalized Matthew's Correlation Coefficient. These metrics will be calculated for all points as well as for subpopulations relating to landcover, slope, and elevation. 
* Module 7 -- Accuracy Visualization. This module will visualize the metrics calculated in Module 6 for different flood events, land cover types, and slope/elevation regimes
* Module 8 -- Resampling. This module will resample all flood products to a common pixel size of 30 meters.
* Module 9 -- Intersection Over Union. This module will caclulate the Intersection over Union for each pair of flood products in order to measure the similarity of each map's classification. In the absence of a ground truth raster, this module allows us to compare the degree of agreement of different flood maps. 
  
Sections

* Section A: Case Study Search. This script will take a file containing flood events and output a file showing the satellite overpass and cloud cover information for each flood event. We used this section to obtain a handful of flood events that we examined in this project.
* Section A1: Data Cleaning. This script will assist you in formatting a CSV to feed to Section A as an input. 
* Section B: Obtaining reference imagery. This script will help you determine areas where we can order high-resolution commercial satellite imagery for data validation
* Section C: Slope and Elevation Analysis. This script was used to determine the slope and elevation classes used in the sampling design
* Section D: Google Drive Export: Allows for exporting of flood maps from Google Earth Engine to Google Drive for further analysis.
* Section E: Manual Validation: Used to validate the statistics calculated in Module 3 and Module 9. 


If you intend to replicate the entire workflow, you can run the sections and modules in the following order: Section A1 --> Section A --> Module 1 --> Module 2 OR Module 2A --> Module 3 --> Section B --> Module 4 --> Section C --> Modules 5-7. PLEASE NOTE: These modules were written with the intent of use for flood events where all seven products are available (i.e. there are cloud-free overpasses for VIIRS and MODIS, and there is an HLS & Sentinel-1 overpass on the day of interest). In order to apply this workflow to different flood events where one or more products are not available, the workflow may have to be modified. 

  For a full overview of these products, including the products full names, documentation, spatial extent/resolution, temporal extent/resolution, latency, and more, please see the spreadsheet called "flood_product_info.csv" located in the "resources" folder of this Github. This folder also contains links to papers and resources for different flood products. 
