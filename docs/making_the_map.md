making_the_map.md
-----------------

this document describes the data and processing techniques used to make the map found at https://nationalunbroadbandmap.com.

At a high level, we used two geographic datasets and two tabular datasets.  these datasets and the processes to develop them are all described below.


Sources
-------

geographic datasets
-------------------
- we use a US Census block shape file, loaded into PostGIS as the geographic base for determining unserved by broadband in the US.  These shape files can be found here ftp://ftp2.census.gov/geo/tiger/TIGER2018/TABBLOCK/. 
- we use a purchased dataset of Wirecenters to determine the study area code (SAC) boundaries, although a public asset is found at https://www.fcc.gov/economics-analytics/industry-analysis-division/study-area-boundary-data.  we then used a geospatial dissolve to get unique boundaries for SACs from wirecenters.

tabular dataset
----------------
- we use the FCC Form 477 from June 2019 to determine unserved.  we join the 477 data with US Census Block data (above) on the unique block code.  The data download for each state can be found here https://www.fcc.gov/general/broadband-deployment-data-fcc-form-477.  We 
- we use the USAC funding disbursement tool to download funding disbursed to each state.  that tool can be found here https://apps.usac.org/li/tools/disbursements/default.aspx.


Processing
----------
Unserved - orange areas on the map for unserved blocks
--------
- we load the block shapes into a PostGIS database one state at a time.  there is a shell script to load that data named `./docs/processing/sh/bl_import.sh` directory.
- we load the csv files for form 477 in to that same database using a load scripts named `./docs/processing/python/load_477.py`
- we then add and populate fields for fiber and cable to the block data.  this is based on the pressence of fiber (technology code `50`) or cable (technology codes `40,41,42,43`) in the most recent 477 data.  that script is named `./docs/python/served.py`.
- we then make an unserved map of each state by dissolving the blocks based on blocks that lack fiber or lack cable.  we do this using the script named `./docs/python/mk_unserved.py`
- finally, we assemble the states as regions using the scripts named `./docs/sql/mk_region_n.sql`.

Disbursement 
------------
- we create a postgres table to store all of the disbursement data.  we then load all of the USAC csv downloaded files into that table, with the script named `./docs/processing/sql/load_disbursement.sql`
- we then dissolve our wirecenter data to SAC only layer, giving us a unique SAC code per polygon.  Now with a SAC code on a polygon layer, and a SAC code on the disbursement table, we use the script `./docs/processing/sql/pop_cost.sql` to sum the amount of money USAC has disbursed to all SAC codes for which we have a polygon. 

remaining
---------
this geography represents the `unaccounted` for money that is distributed to telco's for providing service.  USAC makes publically available the SAC value along with each distrubution.  The SAC value is therefore the only way to understand how much money went to a company AND location.  in this data, HOWEVER, each state has SAC codes for which the geography is `unknown`.  These are typically SACs that were present for the old Bell systems, mostly now AT&T.  The result is USAC is distributing 100s of millions of dollars that are literally unaccounted for; the public, much less the federal entities has no knowledge of where this money is actually going, or whom this is intended to serve.  
- to establish these areas, we use the script `./docs/processing/python/mk_remain.py` to create polygons for the state outside of all existing SAC footprints in the state.  this general `remaining` polygon, then, is the catch all of all unaccounted for funds.
- to add all of these funds to those `remaining` polygons, we use the script `./docs/processing/python/pop_remain.py` to sum up the total disbursements for these unaccounted for areas and dollar amounts.



