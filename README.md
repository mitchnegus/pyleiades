# *pyleiades*
[![Build Status](https://travis-ci.org/mitchnegus/pyleiades.svg?branch=master)](https://travis-ci.org/mitchnegus/pyleiades)

## Python Library for EIA Data Examination & Exhibition

###### A tool for creating visuals from historical energy data (e.g. the EIA monthly energy review).
 
This tool is designed to provide insightful, aesthetic and more flexible visualizations of the Energy Information Administration (EIA) monthly energy review datasets. The datasets contain information about the sources of energy Americans have relied on for power since the middle of the 20th century. The datasets begin in 1949 with annual energy production, consumption, import, and export values, and extend up until the present. Monthly energy datapoints are reported starting in 1973.

The basic energy sources are reported in the following groups:  

###### Fossil Fuels
* Coal
* Natural Gas
* Petroleum

###### Renewables
* Wind
* Solar
* Hydroelectric
* Geothermal
* Biomass

###### Nuclear
* Fission

The data is published monthly on the [EIA's website](https://www.eia.gov/totalenergy/data/monthly/), and as of July 5th, 2017 records were provided up through March 2017.

All reported values are in units of quadrillion british thermal units (1.0E15 btu). Be aware that the datasets may provide [more precision](https://www.eia.gov/totalenergy/data/monthly/dataunits.php) than is published in the PDF reports.

--------------------------------------------------------------

Outside dependencies are numpy, pandas, matplotlib, and seaborn.

--------------------------------------------------------------
