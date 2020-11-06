# # from selenium.webdriver.common.by import By
# # from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys
# # import unittest
# # import time
# # from bs4 import BeautifulSoup
# # import pandas as pd
# #
# # def livability_index(county_name):
# #     scores = []
# #     if county_name is not None:
# #
# #         driver = webdriver.Chrome("C:/Users/Akshay/Desktop/Masters Project/S_SQUARE_LAB/chromedriver_win32/chromedriver.exe")
# #         driver.get("https://livabilityindex.aarp.org/")
# #         driver.delete_all_cookies()
# #         elem = driver.find_element_by_name("address")
# #         elem.clear()
# #
# #         county_name_l = county_name + ", NY, USA"
# #         elem.send_keys(county_name_l)
# #         elem.send_keys(Keys.RETURN)
# #
# #         time.sleep(3)
# #         page_source = driver.page_source
# #         soup = BeautifulSoup(page_source, 'html.parser')
# #         results = str(soup.find(id='livability-total-score'))
# #         categories = soup.find_all('div', class_=['twodigits'])
# #         driver.close()
# #         results = results.split('">')
# #         scores.append(county_name)
# #         scores.append(results[1][0:2])
# #
# #         for i in range(0, len(categories)):
# #             category = str(categories[i])
# #             category = category.split('">')
# #             scores.append(category[1][0:2])
# #
# #         return scores
# #     return "Something went Wrong, Error"
# # # counties_list = ['Albany County', 'Allegany County', 'Bronx County', 'Broome County',
# # #  'Cattaraugus County', 'Cayuga County', 'Chautauqua County', 'Chemung County',
# # #  'Chenango County', 'Clinton County', 'Columbia County', 'Cortland County',
# # #  'Delaware County', 'Dutchess County', 'Erie County', 'Essex County',
# # #  'Franklin County', 'Fulton County', 'Genesee County', 'Greene County',
# # #  'Hamilton County', 'Herkimer County', 'Jefferson County', 'Kings County',
# # #  'Lewis County', 'Livingston County', 'Madison County', 'Monroe County',
# # #  'Montgomery County', 'Nassau County', 'New York County', 'Niagara County',
# # #  'Oneida County', 'Onondaga County', 'Ontario County', 'Orange County',
# # #  'Orleans County', 'Oswego County', 'Otsego County', 'Putnam County',
# # #  'Queens County', 'Rensselaer County', 'Richmond County', 'Rockland County',
# # #  'St. Lawrence County', 'Saratoga County', 'Schenectady County',
# # #  'Schoharie County', 'Schuyler County', 'Seneca County', 'Steuben County',
# # #  'Suffolk County', 'Sullivan County', 'Tioga County', 'Tompkins County',
# # #  'Ulster County', 'Warren County', 'Washington County', 'Wayne County',
# # #  'Westchester County', 'Wyoming County', 'Yates County']
# #
# #
# #
# # counties_list = ['Hamilton County', 'Herkimer County', 'Jefferson County', 'Kings County',
# #  'Lewis County', 'Livingston County', 'Madison County', 'Monroe County',
# #  'Montgomery County', 'Nassau County', 'New York County', 'Niagara County',
# #  'Oneida County', 'Onondaga County', 'Ontario County', 'Orange County',
# #  'Orleans County', 'Oswego County', 'Otsego County', 'Putnam County',
# #  'Queens County', 'Rensselaer County', 'Richmond County', 'Rockland County',
# #  'St. Lawrence County', 'Saratoga County', 'Schenectady County',
# #  'Schoharie County', 'Schuyler County', 'Seneca County', 'Steuben County',
# #  'Suffolk County', 'Sullivan County', 'Tioga County', 'Tompkins County',
# #  'Ulster County', 'Warren County', 'Washington County', 'Wayne County',
# #  'Westchester County', 'Wyoming County', 'Yates County']
# #
# #
# #
# #
# # templist=[]
# # for county in counties_list:
# #     templist.append(livability_index(county))
# #
# #
# # county,TotalScore, Housing,Neighborhood, Transportation,Environment, Health, Engagement, Opportunity, i=[],[],[],[],[],[],[],[],[], 0
# #
# # for element in templist:
# #         county.append(element[0])
# #         TotalScore.append(element[1])
# #         Housing.append(element[2])
# #         Neighborhood.append(element[3])
# #         Transportation.append(element[4])
# #         Environment.append(element[5])
# #         Health.append(element[6])
# #         Engagement.append(element[7])
# #         Opportunity.append(element[8])
# #
# # d = {'county_name':county,'totalScore':TotalScore,'housing':Housing,'neighborhood':Neighborhood,
# #      'transportation':Transportation, 'environment':Environment,'health':Health,'engagement':Engagement,'opportunity':Opportunity}
# # df = pd.DataFrame(d, columns=['county_name','totalScore','housing','neighborhood','transportation', 'environment','health','engagement','opportunity'])
# # # df = pd.DataFrame(d)
# # df.to_csv("liviability_index_data.csv", mode='w', index= False, header=True)
# # # df.to_csv("liviability_index_data.csv", mode='a', index= False, header=False)
#
#
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import unittest
# import time
# from bs4 import BeautifulSoup
# import pandas as pd
#
#
# zipcodes = pd.read_csv("ny-zip-code-latitude-and-longitude.csv")
# zipcodes_list = zipcodes['zipcode'].tolist()
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome("C:/Users/Akshay/Desktop/Masters Project/S_SQUARE_LAB/chromedriver_win32/chromedriver.exe",
#                           options=chrome_options)
# driver.get("https://livabilityindex.aarp.org/")
# driver.delete_all_cookies()
#
#
# for zipcode in zipcodes_list:
#     scores = []
#     if zipcode is not None:
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument("--headless")
#         driver = webdriver.Chrome(
#             "C:/Users/Akshay/Desktop/Masters Project/S_SQUARE_LAB/chromedriver_win32/chromedriver.exe",
#             options=chrome_options)
#         driver.get("https://livabilityindex.aarp.org/")
#         driver.delete_all_cookies()
#         elem = driver.find_element_by_name("address")
#         elem.clear()
#         # zipcode_temp = 'New York, NY '+str(zipcode)+', USA'
#         elem.send_keys(zipcode)
#         elem.send_keys(Keys.RETURN)
#         time.sleep(3)
#         page_source = driver.page_source
#         soup = BeautifulSoup(page_source, 'html.parser')
#         results = str(soup.find(id='livability-total-score'))
#         categories = soup.find_all('div', class_=['twodigits', 'threedigits'])
#         print(categories)
#         driver.close()
#         results = results.split('">')
#         scores.append(zipcode)
#         scores.append(results[1][0:2])
#         for i in range(0, len(categories)):
#             category = str(categories[i])
#             category = category.split('">')
#             scores.append(category[1][0:2])
#         try:
#             d = {'zipcode': [scores[0]], 'totalScore': [scores[1]], 'housing': [scores[2]], 'neighborhood': [scores[3]],
#                  'transportation': [scores[4]], 'environment': [scores[5]], 'health': [scores[6]], 'engagement': [scores[7]],
#                  'opportunity': [scores[8]]}
#             df = pd.DataFrame(d)
#             df.to_csv("ny_zip_code_lat_lon_details.csv", mode='a', index=False, header=False)
#             print(zipcode, ' data is loaded')
#         except:
#             print(zipcode, ' has an error')
#
#
#
#
#
#
#
#
#
#
