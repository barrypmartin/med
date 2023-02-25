# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 09:35:22 2023

@author: barry
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 07:12:47 2023

@author: barry
"""

import time #for time loops
import numpy as np #probability functions
import pandas as pd
import plotly.express as px # interactive charts
import streamlit as st #web development
#import "https://github.com/barrypmartin/med/blob/pages/File%20Upload.py"



#read csv file from a url
dataset_url = "https://raw.githubusercontent.com/barrypmartin/medical/main/processed_cleveland_simple.csv"

@st.experimental_memo()

def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

df = get_data()

# dashboard title
st.title("Heart attack tracker")

# top-level filters
job_filter = st.selectbox("Select Age", pd.unique(df["age"]))

# creating a single-element container
placeholder = st.empty()

# dataframe filter
df = df[df["age"] == job_filter]

# near real-time / live feed simulation
for seconds in range(200):
                                #np.random.choice
    df["age_new"] = df["age"] * np.mean(range(1, 5))
    df["bldpress_new"] = df["restbldpress"] * np.mean(range(1, 5))
                                              #np.random.choice
    # creating KPIs
    avg_age = np.mean(df["age_new"])

    count_married = int(
        df[(df["chol"] == "maxhrtrate")]["chol"].count()
        + np.mean(range(1, 30))
    )
    
    height= np.mean(df["bldpress_new"])

with placeholder.container():

      # create three columns
      kpi1, kpi2, kpi3 = st.columns(3)

      # fill in those three columns with respective metrics or KPIs
      kpi1.metric(
          label="Age ⏳",
          value=round(avg_age),
          delta=round(avg_age) - 10,
      )
      
      kpi2.metric(
          label="Cholesterol Levels ",
          value=int(count_married),
          delta=-10 + count_married,
      )
      
      kpi3.metric(
          label="Cholestorol Predictor",
          value=f" {round(height,2)} ",
          delta=-round( height/ count_married) * 100,
      )

      # create two columns for charts
      fig_col1, fig_col2 = st.columns(2)
      with fig_col1:
          st.markdown("### First Chart")
          fig = px.density_heatmap(
              data_frame=df, y="age_new", x="chol"
          )
          st.write(fig)
          
          with fig_col2:
           st.markdown("### Second Chart")
           fig2 = px.histogram(data_frame=df, x="age_new")
           st.write(fig2)

           st.markdown("### Detailed Data View")
           st.dataframe(df)
           time.sleep(1)
          
           st.sidebar.title("File Uploader")

           # Use the file uploader widget to allow users to upload a file
           file = st.sidebar.file_uploader("Upload a file", type=["csv"])

           # Check if a file was uploaded by the user
           if file is not None:
               # Use pandas to read the CSV file
               data = pd.read_csv(file)

               # Display the data in a table
               st.write("Here's the data you uploaded:")
               st.write(data)



