# Oregon Wildfire Data Project

### This Project aims to analyze the historical trends of wildfires in Oregon.

**Data**
The project uses data obtained from a kaggle dataset: https://www.kaggle.com/rtatman/188-million-us-wildfires
I have also scraped data from the ODF (Oregon Department of Forestry) wildfire database.

**Features:**
Each dataset has different features which allowed different analysis aims.

Kaggle features:

* FIRE_YEAR = Calendar year in which the fire was discovered or confirmed to exist.
* DISCOVERY_DOY = Day of year on which the fire was discovered or confirmed to exist.
* NWCGREPORTINGUNIT_NAME = Active NWCG Unit Name for the unit preparing the fire report.
* STATCAUSEDESCR = Description of the (statistical) cause of the fire.
* FIPS_NAME = County name from the FIPS publication 6-4 for representation of counties and equivalent entities.
* FIRE_NAME = Name of the incident, from the fire report (primary) or ICS-209 report (secondary).
* FIRE_SIZE = Estimate of acres within the final perimeter of the fire.
* FIRESIZECLASS = Code for fire size based on the number of acres within the final fire perimeter expenditures (A=greater than 0 but less than or equal to 0.25 acres, B=0.26-9.9 acres, C=10.0-99.9 acres, D=100-299 acres, E=300 to 999 acres, F=1000 to 4999 acres, and G=5000+ acres).
* `Custom` DTC_Burn_Time = Derived from original Contained time - discovery time
* `Custom` DTC_AVG_Burn_Rate = Fire size divided by burn time
* LATITUDE = Latitude (NAD83) for point location of the fire (decimal degrees).
* LONGITUDE = Longitude (NAD83) for point location of the fire (decimal degrees).
* OWNER_DESCR = Name of primary owner or entity responsible for managing the land at the point of origin of the fire at the time of the incident.

ODF Features:
* fire_year = Calendar year in which the fire was discovered or confirmed to exist.
* fire_name =  Name of the incident, from the fire report (primary) or ICS-209 report (secondary).
* latitude = Latitude (NAD83) for point location of the fire (decimal degrees).
* longitude = Longitude (NAD83) for point location of the fire (decimal degrees).
* fuel_model = Ecosystem environment used as fuel.
* county = County name of the fire's origin.
* report_date = Date and time the fire was discovered.
* general_cause = Description of the (statistical) cause of the fire.
* total_acres = Number of acres that were burned in the fire.