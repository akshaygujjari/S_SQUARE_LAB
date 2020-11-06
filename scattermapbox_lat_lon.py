import geojson
import pandas as pd
import math


from shapely.geometry import Point, Polygon


# Create a Polygon
coords = []


lat, lon = [], []
lat1, lat2, lat3, lon1, lon2, lon3 = 0,0,0,0,0,0
with open("Data/counties.geojson") as f:
    gj = geojson.load(f)

features = gj['features']

for j in range(0, 62):
  lat1, lat2, lat3, lon1, lon2, lon3 = 0, 0, 0, 0, 0, 0
  for i in range(0, len(features[j].geometry.coordinates[0][0])):
  #   feature =  features[j].geometry.coordinates[0][0][i][::-1]
  #   coords.append(feature)
  # poly = Polygon(coords)
  # donut = Point(poly.centroid).buffer(2.0).difference(Point(poly.centroid).buffer(1.0))
  # donut.centroid.wkt
  # donut.representative_point().wkt
  # print(donut.centroid.wkt, j)
    lon1 += features[j].geometry.coordinates[0][0][i][0]
    lat1 += features[j].geometry.coordinates[0][0][i][1]
  # lat3 = lat1 + ((lat2 - lat1) / 2)
  # lon3 = lon1 + ((lon2 - lon1) / 2)
  #
  # lon.append(lon3)
  # lat.append(lat3)


  # lon.append((lon1+lat3)/3)
  # lat.append((lat1++lat3)/3)


  # Bx = math.cos(lat2) * math.cos(lon2 - lon1)
  # By = math.cos(lat2) * math.sin(lon2 - lon1)
  latMid = lat1/i
  # math.sqrt((math.cos(lat1) + Bx) * (math.cos(lat1) + Bx) + By * By))
  lonMid = lon1 /i

#
d = {'lon': lon, 'lat': lat}
df = pd.DataFrame(d, columns=['lon', 'lat'])
df.to_csv("lon_lat.csv", mode='w', index=False, header=True)

