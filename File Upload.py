# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 08:50:04 2023

@author: barry
"""

import streamlit as st
import pandas as pd

def file_upload():
    
    st.write("You selected file_upload")
    # Use the file uploader widget to allow users to upload a file
    file = st.file_uploader("Upload a file", type=["csv"])

    # Check if a file was uploaded by the user
    if file is not None:
        # Use pandas to read the CSV file
        data = pd.read_csv(file)

        # Display the data in a table
        st.write("Here's the data you uploaded:")
        st.write(data)

def function_2():
    st.write("You selected Function 2")

def function_3():
    st.write("You selected Function 3")

st.sidebar.title("Function Menu")

# Define a dictionary mapping option labels to functions
function_map = {
    "file_upload": file_upload,
    "Function 2": function_2,
    "Function 3": function_3
}

# Use the selectbox widget to allow users to choose a function
function_choice = st.sidebar.selectbox("Select a function", list(function_map.keys()))

# Call the function corresponding to the selected option
function_map[function_choice]()
