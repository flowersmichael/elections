#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.colors as mcolors
import pandas as pd 
import plotly as py
import math
import time
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from itertools import cycle, islice
from sklearn.linear_model import LinearRegression, BayesianRidge
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error
import datetime
import operator 
from simple_colors import *
import colorama
from colorama import Fore
plt.style.use('fivethirtyeight')
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import csv
import os
import sys
import glob
import os.path
from pathlib import Path
import fnmatch
from simple_colors import * # pip install simple-colors
import warnings #fixed any warning in terminal
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype


# In[ ]:


def nn_2layers():
    df = pd.read_csv(csv_file)
    #Create category_columns and numeric_columns variables
    numeric_columns = []
    category_columns = []
    for col in df.columns:
        if is_string_dtype(df[col]) == True:
            category_columns.append(col)
        elif is_numeric_dtype(df[col]) == True:
            numeric_columns.append(col)
    #Create dummy variables for the category_columns and merge on the numeric_columns to create an X dataset
    category_columns = pd.get_dummies(df[category_columns])
    X = df[numeric_columns].merge(category_columns, left_index= True, right_index= True)
    #Create an y dataset
    y = df['totalvotes'].values
    # Split X and y into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    # Scale X_train and X_test
    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    # Create a neural network model with keras
    nn = tf.keras.models.Sequential()
    # Add a hidden layer with twice as many neurons as there are inputs. Use 'relu'
    n_input = len(X_train_scaled[0])

    n_hidden = n_input * 2
    n_hidden_layer2 = n_input * 2 #2nd hidden layer

    nn.add(tf.keras.layers.Dense(units=n_hidden, input_dim=n_input, activation='relu'))
    nn.add(tf.keras.layers.Dense(units=n_hidden_layer2, activation='relu')) #2nd hidden layer

    # add an output layer with a 'linear' activation function.
    nn.add(tf.keras.layers.Dense(units=1,  activation='linear'))
    # print a summary of the model
    print(nn.summary())
    # compile the model using the "adam" optimizer and "mean_squared_error" loss function
    nn.compile(loss='mean_squared_error' , optimizer='adam' , metrics=['mse'])
    # train the model for 100 epochs
    model = nn.fit(X_train_scaled, y_train, epochs=100)
    # predict values for the train and test sets
    y_train_pred = nn.predict(X_train_scaled)
    y_test_pred = nn.predict(X_test_scaled)
    # score the training predictions with r2_score()
    print(f"r2_score of y_train: {r2_score(y_train, y_train_pred)}")
    # score the test predictions with r2_score()
    print(f"r2_score of y_test: {r2_score(y_test, y_test_pred)}")


# In[ ]:


def nn_1layer():
    df = pd.read_csv(csv_file)
    #Create category_columns and numeric_columns variables
    numeric_columns = []
    category_columns = []
    for col in df.columns:
        if is_string_dtype(df[col]) == True:
            category_columns.append(col)
        elif is_numeric_dtype(df[col]) == True:
            numeric_columns.append(col)
    #Create dummy variables for the category_columns and merge on the numeric_columns to create an X dataset
    category_columns = pd.get_dummies(df[category_columns])
    X = df[numeric_columns].merge(category_columns, left_index= True, right_index= True)
    #Create an y dataset
    y = df['totalvotes'].values
    # Split X and y into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    # Scale X_train and X_test
    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    # Create a neural network model with keras
    nn = tf.keras.models.Sequential()
    # Add a hidden layer with twice as many neurons as there are inputs. Use 'relu'
    n_input = len(X_train_scaled[0])

    n_hidden = n_input * 2
    #n_hidden_layer2 = n_input * 2 #2nd hidden layer

    nn.add(tf.keras.layers.Dense(units=n_hidden, input_dim=n_input, activation='relu'))
    #nn.add(tf.keras.layers.Dense(units=n_hidden_layer2, activation='relu')) #2nd hidden layer

    # add an output layer with a 'linear' activation function.
    nn.add(tf.keras.layers.Dense(units=1,  activation='linear'))
    # print a summary of the model
    print(nn.summary())
    # compile the model using the "adam" optimizer and "mean_squared_error" loss function
    nn.compile(loss='mean_squared_error' , optimizer='adam' , metrics=['mse'])
    # train the model for 100 epochs
    model = nn.fit(X_train_scaled, y_train, epochs=100)
    # predict values for the train and test sets
    y_train_pred = nn.predict(X_train_scaled)
    y_test_pred = nn.predict(X_test_scaled)
    # score the training predictions with r2_score()
    print(f"r2_score of y_train: {r2_score(y_train, y_train_pred)}")
    # score the test predictions with r2_score()
    print(f"r2_score of y_test: {r2_score(y_test, y_test_pred)}")


# In[ ]:


def predict_2():
    from sklearn.ensemble import RandomForestRegressor
    df = pd.read_csv(csv_file)
    df = df[df.loc[:] != 'LIB'].dropna()
    df = df.drop(df.columns[0], axis=1)
    df.party = df.party.replace({'DEM': 1, 'REP': 2})
    dataset = df.drop(['state', 'party'],axis=1)
    # the last column is our label
    y_train = dataset.iloc[:,-1:]
    #drop last column of data
    X_train = dataset.iloc[:, :-1]
    #drop first colum of data
    X_test = dataset.iloc[:,1:]
    model = RandomForestRegressor(max_depth=5, random_state=1, n_estimators=1000).fit(X_train, y_train)
    y_pred = model.predict(X_train)
    print(y_pred)
    print(f"Predict_Score: {model.score(X_train, y_train)}")
    prediction = pd.DataFrame({'state':df.state,'party':df.party, 'prediction_2024': y_pred.astype(int)})
    my_colors = list(islice(cycle(['b', 'r']), None, len(prediction)))
    prediction.party = prediction.party.map({1: 'DEM', 2: 'REP'})
    prediction.groupby('party')['prediction_2024'].sum().plot.bar(ylabel= "candidatevotes", title="2024 Party Prediction", color=my_colors)
    predict_winner = prediction.groupby('party')['prediction_2024'].sum()
    print(predict_winner)
    plt.show()


# In[2]:


def minority_2(): 
    import plotly.figure_factory as ff
    import numpy as np 
    import pandas as pd
    import plotly as py

    NE_states = ['Georgia', 'South Carolina']
    df = pd.read_csv(csv_file)
    df = df[df['STNAME'].isin(NE_states)]

    values = df['TOT_POP'].tolist()
    fips = df['FIPS'].tolist()
    count=df['Black'].tolist()

    color = ["#8dd3c7", "#ffffb3", "#bebada", "#fb8072",
                "#80b1d3", "#fdb462", "#b3de69", "#fccde5",
                "#d9d9d9", "#bc80bd", "#ccebc5", "#ffed6f",
                "#8dd3c7", "#ffffb3", "#bebada", "#fb8072",
                "#80b1d3", "#fdb462", "#b3de69", "#fccde5",
                "#d9d9d9", "#bc80bd", "#ccebc5", "#ffed6f",
                "#8dd3c7", "#ffffb3", "#bebada", "#fb8072",
                "#80b1d3", "#fdb462", "#b3de69", "#fccde5",
                "#d9d9d9", "#bc80bd", "#ccebc5", "#ffed6f"]
    colorscale = color * 6

    fig = ff.create_choropleth(
        fips=fips, values=values,
        #colorscale=colorscale, round_legend_values=True,
        simplify_county=0, simplify_state=0,
        scope=NE_states, county_outline={'color': 'rgb(255,255,255)', 'width': 0.5},
        state_outline={'color': 'rgb(0,0,0)', 'width': 2},
        #show_hover=True, centroid_marker={'opacity': 1},
        legend_title='Population per county',
        title='Georgia vs South Carolina Population'

    )

    fig.layout.template = None
    fig.show()
    py.offline.plot(fig,
    filename='Georgia vs South Carolina.html',
    include_plotlyjs='https://cdn.plot.ly/plotly-1.42.3.min.js')


# In[3]:


def county_4():
    from urllib.request import urlopen
    import plotly as py
    import json
    import webbrowser
    df = pd.read_csv(csv_file)
    #df['fips'] = df['fips'].apply(lambda x: '0'+x if len(x) == 4 else x)
    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)
    #geojson = px.data.election_geojson()
    #df = counties_fips_color[(counties_fips_color["state_code"] == "GA") | (counties_fips_color["state_code"] == "FL")]
    states = ['GA', 'SC', 'FL']
    df = df[df["state_code"].isin(states)]
    #df = counties_fips_color
    fig = px.choropleth(df, geojson=counties, locations='fips', color='color',
                                scope="usa",
                            
                            hover_data=["state","county", "candidate", "total_votes"])
    fig.update_geos(
                #lonaxis_range=[20, 380],
                projection_scale=2.7,
                center=dict(lat=31, lon=-83),
                visible=True)                      
    fig.update_layout(title= {"text": "Georgia vs South Carolina & Florida'\n' 2020 swing states total_votes", "xanchor": "center", "x": 0.5, "y": 0.95}, 
        margin={"r":0,"t":0,"l":0,"b":0}, showlegend=False)
    fig.show()
    fig.write_html("myplot.html")
    url = 'file://file:///Users/hiep_pham/Desktop/Analysis_Projects/Final_Project/myplot.html'
    webbrowser.open(url, new=2)  # open in new tab


# In[4]:


def county_3():
    df = pd.read_csv(csv_file)
    plt.scatter(df.median_age,df.total_votes)
    plt.xlabel("median_age")
    plt.ylabel('Total_Votes')
    plt.title("median_age vs Total_Votes")


# In[5]:


def county_2():
    df = pd.read_csv(csv_file)
    y = df.total_votes
    X = df.population.values.reshape(-1, 1)
    model = LinearRegression().fit(X, y)
    y_pred = model.predict(X)
    plt.scatter(X,y)
    plt.plot(X, y_pred, color='red')
    plt.xlabel("Population")
    plt.ylabel('Total_Votes')
    plt.title("Population vs Total_Votes'\n' Linear Regression")


# In[6]:


def cost_3():
    df = pd.read_csv(csv_file)
    df = df[['year','House winner spending', 'Senate winner spending']] 
    df = df.sort_values(by='year', ascending=True)
    df.plot(
    x = 'year', 
    kind = 'barh', 
    stacked = True, 
    title = 'House winner vs. Senate winner Spending',)
    plt.xlabel('Spending')
    plt.show()


# In[7]:


def cost_2():
    df = pd.read_csv(csv_file)
    df = df[['year','Democrats', 'Republicans']] 
    df = df.sort_values(by='year', ascending=True)
    df.plot(
    x = 'year', 
    kind = 'barh', 
    stacked = True, 
    title = 'Democrats vs. Republican Spending',)
    plt.xlabel('Spending')
    plt.show()


# In[8]:


def df():
    df = pd.read_csv(csv_file)
    print(df)


# In[9]:


while True:
    plt.close()
    csv_file = input("Import CSV_file to analyze: ").strip()
    file_name1 = os.path.split(os.path.abspath(csv_file))[-1] 
    if len(csv_file) < 2: #hit enter to quit csv files while loop(enter is len = 1) 
        break  
    elif not file_name1.endswith('csv'):
        continue  # ignore it if not csv files
    file_name, file_extension = os.path.splitext(file_name1)   
    list1 = ["Option 1: Print Data Frame",
             "Option 2: Democrats vs. Republican Spending",
             "Option 3: House winner vs. Senate winner Spending"
            ]
    list2 = ["Option 1: Print Data Frame",
             "Option 2: Population vs Total_Votes & Linear Regression",
             "Option 3: Median Age vs Total_Votes",
             "Option 4: 2020 swing states total_votes(Georgia vs South Carolina & Florida)",
            ]
    list3 = ["Option 1: Print Data Frame",
             "Option 2: Georgia vs South Carolina Population",
            ]
    list4 = ["Option 1: Print Data Frame",
             "Option 2: 2024 Party Prediction (Randomforestclassifier)",
            ]
    list5 = ["Option 1: Print Data Frame",
             "Option 2: neural network with 1 hidden layer",
             "Option 3: neural network with 2 hidden layers",
            ]
    while True and len(file_name) > 3:
        if file_name.find('CostOf') != -1:
            print(blue(f"The following options are available for {file_name1}:"))
            print(*list1,sep='\n')
            func = input("Please input the option #: ")
            print("")
        elif file_name.find('president_counties') != -1:
            print(blue(f"The following options are available for {file_name1}:"))
            print(*list2,sep='\n')
            func = input("Please input the option #: ")
            print("")
        elif file_name.find('minority') != -1:
            print(blue(f"The following options are available for {file_name1}:"))
            print(*list3,sep='\n')
            func = input("Please input the option #: ")
            print("")
        elif file_name.find('president_dataset') != -1:
            print(blue(f"The following options are available for {file_name1}:"))
            print(*list4,sep='\n')
            func = input("Please input the option #: ")
            print("")
        elif file_name.find('senate_dataset') != -1:
            print(blue(f"The following options are available for {file_name1}:"))
            print(*list5,sep='\n')
            func = input("Please input the option #: ")
            print("")
        
        if func == "": #hit enter to quit function while loop(enter is len = 1) 
            break
        elif func not in ("1", "2", "3", "4", "5"):
             print(red("Typo! Please try again."))
        if func == "1" and file_name.find('CostOf') != -1:
                df()
        elif func == "2" and file_name.find('CostOf') != -1:
                cost_2()
        elif func == "3" and file_name.find('CostOf') != -1:
                cost_3()
        elif func == "1" and file_name.find('president_counties') != -1:
                df()       
        elif func == "2" and file_name.find('president_counties') != -1:
                county_2()
        elif func == "3" and file_name.find('president_counties') != -1:
                county_3()
        elif func == "4" and file_name.find('president_counties') != -1:
                county_4()
        elif func == "1" and file_name.find('minority') != -1:
               df()
        elif func == "2" and file_name.find('minority') != -1:
               minority_2()
        elif func == "1" and file_name.find('president_dataset') != -1:
               df()
        elif func == "2" and file_name.find('president_dataset') != -1:
               predict_2()
        elif func == "1" and file_name.find('senate_dataset') != -1:
               df()
        elif func == "2" and file_name.find('senate_dataset') != -1:
               nn_1layer()
        elif func == "3" and file_name.find('senate_dataset') != -1:
               nn_2layers()
        
        plt.show()
        plt.close()
 

