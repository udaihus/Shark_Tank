import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("Shark Tank India Dataset.csv")
df.head()

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

col2, col3 = st.columns([2,3])

# with col1:
#     st.header("Filters")
#     # Example filter options
#     filter_shark = st.selectbox("Select Shark:", ['All', 'Ashneer', 'Anupam', 'Aman', 'Namita', 'Vineeta', 'Peyush', 'Ghazal'])

with col2:

    st.write("Total Deal Amount Invested by Shark (in Crs): ")
    #st.dataframe(shark_investment_df)
    st.dataframe(shark_investment_df.style.set_properties(**{
        'text-align': 'center',
        'background-color': 'lightblue',  # Add background color to cells
        'color': 'black',                 # Text color
        'border-color': 'grey'            # Border color
    }).set_table_styles([{
        'selector': 'thead th',  # Style the header
        'props': [('background-color', 'darkblue'), ('color', 'white')]
    }, {
        'selector': 'thead th:nth-child(1)',
        'props': [('text-align', 'center')]  # Center align header for "Shark Name"
    }, {
        'selector': 'tbody td:nth-child(2)',
        'props': [('text-align', 'center')]   # Right align numeric columns (e.g., Total Investment)
    }]))

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
    fig.update_layout(
    height=350,  # height remains the same, but you can reduce it further if needed
    width=700,   # adjust width to reduce overall length
    margin=dict(l=10, r=20, t=30, b=60),  # tighter margins, especially at the bottom
    #xaxis_tickangle=-45,  # Rotate x-axis labels for better fit
    showlegend=False  # Hide legend if it's redundant (optional)
    )
    st.plotly_chart(fig)

#Shreyashi Graph:
#Total Investement count of each shark's

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

# Nissi Grace:
#Top 5 brank names based on the highest valuation /equity


# Neetu Kumari:
# Episode wise deal amount and count of deal # Line plot


# Hussain Udaipurwala
# Score card

# User filter to select a Shark or show all
shark_names = ['ALL'] + [name.replace('_deal',"")for name in names]
selected_shark = st.selectbox("Select a shark to see the total investment", shark_names)

# Calculate total investment for the selected shark or all sharks
if selected_shark == 'All':
    total_inv = (df[names].multiply(df['deal_amount'],axis=0)).sum(axis=0)
    tot1_in_crs = round(total_inv.sum()/ 100,2)
    heading = "Total Invested Amount by All Sharks"

else:
    selected_shark_col = f"{selected_shark.lower()}_deal"
    shark_Dea = df[df[selected_shark_col] == 1]
    totl = shark_Dea['deal_amount'].sum()
    tot1_in_crs = totl/100
    heading = f"Amount Investes by{selected_shark}"

# Create a scorecard box
scorecard_html = f"""
<div style="background-color: #f0f4f8; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); width: 300px;">
    <h2 style="color: #333; text-align: center;">{heading}</h2>
    <h1 style="color: #4CAF50; text-align: center;">{round(tot1_in_crs, 2)} Cr</h1>
</div>
"""

# Display the scorecard box
st.markdown(scorecard_html, unsafe_allow_html=True)

# Optionally display more details (such as a breakdown or graph)
st.write(f"Total deals made by {selected_shark if selected_shark != 'All' else 'All Sharks'}:")
st.write(df[selected_shark_col] if selected_shark != "All" else df[names].sum(axis=0))  # Shows deal count or investments
