import libraries_used as lu

#______________________________Census_Data_Files________________________________________________________________________
census_2015_data = lu.pd.read_csv("Data/census_2015_data.csv")
census_2016_data = lu.pd.read_csv("Data/census_2016_data.csv")
census_2017_data = lu.pd.read_csv("Data/census_2017_data.csv")
census_2018_data = lu.pd.read_csv("Data/census_2018_data.csv")
census_dummy_data = lu.pd.read_csv("Data/census_dummy_data.csv")
#_______________________________________________________________________________________________________________________

#______________________________211_Data_Files________________________________________________________________________
_211_2015_data = lu.pd.read_csv("Data/2015_211.csv")
_211_2016_data = lu.pd.read_csv("Data/2016_211.csv")
_211_2017_data = lu.pd.read_csv("Data/2017_211.csv")
_211_2018_data = lu.pd.read_csv("Data/2018_211.csv")

#______________________________ZipCode_211_Data_Files________________________________________________________________________
zipcode_211_2015_data = lu.pd.read_csv("Data/zipcode_2015_211.csv")
zipcode_211_2016_data = lu.pd.read_csv("Data/zipcode_2016_211.csv")
zipcode_211_2017_data = lu.pd.read_csv("Data/zipcode_2017_211.csv")
zipcode_211_2018_data = lu.pd.read_csv("Data/zipcode_2018_211.csv")
#_______________________________________________________________________________________________________________________



zipcode_laton_lon_data = lu.pd.read_csv("Data/ny-zip-code-latitude-and-longitude.csv")
zipcode_laton_lon_data["GEOID"]= zipcode_laton_lon_data["GEOID"].astype(str)

with open('Data/ny_new_york_zip_codes_geo.min.json') as zipcode_data:
  zipcode_data = lu.json.load(zipcode_data)



zip_county_lat_lon_data = lu.pd.read_csv("Data/county_lat_lon.csv")
livability_index_data = lu.pd.read_csv('Data/liviability_index_data.csv')
zipcode_livability_index_data = lu.pd.read_csv('Data/ny_zip_code_livability_details.csv')
lat_lon_data = lu.pd.read_csv('Data/county_lat_lon.csv')