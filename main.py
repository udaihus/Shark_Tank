import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Shark Tank India Dataset.csv")

#Top 5 rows of data
df.head()

# #rows & colums
# df.shape

# #Null values count of each columns
# df.isnull().sum()

# #checking the datatypes of the columns
# df.info()

# #columns count
# df.columns.size #27

# df.loc[df['age']<=25,'age_groups'] = 'Youth'
# df.loc[df['age'].between(26,60),'age_groups'] = 'Adult'
# df.loc[df['age']>=61,'age_groups'] = 'Senior'

st.sidebar.multiselect("Select Episode number",df['episode_number'].unique())

sharks = ['ashneer_present', 'anupam_present','aman_present', 'namita_present', 'vineeta_present', 'peyush_present']

selected_shark = st.sidebar.multiselect(
    "Select Sharks",
    sharks,
)

f_df = df.copy()

for shark in selected_shark:
    f_df = f_df[f_df['sharks'] == 1]

st.write(f"Filtered data (Shark selected: {', '.join(selected_shark)})")
st.dataframe(f_df)
st.write(f_df.head())