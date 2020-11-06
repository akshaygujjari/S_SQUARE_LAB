import pandas as pd

df1 = pd.read_csv("2018_211_zipcode.csv")
df2 = pd.read_csv("ny-zip-code-latitude-and-longitude.csv")

# df2["Client's_County"] = df2["Client's_County"].str.upper()
df = pd.merge(df1, df2, how='inner', on="zipcode")
df.to_csv("zipcode_2018_2011.csv")


# import plotly.express as px
# # px.set_mapbox_access_token(open(".mapbox_token").read())
# df = px.data.carshare()
# fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon",     color="peak_hour", size="car_hours",
#                   color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)
# fig.show()
#
# # print(df)