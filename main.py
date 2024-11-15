import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")

df = pd.read_csv("Shark Tank India Dataset.csv")
df.head()

#----------------------------------------------------------------------------------------------------

#Title
st.markdown("""
    <h1 style="text-align: center; color: #1E90FF; font-family: Arial, sans-serif; font-size: 65px; margin-top:-40px;background-color: #D3D3D3;">
        Shark Tank India - Analysis 2024
    </h1>
""", unsafe_allow_html=True)

names = ['ashneer_deal', 'anupam_deal', 'aman_deal', 'namita_deal', 'vineeta_deal', 'peyush_deal', 'ghazal_deal']
#----------------------------------------------------------------------------------------------------


# Hussain Udaipurwala
# Score card

# User filter to select a Shark or show all
shark_names = ['ALL'] + [name.replace('_deal', '') for name in names]
selected_shark = st.sidebar.selectbox("Select a shark to see the total investment", shark_names)

# Calculate total investment for the selected shark or all sharks
if selected_shark == 'ALL':
    total_inv = (df[names].multiply(df['deal_amount'], axis=0)).sum(axis=0)
    tot1_in_crs = round(total_inv.sum() / 100, 2)  # Convert from lakhs to crores
    heading = "Total Invested Amount by All Sharks"
else:
    selected_shark_col = f"{selected_shark.lower()}_deal"
    shark_Dea = df[df[selected_shark_col] == 1]
    totl = shark_Dea['deal_amount'].sum()
    tot1_in_crs = totl / 100  # Convert from lakhs to crores
    heading = f"Amount Invested by - {selected_shark}"

# Create a scorecard box
scorecard_html = f"""
<div style="background-color: #f0f4f8; padding: 10px 10px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); width: 170px; margin-top: 10px; margin-right: 5px; border: 3px solid yellow;">
    <h2 style="color: #333; text-align: left; font-size: 14px; font-weight: bold; margin-bottom: 5px;">{heading}</h2>
    <h1 style="color: #4CAF50; text-align: left; font-size: 20px; font-weight: bold; margin-top: 5px;">{round(tot1_in_crs, 2)} Cr</h1>
</div>
"""
#----------------------------------------------------------------------------------------------------
#Hussain Udaipurwala

# Calculate the number of deals for the selected shark or all sharks
if selected_shark == 'ALL':
    # Count the total number of deals made by all sharks (where value is 1 in their respective columns)
    total_deals = df[names].sum().sum()  # Sum all deals by all sharks
    heading_deals = "Total Number of Deals by All Sharks"
else:
    selected_shark_col = f"{selected_shark.lower()}_deal"
    # Count the number of deals for the selected Shark
    shark_deals_count = df[selected_shark_col].sum()  # Count how many '1's in the selected shark's deal column
    heading_deals = f"Number of Deals by - {selected_shark}"
    total_deals = shark_deals_count

# Create a scorecard box to display the deal count
scorecard_h = f"""
<div style="background-color: #f0f4f8; padding: 10px 15px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); width: 170px; margin-top: 10px; margin-left: 5px; border: 3px solid yellow;">
    <h2 style="color: #333; text-align: left; font-size: 14px; font-weight: bold; margin-bottom: 5px;">{heading_deals}</h2>
    <h1 style="color: #4CAF50; text-align: left; font-size: 20px; font-weight: bold; margin-top: 5px;">{total_deals} Deals</h1>
</div>
"""

#------------------------------------------------------------------------------------------------------
# Hussain Udaipurwala

if selected_shark =='ALL':
    highest_Deal = df[df[names].sum(axis=1) > 0]['deal_amount'].max()
    head_deal = "Highest Deal Amount by All Sharks"
else:
    selected_shark_col = f"{selected_shark.lower()}_deal"
    highest_Deal = df[df[selected_shark_col] == 1]['deal_amount'].max()
    head_deal = f"Highest Deal by {selected_shark}"

# Create a scorecard box to display the max deal
scorecard_ht = f"""
<div style="background-color: #f0f4f8; padding: 10px 10px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); width: 170px; margin-top: 10px; margin-right: 5px; border: 3px solid yellow;">
    <h2 style="color: #333; text-align: left; font-size: 14px; font-weight: bold; margin-bottom: 5px;">{head_deal}</h2>
    <h1 style="color: #4CAF50; text-align: left; font-size: 20px; font-weight: bold; margin-top: 5px;">{highest_Deal} Lakhs</h1>
</div>
"""

# Display the scorecard box
col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])

with col1:
    st.markdown(scorecard_html, unsafe_allow_html=True)

with col2:
    st.markdown(scorecard_h, unsafe_allow_html=True)

with col3:
    st.markdown(scorecard_ht, unsafe_allow_html=True)

#----------------------------------------------------------------------------------------------------
#Hussain's Code:

# How much each shark's invested with the count of deal

shark_investment = {}
shark_investment_count = {}

for shark in names:
    shark_deals = df[df[shark]==1]
    total_investment = shark_deals['deal_amount'].sum()
    total_investement_in_crs = round((total_investment / 100),2) # it will be in Crores
    total_deals =shark_deals.shape[0]
    shark_investment[shark.replace('_deal',"")] = total_investement_in_crs
    shark_investment_count[shark.replace("_deal","")] = total_deals

shark_investment_df = pd.DataFrame({
    'Shark Name': list(shark_investment.keys()),
    'Total Investment (in Crs)': list(shark_investment.values()),
    'Total Investment Count': list(shark_investment_count.values())
})

# shark_investment_df = pd.DataFrame(list(shark_investment.items()),columns=['Shark Name','Total Investment (in Crs)'])

#st.title('Shark Tank India - Total Investment by Each Shark (in Crs)')
st.markdown(
    "<h3 style='text-align: center; color: #33;'>Shark Tank India - Total Investment by Each Shark (in Crs)</h3>",
    unsafe_allow_html=True
)
# col6 = st.columns([1])

# with col6[0]:
fig = go.Figure()

# Line plot for Total Investment in Crs
fig.add_trace(go.Scatter(
    x=shark_investment_df['Shark Name'],
    y=shark_investment_df['Total Investment (in Crs)'],
    mode='lines+markers',
    name='Total Investment (in Crs)',
    line=dict(color='royalblue', width=4),
    marker=dict(size=10, symbol='circle', color='royalblue', line=dict(width=2, color='black')),
    opacity=0.8
))

# Line plot for Total Investment Count
fig.add_trace(go.Scatter(
    x=shark_investment_df['Shark Name'],
    y=shark_investment_df['Total Investment Count'],
    mode='lines+markers',
    name='Total Investment Count',
    line=dict(color='darkorange', width=4, dash='dot'),
    marker=dict(size=10, symbol='square', color='darkorange', line=dict(width=2, color='black')),
    opacity=0.8,
    yaxis='y2'
))

# Add secondary y-axis for Total Investment Count
fig.update_layout(
    title="Total Investment and Deal Count by Each Shark",
    xaxis_title="Shark Name",
    yaxis_title="Total Investment (in Crs)",
    yaxis=dict(
        title="Total Investment (in Crs)",
        side="left",
        range=[0, shark_investment_df['Total Investment (in Crs)'].max() + 2],
        showgrid=True,  # Show grid lines for better readability
        gridcolor='rgba(0, 0, 0, 0.1)',  # Light grid color
        gridwidth=2,  # Grid lines width
        griddash='dot'  # Grid lines are dotted
    ),
    yaxis2=dict(
        title="Total Investment Count",
        side="right",
        overlaying="y",
        range=[0, shark_investment_df['Total Investment Count'].max() + 2],
        showgrid=True,  # Show grid lines for better readability on secondary axis
        gridcolor='rgba(0, 0, 0, 0.1)',  # Light grid color
        gridwidth=2,  # Grid lines width
        griddash='dot',  # Dotted grid lines
        position=0.95  # Position of the secondary y-axis
    ),
    legend=dict(x=0.8, y=0.1, traceorder='normal', orientation='h'),
    template="plotly_white",
    plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
    margin=dict(l=50, r=50, t=40, b=60),  # Adjust margins to prevent clipping
    showlegend=True
)

col6 = st.columns(1)
with col6[0]:
    st.plotly_chart(fig)

#----------------------------------------------------------------------------------------------------
# Nissi Grace:

# Map shark column names to proper names for display
# Shark names and mappings
# shark_names = {
#     'ashneer_deal': 'Ashneer',
#     'anupam_deal': 'Anupam',
#     'aman_deal': 'Aman',
#     'namita_deal': 'Namita',
#     'vineeta_deal': 'Vineeta',
#     'peyush_deal': 'Peyush',
#     'ghazal_deal': 'Ghazal'
# }

# # Streamlit graph Title
# st.markdown(
#     "<h3 style='text-align: center; color: #33;'>Shark Equity Analysis for Brands with Deals</h3>",
#     unsafe_allow_html=True
# )

# # Sidebar for Shark Selection
# selected_shark_name = st.sidebar.selectbox("Select a Shark to Analyze", list(shark_names.values()))

# # Get the corresponding column name for the selected shark
# selected_shark_column = [key for key, value in shark_names.items() if value == selected_shark_name][0]

# # Filter rows where the selected shark made a deal
# shark_deals_df = df[df[selected_shark_column] == 1]

# # Visualization
# if not shark_deals_df.empty:
#     # Extract required columns for the plot
#     brands = shark_deals_df['brand_name']  # X-axis: Brand names
#     ask_equity = shark_deals_df['ask_equity']  # Pitcher's asked equity
#     equity_per_shark = shark_deals_df['equity_per_shark']  # Average equity per shark
#     deal_equity = shark_deals_df['deal_equity']  # Final equity in the deal

#     # Create a line plot with a black background
#     fig, ax = plt.subplots(figsize=(6, 4), facecolor='black')  # Smaller size and black background
#     ax.set_facecolor('black')  # Set the axis background color to black

#     # Plotting the lines
#     ax.plot(brands, ask_equity, marker='o', label='Ask Equity (%)', color='blue')
#     ax.plot(brands, equity_per_shark, marker='o', label='Equity Per Shark (%)', color='orange')
#     ax.plot(brands, deal_equity, marker='o', label='Deal Equity (%)', color='green')

#     # Customize the plot
#     ax.set_title(f'Equity Comparison for {selected_shark_name}', fontsize=16, color='white')
#     ax.set_xlabel('Brand Name', fontsize=12, color='white')
#     ax.set_ylabel('Equity (%)', fontsize=12, color='white')
#     ax.legend(fontsize=10, loc='upper left', facecolor='black', edgecolor='white', labelcolor='white')

#     # Remove grid lines
#     ax.grid(False)

#     # Rotate x-axis labels and set them in white color
#     plt.xticks(rotation=90, ha='right', color='white')
#     plt.yticks(color='white')

#     # Display the plot in Streamlit
#     st.pyplot(fig)

# Shark names and mappings
shark_names = {
    'ashneer_deal': 'Ashneer',
    'anupam_deal': 'Anupam',
    'aman_deal': 'Aman',
    'namita_deal': 'Namita',
    'vineeta_deal': 'Vineeta',
    'peyush_deal': 'Peyush',
    'ghazal_deal': 'Ghazal'
}

# Streamlit graph Title
st.markdown(
    "<h3 style='text-align: center; color: #33;'>Shark Equity Analysis for Brands with Deals</h3>",
    unsafe_allow_html=True
)

# Sidebar for Shark Selection
selected_shark_name = st.sidebar.selectbox("Select a Shark to Analyze", list(shark_names.values()))

# Get the corresponding column name for the selected shark
selected_shark_column = [key for key, value in shark_names.items() if value == selected_shark_name][0]

# Filter rows where the selected shark made a deal
shark_deals_df = df[df[selected_shark_column] == 1]

# Visualization
if not shark_deals_df.empty:
    # Extract required columns for the plot
    brands = shark_deals_df['brand_name']  # X-axis: Brand names
    ask_equity = shark_deals_df['ask_equity']  # Pitcher's asked equity
    equity_per_shark = shark_deals_df['equity_per_shark']  # Average equity per shark
    deal_equity = shark_deals_df['deal_equity']  # Final equity in the deal

    # Create a figure using Plotly
    fig = go.Figure()

    # Add lines with markers for Ask Equity, Equity per Shark, and Deal Equity
    fig.add_trace(go.Scatter(
        x=brands,
        y=ask_equity,
        mode='lines+markers',
        name='Ask Equity (%)',
        line=dict(color='blue', width=4, dash='dot'),  # Blue dashed line for Ask Equity
        marker=dict(size=10, symbol='square', color='blue', line=dict(width=2, color='black')),
        opacity=0.8,
        yaxis='y1'
    ))

    fig.add_trace(go.Scatter(
        x=brands,
        y=equity_per_shark,
        mode='lines+markers',
        name='Equity Per Shark (%)',
        line=dict(color='orange', width=4, dash='dash'),  # Orange dashed line for Equity per Shark
        marker=dict(size=10, symbol='circle', color='orange', line=dict(width=2, color='black')),
        opacity=0.8,
        yaxis='y1'
    ))

    fig.add_trace(go.Scatter(
        x=brands,
        y=deal_equity,
        mode='lines+markers',
        name='Deal Equity (%)',
        line=dict(color='green', width=4),  # Solid green line for Deal Equity
        marker=dict(size=10, symbol='diamond', color='green', line=dict(width=2, color='black')),
        opacity=0.8,
        yaxis='y1'
    ))

    # Update the layout with the black background, no grid lines, and two y-axes
    fig.update_layout(
        title=f'Equity Comparison for {selected_shark_name}',
        xaxis_title="Brand Name",
        yaxis_title="Equity (%)",
        plot_bgcolor='black',  # Black background for the plot
        template="plotly_dark",  # Dark theme for the entire plot
        margin=dict(l=50, r=50, t=40, b=60),  # Adjust margins to prevent clipping
        showlegend=True,
        legend=dict(x=0.8, y=0.1, traceorder='normal', orientation='h'),
        xaxis=dict(
            tickmode='array',
            tickvals=brands,
            ticktext=brands,
            tickangle=90,
            tickfont=dict(color='white'),  # White color for X-axis labels
            showgrid=False,  # Remove grid lines
            zeroline=False  # Remove the zero line
        ),
        yaxis=dict(
            title="Equity (%)",
            showgrid=True,
            gridcolor='rgba(255, 255, 255, 0.1)',  # Light grid color for readability
            gridwidth=1,
            tickfont=dict(color='white'),  # White color for Y-axis labels
            zeroline=False  # Remove the zero line
        ),
        # Optional: Add secondary y-axis if required for another metric (e.g., deal amount or count)
        # yaxis2=dict(
        #     title="Deal Amount",
        #     overlaying="y",
        #     side="right",
        #     showgrid=False,
        #     tickfont=dict(color='white')
        # )
    )

    # Display the plot in Streamlit
    st.plotly_chart(fig)


#----------------------------------------------------------------------------------------------------
# Neetu Kumari:
# Episode wise deal amount and count of deal # Line plot

#-----------------------------------------------------------------------------------------------------
