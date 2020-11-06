import libraries_used as lu
import read_csv_data as rcd

#--------Census Data Dropdown Prepare------------------------------------------------------------------
# census_data_df = lu.pd.read_csv('Data/census_2015_data.csv')
# census_data_columns = list(census_data_df.columns.values)
census_data_columns = list(rcd.census_2015_data.columns.values)
census_del_data = ['GEOID','year','name','parent_location']

census_data_columns = [i for i in census_data_columns if i not in census_del_data]
for i in range(0, len(census_data_columns)):
    if 'pct' in census_data_columns[i]:
        x, y = census_data_columns[i].split("pct_")
        census_data_columns[i] = "% of "+ y
        # census_data_columns[i] = census_data_columns[i].replace("_", " ")
    if '_' in census_data_columns[i]:
        census_data_columns[i] = census_data_columns[i].replace("_", " ")

#-------------------------------------------------------------------------------------------------------


#--------Slider Prepare----------------------------------------------------------------
years = [2015, 2016, 2017, 2018]
#--------------------------------------------------------------------------------------


#---------------------------------Counties Mapping------------------------------------------
with lu.urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
  counties = lu.json.load(response)



#---------------------------------Zip Code Mapping------------------------------------------
# # with open('C://Users//Akshay//Desktop//Masters Project//S_SQUARE_LAB//Data//New_York.topo.json') as response1:
# #   zipcodes = lu.json.load(response1)
#
# zipcodes_data_df = lu.pd.read_csv('Data/New_York_State_ZIP_Codes-County_FIPS_Cross-Reference.csv')
#----------------------------------------------------------------------------------------------------

#--------------------Map Level----------------------------------------------------------
map_level = ['Auto', 'Counties', 'Zip Code']
# #---------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------

# livability_index_data = lu.pd.read_csv('Data/liviability_index_data.csv')
# zipcode_livability_index_data = lu.pd.read_csv('Data/ny_zip_code_livability_details.csv')

#------------------------------------------------------------------------------------------------------
data_211_categories = {'B':'Basic Needs','D':"Consumer Services",'F':'Criminal Justice and Legal Services',
                       'H': 'Education', 'J': 'Environment and Public Health/Safety', 'L': 'Health Care',
                       'N': 'Income Support and Employment', 'P': 'Individual and Family Life',
                       'R': 'Mental Health and Substance Use', 'T': 'Organizational/Community/International Services',
                       'Y': 'Target Populations' }

data_211_categories_num = {'B': 1, 'D': 2, 'F': 3,
                           'H': 4, 'J': 5, 'L': 6,
                           'N': 7, 'P': 8, 'R': 9,
                           'T': 10,'X':11, 'Y': 12}


data_211_sub_categories = {'B': ['BD', 'BH', 'BM', 'BT', 'BV'],
                          'D': ['DD', 'DF', 'DM', 'DT'],
                          'F': ['FC', 'FF', 'FJ', 'FL', 'FN', 'FP', 'FR', 'FT'],
                          'H': ['HD', 'HH', 'HL'],
                          'J': ['JP', 'JR'],
                          'L': ['LD', 'LE', 'LF', 'LH', 'LJ', 'LL', 'LN', 'LR', 'LT', 'LV'],
                          'N': ['ND', 'NL', 'NS', 'NT'],
                          'P': ['PB', 'PD', 'PH', 'PL', 'PN', 'PS', 'PW', 'PX'],
                          'R': ['RF', 'RM', 'RP', 'RR', 'RX'],
                          'T': ['TB', 'TC', 'TD', 'TE', 'TH', 'TI', 'TJ', 'TM', 'TN', 'TO', 'TP'],
                          'Y': ['YB', 'YC', 'YF', 'YJ', 'YK', 'YL', 'YM', 'YN', 'YO', 'YP', 'YS', 'YT', 'YV', 'YX', 'YZ']}


data_211_sub_categories_text = {'B': ['Food','Housing/Shelter','Material Goods','Transportation','Utilities'],
                          'D': ['Consumer Assistance and Protection','Consumer Regulation','Money Management',
                                'Tax Organizations and Services'],
                          'F': ['Courts','Criminal Correctional System','Judicial Services','Law Enforcement Agencies',
                                'Law Enforcement Services','Legal Assistance Modalities','Legal Expense Insurance','Legal Services'],
                          'H': ['Educational Institutions/Schools','Educational Programs','Educational Support Services'],
                          'J': ['Environmental Protection and Improvement','Public Health','Public Safety'],
                          'L': ['Emergency Medical Care','General Medical Care','Health Screening/Diagnostic Services',
                                'Health Supportive Services','Human Reproduction','Inpatient Health Facilities',
                                'Outpatient Health Facilities','Rehabilitation/Habilitation Services',
                                'Specialized Treatment and Prevention','Specialty Medicine'],
                          'N': ['Employment','Public Assistance Programs','Social Insurance Programs','Temporary Financial Assistance'],
                          'P': ['Death Certification/Burial Arrangements','Domestic Animal Services','Individual and Family Support Services',
                                'Leisure Activities/Recreation','Mutual Support','Social Development and Enrichment',
                                'Volunteer Development','Volunteer Opportunities'],
                          'R': ['Counseling Settings','Mental Health Care Facilities',
                                'Mental Health Assessment and Treatment','Mental Health Support Services',
                                'Substance Use Disorder Services'],
                          'T': ['Community Economic Development and Finance','Community Facilities/Centers','Community Groups and Government/Administrative Offices',
                                'Community Planning and Public Works','Disaster Services','Donor Services','Information Services','Military Service',
                                'Occupational/Professional Associations','Organizational Development and Management Delivery Methods',
                                'Organizational Development and Management Services'],
                          'Y': ['Age Groups','Benefits Recipients','Disabilities and Health Conditions','Families and Individuals Needing Support',
                                'Family Relationships','Income/Employment Status', 'Living Situation/Housing Status','Military Personnel/Contractors',
                                'Occupations','Offenders','Sex/Gender','Sexual Orientation/Gender Identity','Transients',
                                'Victims/Survivors','Topical Identifiers/Issues']}

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
data_211_categories_l = list(data_211_categories.values())
key_list = list(data_211_categories.keys())
val_list = list(data_211_categories.values())

