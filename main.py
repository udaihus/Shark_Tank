import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Shark Tank India Dataset.csv")
df.head()

# filer for the episode
select_episode = st.sidebar.multiselect(
    "Select Episode number",
    options=df['episode_number'].unique(),
    default=[]
)
#created a copy of the data set
f_df = df.copy()

names = ['ashneer_deal', 'anupam_deal', 'aman_deal', 'namita_deal', 'vineeta_deal', 'peyush_deal', 'ghazal_deal']

# Sidebar filter: Multi-select for sharks
selected_sharks = st.sidebar.multiselect(
    'Select Sharks',
    options=names,
    default=[]  # Default select all sharks
)
if not selected_sharks and not select_episode:
    st.write("Displaying all data (No filters applied):")
    st.dataframe(f_df)
else:    
    # Initialize a filter condition with all rows (True)
    filter_condition = pd.Series([True] * len(f_df))

    # Apply the filter for each selected shark
    for shark in selected_sharks:
        filter_condition &= f_df[shark] == 1  # Include rows where the shark made a deal

    if select_episode:
        filter_condition &= df['episode_number'].isin(select_episode)

    # Apply the filter to the DataFrame
    filtered_df = f_df[filter_condition]

    # Display the filtered DataFrame
    st.write(f"Filtered Data (Sharks Selected: {', '.join(selected_sharks)}):")
    st.dataframe(filtered_df)

