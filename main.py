import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("Shark Tank India Dataset.csv")
df.head()

# # filer for the episode
# select_episode = st.sidebar.multiselect(
#     "Select Episode number",
#     options=df['episode_number'].unique(),
#     default=[]
# )
# #created a copy of the data set
# f_df = df.copy()

# names = ['ashneer_deal', 'anupam_deal', 'aman_deal', 'namita_deal', 'vineeta_deal', 'peyush_deal', 'ghazal_deal']

# # Sidebar filter: Multi-select for sharks
# selected_sharks = st.sidebar.multiselect(
#     'Select Sharks',
#     options=names,
#     default=[]  # Default select all sharks
# )
# if not selected_sharks and not select_episode:
#     st.write("Displaying all data (No filters applied):")
#     st.dataframe(f_df)
# else:    
#     # Initialize a filter condition with all rows (True)
#     filter_condition = pd.Series([True] * len(f_df))

#     # Apply the filter for each selected shark
#     for shark in selected_sharks:
#         filter_condition &= f_df[shark] == 1  # Include rows where the shark made a deal

#     if select_episode:
#         filter_condition &= df['episode_number'].isin(select_episode)

#     # Apply the filter to the DataFrame
#     filtered_df = f_df[filter_condition]

#     # Display the filtered DataFrame
#     st.write(f"Filtered Data (Sharks Selected: {', '.join(selected_sharks)}):")
#     st.dataframe(filtered_df)

#Hussain's Code:
# How much each shark's invested

names = ['ashneer_deal', 'anupam_deal', 'aman_deal', 'namita_deal', 'vineeta_deal', 'peyush_deal', 'ghazal_deal']

shark_investment = {}

for shark in names:
    shark_deals = df[df[shark]==1]
    total_investment = shark_deals['deal_amount'].sum()
    total_investement_in_crs = round((total_investment / 100),2) # it will be in Crores
    shark_investment[shark.replace('_deal',"")] = total_investement_in_crs

shark_investment_df = pd.DataFrame(list(shark_investment.items()),columns=['Shark Name','Total Investment (in Crs)'])

st.title('Shark Tank India - Total Investment by Each Shark (in Crs)')

col1, col2, col3 = st.columns([1, 2, 2])

with col1:
    st.header("Filters")
    # Example filter options
    filter_shark = st.selectbox("Select Shark:", ['All', 'Ashneer', 'Anupam', 'Aman', 'Namita', 'Vineeta', 'Peyush', 'Ghazal'])

with col2:

    st.write("Total Deal Amount Invested by Shark (in Crs): ")
    st.dataframe(shark_investment_df)

#plotting graphs
with col3:

    fig = px.bar(shark_investment_df,
                x='Shark Name',
                y = 'Total Investment (in Crs)',
                title = "Total Investment by Each Shark",
                labels = {'Shark Name': 'Shark', 'Total Investment': 'Total Investment (in Crs)'},
                color = 'Shark Name',
                color_continuous_scale= 'viridis'
                )
    st.plotly_chart(fig)

#Shreyashi Graph:

shark_inv_count = {}

for shark in names:
    shark_inv_count[shark.replace("_deal","")] = df[shark].sum()

shark_count_df = pd.DataFrame(list(shark_inv_count.items()),columns=['Shark Name','Total Investment (in Count)'])

col4,col5,col6 = st.columns([1,2,3])
with col6:

    fig2 = px.bar(shark_count_df,
                x='Shark Name',
                y = 'Total Investment (in Count)',
                title = "Total Number of Investment by Each Shark",
                labels = {'Shark Name': 'Shark', 'Total Investment (in Count)':'Number of Investment'},
                color = 'Shark Name',
                color_continuous_scale= 'viridis'
                )
    fig2.update_layout(
    height=350,  # height remains the same, but you can reduce it further if needed
    width=700,   # adjust width to reduce overall length
    margin=dict(l=60, r=20, t=30, b=60),  # tighter margins, especially at the bottom
    #xaxis_tickangle=-45,  # Rotate x-axis labels for better fit
    showlegend=False  # Hide legend if it's redundant (optional)
    )
    st.markdown("""
    <style>
    .streamlit-expanderHeader {
        display: none;
    }
    .block-container {
        padding-left: 5rem;  /* Adjust the value as needed to shift the chart right */
    }
    </style>
    """, unsafe_allow_html=True)
    st.plotly_chart(fig2)
