import libraries_used as lu
import read_data as rd
import read_csv_data as rcd


df = lu.pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')
search_bar = lu.dbc.Row(
    [
        lu.dbc.Col(lu.dbc.Input(type="search", placeholder="Search")),
        lu.dbc.Col(
            lu.dbc.Button("Search", color="primary", className="ml-2"),
            width="auto",
        ),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = lu.dbc.NavbarSimple(
    children=[
        search_bar,
    ],
    brand="Social Services Lab",
    brand_href="#",
    sticky="top",
)
body = lu.dbc.Container(
    [
        lu.html.Br(),
        lu.dbc.Row(
            [
                        lu.dcc.Dropdown(
                            id='211_data',
                            options=[{'label': i.title(), 'value': i} for i in rd.data_211_categories.values()],
                            value=rd.data_211_categories_l[0],
                            placeholder= "2-1-1 Data",
                            # className = "col-lg-4 col-md-4 col-sm-12",
                            style={'width':'36%'},
                            clearable=False,
                            searchable=False
                        ),
                        lu.dcc.Dropdown(
                            id='census_data',
                            options=[{'label': i.title(), 'value': i} for i in rd.census_data_columns],
                            value=None,
                            placeholder="Census Data",
                            style={'width': '34%'},
                            clearable=False,
                            searchable=False,
                        ),
                        lu.dcc.Dropdown(
                            id='map_level',
                            options=[{'label': i.title(), 'value': i} for i in rd.map_level],
                            value='Auto',
                            placeholder="Map level",
                            clearable=False,
                            searchable=False,
                            style={'width':'29%'},
                        )
                ],className = "col-lg-12 col-md-12 col-sm-12"),

        lu.html.Br(),
        lu.html.H2("New York State", style={'align':'center'}),
        lu.dbc.Row(
            [
                lu.html.Div(
                    [

                        #DropDown and Slider
                        lu.dcc.Graph(
                            id="feature-graphic",
                            style = {'width': '100%'},
                            figure={
                                "data": [
                                    dict(
                                        type="choroplethmapbox+scattermapbox",
                                        lat = rcd.lat_lon_data['latitude'],
                                        lon=rcd.lat_lon_data['longitude'],
                                        mode="markers",
                                        clickmode="event",
                                        marker=lu.go.scattermapbox.Marker(size=8, color='rgb(255, 0, 0)', opacity=0.7),
                                        showlegend=False,
                                        hoverinfo=rcd.census_2015_data.name,
                                        geojson=rd.counties,
                                        locations=rcd.census_2015_data.GEOID,
                                    )
                                ],
                                "layout": dict(
                                    hovermode="closest",
                                    clickmode="event",
                                    margin=dict(l=0, r=0, t=0, b=0),
                                    mapbox=dict(
                                        accesstoken="pk.eyJ1IjoiYWd1amphcmkiLCJhIjoiY2s2ZW83OHpnMGJiOTNtcWRzcHBhZWt6aiJ9.atHNPf4K3mdpAENGX4Gjdw",
                                        bearing=0,
                                        center=dict(lat=42.648613, lon=-73.761391),
                                        style="mapbox://styles/agujjari/ck6zfxkm62nwu1ip2gdx974ro",
                                        pitch=0,
                                        zoom=5.5,
                                    )
                                )
                            },
                        ),

                        lu.html.Br(),
                        lu.dcc.Slider(
                                id='year-slider',
                                min=min(rd.years),
                                max=max(rd.years),
                                value=max(rd.years),
                                marks={str(year): str(year) for year in rd.years},
                                step=None
                            )
                    ], className = "col-lg-9 col-md-9 col-sm-12", id  = 'map_container'
                ),


                        lu.html.Div([

                        ],
                        style={"margin-left":"auto","margin-right":"auto",'width': '100%'},
                        className = "col-lg-3 col-md-3 col-sm-12",
                        id = "living_index")

                #     ]
                # ),


            ]
        ),
    lu.dbc.Row(
            [

              lu.html.Div([
                # dcc.Graph(id="line_graph",style = {'width': '100%'}),

              ],
                style={'width': '100%', "height":"100%"},
                className="col-lg-12 col-md-12 col-sm-12",
                id="line_graph_div"),




            ]),
    ],
    # className="mt-4",
)

app = lu.dash.Dash(__name__, external_stylesheets=[lu.dbc.themes.BOOTSTRAP])
app.layout = lu.html.Div([navbar, body])








@app.callback(lu.Output('feature-graphic', 'figure'),
             [lu.Input('year-slider', 'value'),
              lu.Input('census_data', 'value'),
              lu.Input('211_data', 'value'),
              lu.Input('map_level', 'value')])
def census_data_fill(year, census_parameter, parameter_211, map_level):

  fig = lu.go.Figure()

  if census_parameter is not None:
      if "%" in census_parameter:
          census_parameter = census_parameter.replace("% of ", "pct_")
      if " " in census_parameter:
          census_parameter = census_parameter.replace(" ", "_")


  if parameter_211 is None:
      parameter_211 = 'B'

  if map_level is None:
      map_level = 'Auto'

  if map_level == "Auto" or map_level == "Counties":

      if str(year) == "2015":
          choloropeth_data = rcd.census_2015_data
          data_211_file = rcd._211_2015_data
      elif str(year) == "2016":
          choloropeth_data = rcd.census_2016_data
          data_211_file = rcd._211_2016_data
      elif str(year) == "2017":
          choloropeth_data = rcd.census_2017_data
          data_211_file = rcd._211_2017_data
      elif str(year) == "2018":
          choloropeth_data = rcd.census_2018_data
          data_211_file = rcd._211_2018_data
      else:
          choloropeth_data = rcd.census_dummy_data

      if parameter_211 is not None:
          key_list = list(rd.data_211_categories.keys())
          val_list = list(rd.data_211_categories.values())
          data_key = key_list[val_list.index(parameter_211)]

          data_211_file = data_211_file[data_211_file['category_code'] == data_key]
          data_211_file['category_code'].replace('', lu.np.nan, inplace=True)
          data_211_file.dropna(subset=['category_code'], inplace=True)
          data_211_file_count = data_211_file.groupby(['county','latitude', 'longitude'], as_index=False).count()
          data_211_file_count = data_211_file.groupby(['county','latitude', 'longitude'], as_index=False).count()
          data_211_file_count.rename(columns={'category_code': 'Total_Requests'}, inplace=True)

      fig = lu.px.scatter_mapbox(data_211_file_count, lat="latitude", lon="longitude", size="Total_Requests",
                                 size_max=30, zoom=10)
      if census_parameter is not None:

          fig.add_trace(lu.go.Choroplethmapbox(geojson=rd.counties, locations=choloropeth_data.GEOID, z=choloropeth_data[census_parameter],
                        colorscale="Blues", zmin=choloropeth_data[census_parameter].min(), hovertemplate = "<b>%{text}<b>",
                        zmax=choloropeth_data[census_parameter].max(), name = "", marker_opacity=1.0, marker_line_width=1,
                        text = choloropeth_data.name))
      else:
          choloropeth_data = rcd.census_dummy_data
          fig.add_trace(lu.go.Choroplethmapbox(geojson=rd.counties, locations=choloropeth_data.GEOID,text=choloropeth_data.name,
                                               hovertemplate = "<b>%{text}<b>",name = "", showscale = False,
                                               marker_opacity=1.0, marker_line_width=1,z=choloropeth_data['population']))


      fig.update_layout(mapbox_style="mapbox://styles/agujjari/ck6zfxkm62nwu1ip2gdx974ro",
                      mapbox_accesstoken="pk.eyJ1IjoiYWd1amphcmkiLCJhIjoiY2s2ZW83OHpnMGJiOTNtcWRzcHBhZWt6aiJ9.atHNPf4K3mdpAENGX4Gjdw",
                      clickmode="event", autosize=True, width=800, height=470,
                      margin={"r": 0, "t": 0, "l": 0, "b": 0},
                      mapbox_zoom=5.5, mapbox_center={"lat": 42.648613, "lon": -73.761391})

  else:

      if str(year) == "2015":
          data_211_file = rcd.zipcode_211_2015_data
      elif str(year) == "2016":
          data_211_file = rcd.zipcode_211_2016_data
      elif str(year) == "2017":
          data_211_file = rcd.zipcode_211_2017_data
      elif str(year) == "2018":
          data_211_file = rcd.zipcode_211_2018_data
      else:
          choloropeth_data = rcd.census_dummy_data

      if parameter_211 is not None:
          key_list = list(rd.data_211_categories.keys())
          val_list = list(rd.data_211_categories.values())
          data_key = key_list[val_list.index(parameter_211)]

          data_211_file = data_211_file[data_211_file['category_code'] == data_key]
          data_211_file['category_code'].replace('', lu.np.nan, inplace=True)
          data_211_file.dropna(subset=['category_code'], inplace=True)
          data_211_file_count = data_211_file.groupby(['zipcode','latitude', 'longitude'], as_index=False).count()
          data_211_file_count.rename(columns={'category_code': 'Total_Requests'}, inplace=True)

      choloropeth_data = rcd.zipcode_laton_lon_data

      fig = lu.px.scatter_mapbox(data_211_file_count, lat="latitude", lon="longitude", size="Total_Requests",
                                 size_max=30, zoom=10,text= 'zipcode', hover_name='zipcode')
      if census_parameter is not None:
          fig.add_trace(lu.go.Choroplethmapbox(geojson=rcd.zipcode_data, locations=choloropeth_data.zipcode,text=choloropeth_data.zipcode,
                                               showscale=False, marker_opacity=1.0, marker_line_width=1, z=choloropeth_data['dummy_column']))
      else:
          fig.add_trace(lu.go.Choroplethmapbox(geojson=rcd.zipcode_data, locations=choloropeth_data.zipcode, text=choloropeth_data.zipcode,
                        hovertemplate = "<b>Zip Code<b>: %{text}", showscale=False, marker_opacity=1.0, marker_line_width=1, name ='', z=choloropeth_data['dummy_column']))

      fig.update_layout(mapbox_style="mapbox://styles/agujjari/ck7v2ct2v02in1ippcn7eqx4z",
                        mapbox_accesstoken= "pk.eyJ1IjoiYWd1amphcmkiLCJhIjoiY2s2ZW83OHpnMGJiOTNtcWRzcHBhZWt6aiJ9.atHNPf4K3mdpAENGX4Gjdw",
                        clickmode="event", autosize=True, width=800, height=470,
                        margin={"r": 0, "t": 0, "l": 0, "b": 0},overwrite = True,
                        mapbox_zoom=5.5, mapbox_center= {"lat": 42.648613, "lon": -73.761391})

  return fig




@app.callback(
        lu.Output('living_index', 'children'),
        [lu.Input('feature-graphic', 'clickData'),
         lu.Input('map_level', 'value')])
def selected_county(selected_county, map_level):
  if selected_county is not None:

      if map_level is None:
          map_level = 'Auto'

      if map_level == "Auto" or map_level == "Counties":
          try:
              # selected_county = selected_county['points'][0]['text']
              selected_county = selected_county['points'][0]['marker.size']
              if selected_county > 0:
                  return  lu.no_update
              else:
                  selected_county = selected_county['points'][0]['text']
          except:
              selected_county = selected_county['points'][0]['text']

          scores = rcd.livability_index_data[(rcd.livability_index_data['county_name'] == selected_county)]
          scores = scores.values.tolist()
          if scores is not None:
              df = lu.pd.DataFrame(
                    {
                      "Categories": ["County Name", "Total Score", "Housing", "Neighborhood", "Transportation",
                                     "Environment", "Health", "Engagement", "Opportunity"],
                      "Score": scores[0],
                   })
          else:
              df = lu.pd.DataFrame(
                  {
                      "Categories": ["County Name", "Total Score", "Housing", "Neighborhood", "Transportation",
                                     "Environment", "Health", "Engagement", "Opportunity"],
                      "Score": [selected_county, 'N/A', 'N/A', 'N/A',
                                'N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                  })

          table = lu.dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, responsive=True, dark=True)
          return table
      else:
          selected_county = selected_county['points'][0]['text']
          scores = rcd.zipcode_livability_index_data[(rcd.zipcode_livability_index_data['zipcode'] == selected_county)]
          scores = scores.values.tolist()
          if scores !=[]:
              df = lu.pd.DataFrame(
                  {
                      "Categories": ["Zip Code", "Total Score", "Housing", "Neighborhood", "Transportation",
                                     "Environment", "Health", "Engagement", "Opportunity"],
                      "Score": scores[0],
                  })
          else:
              df = lu.pd.DataFrame(
                  {
                      "Categories": ["Zip Code", "Total Score", "Housing", "Neighborhood", "Transportation",
                                     "Environment", "Health", "Engagement", "Opportunity"],
                      "Score": [selected_county,'N/A','N/A','N/A','N/A',
                                'N/A','N/A','N/A','N/A'],
                  })
          table1 = lu.dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, responsive=True, dark=True)
          return table1



@app.callback(
        lu.Output('line_graph_div', 'children'),
        [lu.Input('feature-graphic', 'clickData'),
         lu.Input('year-slider', 'value'),
         lu.Input('census_data', 'value'),
         lu.Input('211_data', 'value'),
         lu.Input('map_level', 'value')])
def line_and_bar_graph(selected_county, year, census_data,data_211,map_level):
  if data_211 is None:
      data_211 = 'B'

  if map_level is None:
      map_level = 'Auto'

  if map_level == "Auto" or map_level == "Counties":
      if selected_county is not None:
        # selected_county = selected_county['points'][0]['text']
        try:
            # selected_county = selected_county['points'][0]['text']
            selected_county = selected_county['points'][0]['marker.size']
            if selected_county > 0:
                pass
            else:
                selected_county = selected_county['points'][0]['text']
        except:
            selected_county = selected_county['points'][0]['text']

        if str(year) == "2015":
            census_data = rcd.census_2015_data
            data_211_file = rcd._211_2015_data
        elif str(year) == "2016":
            census_data = rcd.census_2016_data
            data_211_file = rcd._211_2016_data
        elif str(year) == "2017":
            census_data = rcd.census_2017_data
            data_211_file = rcd._211_2017_data
        else:
            census_data = rcd.census_2018_data
            data_211_file = rcd._211_2018_data

        if data_211 is not None:
            key_list = list(rd.data_211_categories.keys())
            val_list = list(rd.data_211_categories.values())
            data_key = key_list[val_list.index(data_211)]
            if isinstance(selected_county, int):
                return  lu.no_update
            else:
                if selected_county == 'St. Lawrence County':
                    countyname = 'St. Lawrence'
                else:
                    countyname, error = selected_county.split()
            countyname = countyname.upper()
            data_211_file = data_211_file[data_211_file["county"] == countyname]
            data_211_file = data_211_file[data_211_file['category_code'] == data_key]
            data_211_file['category_code'].replace('', lu.np.nan, inplace=True)
            data_211_file.dropna(subset=['category_code'], inplace=True)
            y_data_line = lu.pd.DataFrame(data_211_file.groupby('category_sub').count())

            table_list, census_data_bar = [], []
            table_list = rd.census_data_columns[:]
            # table_list = table_list[1:]
            table_list.append(data_211)
            census_data = census_data[census_data["name"] == selected_county]
            census_data= census_data.values.tolist()
            census_data=census_data[0]
            temp = y_data_line['Unnamed: 0'].tolist()
            temp = sum(temp[1:])
            census_data.append(temp)
            census_data_bar = [i if i != 0 else 'N/A' for i in census_data[4:]]

            # dropdown_text = "Select a field from dropdown to add in the table:"
            # dropdown = lu.dcc.Dropdown(
            #     id='data_211_tbl',
            #     options=[{'label': i.title(), 'value': i} for i in rd.data_211_categories.values()],
            #     value=rd.data_211_categories_l[0],
            #     placeholder="2-1-1 Data",
            #     style={'width': '30%'})
    #_________________________________________________________________________________________________

    # ------------------------------------------------------------------------------------------------------
            table_header = 'Tabular View of the Data for '+ selected_county
            df = lu.pd.DataFrame(
                {
                    "Category": table_list,
                    "Value": census_data_bar,
                }
            )

            table = lu.dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, responsive=True, dark=True)
    # ------------------------------------------------------------------------------------------------------

            y_data_line = y_data_line['Unnamed: 0'].tolist()
            if len(y_data_line) == 0 or len(y_data_line) == 1:
                hide_bar_chart = True
            else:
                hide_bar_chart = False

                trace10 = lu.go.Bar( x=rd.data_211_sub_categories_text[data_key],
                                     y=y_data_line[1:],
                                     name='Bar Graph',
                                     marker=dict(color='#026E91'))

                layout2 = lu.go.Layout(title='Number of counts for each sub category in ' + selected_county)
                data2= [trace10]
                fig2 = lu.go.Figure(data=data2, layout=layout2)
                fig2.update_layout(xaxis_title="subcategories",
                                   yaxis_title="Total number of requests",
                                   font=dict(
                                   family="Courier New, monospace",
                                   size=18,
                                   color="#026E91"))

    # ------------------------------------------------------------------------------------------------------
            y = []
            _211_data_all_files = [rcd._211_2015_data, rcd._211_2016_data, rcd._211_2017_data, rcd._211_2018_data]

            for filename in _211_data_all_files:
                df_211_file = filename
                df_211_file = df_211_file[df_211_file["county"] == countyname]
                df_211_file = df_211_file[df_211_file['category_code'] == data_key]
                df_211_file['category_code'].replace('', lu.np.nan, inplace=True)
                df_211_file.dropna(subset=['category_code'], inplace=True)
                yf_data_line = lu.pd.DataFrame(df_211_file.groupby('category_sub').count())
                temp1 = yf_data_line['Unnamed: 0'].tolist()
                temp1 = sum(temp1[1:])
                y.append(temp1)

            line_data = ''.join(map(str, y))
            if line_data == '0000':
                hide_line_chart = True
            else:
                hide_line_chart = False

                trace2 = lu.go.Scatter(x=rd.years,
                                       y=y,
                                       mode='markers+lines',
                                       name = "Line Graph",
                                       marker=dict(color='#026E91'))

                layout1 = lu.go.Layout(title= 'Number of Requests for '+ data_211 + ' in '+ selected_county)
                data1 = [trace2]
                fig1 = lu.go.Figure(data=data1, layout=layout1)
                fig1.update_layout( xaxis_title="Years",
                                    yaxis_title=data_211,
                                    font=dict(
                                    family="Courier New, monospace",
                                    size=18,
                                    color="#026E91"))

            if selected_county is not None:
                if hide_line_chart is True and hide_bar_chart is False:
                    return lu.html.Br(), lu.html.H3(table_header, style={'align': 'center', 'color':'#026E91'}), lu.html.Br(),\
                           lu.html.Br(), table, lu.dcc.Graph(id="line_graph",figure=fig2),\
                           lu.html.Br(), lu.html.H2("No Data to display Line Chart", style={'align': 'center', 'color':'#026E91'})
                elif hide_bar_chart is True and hide_line_chart is False:
                    return lu.html.Br(), lu.html.H3(table_header, style={'align': 'center', 'color':'#026E91'}),lu.html.Br(),\
                           lu.html.Br(), table, lu.dcc.Graph(id="line_graph", figure=fig1),\
                           lu.html.Br(), lu.html.H2("No Data to display Bar Chart", style={'align': 'center', 'color':'#026E91'})
                elif hide_bar_chart is False and hide_line_chart is False:
                    return lu.html.Br(), lu.html.H3(table_header, style={'align': 'center', 'color':'#026E91'}),lu.html.Br()\
                          ,lu.html.Br(),table, lu.dcc.Graph(id="line_graph", figure=fig2),\
                           lu.dcc.Graph(id ="line_graph", figure = fig1)
                else:
                    return lu.html.Br(), lu.html.H3(table_header, style={'align': 'center', 'color':'#026E91'}), lu.html.Br(),\
                           lu.html.Br(), table
  else:
      if selected_county is not None:
          selected_county = selected_county['points'][0]['text']

          if str(year) == "2015":
              data_211_file = rcd.zipcode_211_2015_data
          elif str(year) == "2016":
              data_211_file = rcd.zipcode_211_2016_data
          elif str(year) == "2017":
              data_211_file = rcd.zipcode_211_2017_data
          else:
              data_211_file = rcd.zipcode_211_2018_data

          if data_211 is not None:
              key_list = list(rd.data_211_categories.keys())
              val_list = list(rd.data_211_categories.values())
              data_key = key_list[val_list.index(data_211)]
              data_211_file = data_211_file[data_211_file["zipcode"] == selected_county]
              data_211_file = data_211_file[data_211_file['category_code'] == data_key]
              data_211_file['category_code'].replace('', lu.np.nan, inplace=True)
              data_211_file.dropna(subset=['category_code'], inplace=True)
              y_data_line = lu.pd.DataFrame(data_211_file.groupby('category_sub').count())

              y_data_line = y_data_line['Unnamed: 0'].tolist()
              if len(y_data_line) == 0 or len(y_data_line) == 1:
                  hide_bar_chart = True
              else:
                  hide_bar_chart = False

                  trace11 = lu.go.Bar(x=rd.data_211_sub_categories_text[data_key],
                                      y=y_data_line[1:],
                                      name='Bar Graph',
                                      marker=dict(color='#026E91'))

                  layout11 = lu.go.Layout(title='Number of counts for each sub category in ' + str(selected_county))
                  data11 = [trace11]
                  fig11 = lu.go.Figure(data=data11, layout=layout11)
                  fig11.update_layout(xaxis_title="subcategories",
                                     yaxis_title="Total number of requests",
                                     font=dict(
                                         family="Courier New, monospace",
                                         size=18,
                                         color="#026E91"))

              # ------------------------------------------------------------------------------------------------------
              y = []
              _211_data_all_files = [rcd.zipcode_211_2015_data , rcd.zipcode_211_2016_data , rcd.zipcode_211_2017_data , rcd.zipcode_211_2018_data ]

              for filename in _211_data_all_files:
                  df_211_file = filename
                  df_211_file = df_211_file[df_211_file["zipcode"] == selected_county]
                  df_211_file = df_211_file[df_211_file['category_code'] == data_key]
                  df_211_file['category_code'].replace('', lu.np.nan, inplace=True)
                  df_211_file.dropna(subset=['category_code'], inplace=True)
                  yf_data_line = lu.pd.DataFrame(df_211_file.groupby('category_sub').count())
                  temp1 = yf_data_line['Unnamed: 0'].tolist()
                  temp1 = sum(temp1[1:])
                  y.append(temp1)

              line_data = ''.join(map(str, y))
              if line_data == '0000':
                  hide_line_chart = True
              else:
                  hide_line_chart = False

                  trace21 = lu.go.Scatter(x=rd.years,
                                         y=y,
                                         mode='markers+lines',
                                         name="Line Graph",
                                         marker=dict(color='#026E91'))

                  layout21 = lu.go.Layout(title='Number of Requests for ' + data_211 + ' in ' + str(selected_county))
                  data21 = [trace21]
                  fig21 = lu.go.Figure(data=data21, layout=layout21)
                  fig21.update_layout(xaxis_title="Years",
                                     yaxis_title=data_211,
                                     font=dict(
                                         family="Courier New, monospace",
                                         size=18,
                                         color="#026E91"))

              if selected_county is not None:
                  if hide_line_chart is True and hide_bar_chart is False:
                      return lu.html.Br(), lu.dcc.Graph(id="line_graph", figure=fig11)
                  elif hide_bar_chart is True and hide_line_chart is False:
                      return lu.html.Br(), lu.dcc.Graph(id="line_graph", figure=fig21)
                  elif hide_bar_chart is False and hide_line_chart is False:
                      return lu.html.Br(), lu.dcc.Graph(id="line_graph", figure=fig11), \
                             lu.dcc.Graph(id="line_graph", figure=fig21)
                  else:
                      return lu.html.Br()


@app.callback(lu.Output('feature-graphic', 'clickData'),
             [lu.Input('map_level', 'value')])
def reset_clickData(map_level):
    return None

@app.callback([lu.Output('census_data', 'style'),
              lu.Output('census_data', 'value')],
              [lu.Input('map_level', 'value')])
def reset_clickData(map_level):
    if  map_level == "Auto" or map_level == "Counties":
        return {'display': 'block', 'width':'34%'}, None
    else:
        return {'display': 'none'}, None



if __name__ == "__main__":
    # app.run_server(debug=True, port=8056)
    app.run_server(port=8056)
    # app.run_server()