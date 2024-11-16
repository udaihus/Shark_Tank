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




#Shreyashi Graph strat---------------------------------------------------------------------------------------:

# Load your dataset
data = pd.read_csv("Shark Tank India Dataset.csv")

# List of shark names to be used as column identifiers for investments
names = ['ashneer_deal', 'anupam_deal', 'aman_deal', 'namita_deal', 'vineeta_deal', 'peyush_deal', 'ghazal_deal']

# Calculate how many brands each shark invested in (i.e., count of deals)
shark_investment_count = {}

for shark in names:
    shark_deals = data[data[shark] == 1]  # Filter data for rows where the shark made a deal
    total_deals = shark_deals.shape[0]  # Count the number of rows (deals) the shark has made
    shark_investment_count[shark.replace('_deal', '')] = total_deals  # Add shark name and number of deals

# Create a DataFrame to store shark investment data (count of deals)
shark_investment_count_df = pd.DataFrame(list(shark_investment_count.items()), columns=['Shark Name', 'Total Brands Invested'])

# Display the title of the dashboard
st.title('Shark Tank India - Number of Brands Invested by Each Shark')

# Create columns for layout
col1, col2, col3 = st.columns([1, 2, 2])

# Sidebar for filtering sharks
with col1:
    #st.header("Filters")
    # Filter selection for sharks
    filter_shark = st.selectbox("Select Shark Name:", ['All'] + list(shark_investment_count.keys()))

# Display total investment data (number of brands invested)
with col2:
    st.write("Total Number of Brands Invested by Shark: ")

    # Filter data based on selected shark
    if filter_shark != 'All':
        filtered_data = shark_investment_count_df[shark_investment_count_df['Shark Name'] == filter_shark]
        st.dataframe(filtered_data)  # Display filtered data
    else:
        st.dataframe(shark_investment_count_df)  # Display all data

# Plot the bar chart of number of brands invested by each shark
with col3:
    fig = px.bar(shark_investment_count_df,
                 x='Shark Name',
                 y='Total Brands Invested',
                 title="Number of Brands Invested by Each Shark",
                 labels={'Shark Name': 'Shark', 'Total Brands Invested': 'Number of Brands Invested'},
                 color='Shark Name',
                 color_continuous_scale='viridis')
    st.plotly_chart(fig)


#Average Equity 
# Load the dataset
file_path = 'Shark Tank India Dataset.csv' 
data = pd.read_csv(file_path)

# Define the columns related to shark deals and equity
shark_columns = ['ashneer_deal', 'anupam_deal', 'aman_deal', 'namita_deal', 'vineeta_deal', 'peyush_deal', 'ghazal_deal']
equity_column = 'equity_per_shark'

# Calculate Average Equity per Shark
equity_data = {}
for shark in shark_columns:
    shark_equity = data[data[shark] == 1][equity_column]
    equity_data[shark.split('_')[0].capitalize()] = shark_equity.mean()

# Convert dictionary to DataFrame for easy table and plotting
equity_df = pd.DataFrame(list(equity_data.items()), columns=['Shark', 'Average Equity'])

# Display the title and the table in Streamlit
st.subheader("Shark Tank India - Average Equity Data Table")
st.write("Select multiple sharks or use 'All' to view all sharks' data.")

# List of shark names with "All" as the first option
shark_options = ['All'] + equity_df['Shark'].tolist()

# Multi-select box for choosing multiple sharks, with "All" option
selected_sharks = st.multiselect("Select Shark Names:", options=shark_options, default=['All'])

# Check if "All" is selected
if "All" in selected_sharks:
    filtered_df = equity_df  # Show all sharks
else:
    filtered_df = equity_df[equity_df['Shark'].isin(selected_sharks)]  # Filter based on selected sharks

# Display the filtered table
st.write(filtered_df)

# Plot an interactive bar chart for Average Equity
fig_average_equity = px.bar(
    filtered_df,
    x='Shark',
    y='Average Equity',
    title="Average Equity per Shark",
    labels={'Average Equity': 'Average Equity (%)'},
    hover_data={'Average Equity': ':.2f'},
    color_discrete_sequence=['Purple'] 
)

# Display the filtered chart
st.plotly_chart(fig_average_equity)


    

# Top 5 
# Load the dataset
df = pd.read_csv("Shark Tank India Dataset.csv")

# Function to get top 5 brands for a selected shark based on investment
def top_brands_per_shark(shark_column, amount_column):
    shark_investments = df[df[shark_column] > 0][['brand_name', amount_column]]
    top_brands = shark_investments.sort_values(by=amount_column, ascending=False).head(5)
    return top_brands

# Streamlit app with single select for selecting shark
st.title("Top 5 Brands per Shark by Investment Amount")

# Sidebar for selecting a single shark for plotting
st.sidebar.header("Select Shark for Plotting")
shark_selection_for_plot = st.sidebar.selectbox(
    "Select Shark to Plot Investment",
    ["Ashneer", "Anupam", "Aman", "Namita", "Vineeta", "Peyush", "Ghazal"],
    index=0  # Default to Ashneer (index=0)
)

# Mapping of sharks to their respective deal columns in the dataset
sharks = {
    "Ashneer": "ashneer_deal",
    "Anupam": "anupam_deal",
    "Aman": "aman_deal",
    "Namita": "namita_deal",
    "Vineeta": "vineeta_deal",
    "Peyush": "peyush_deal",
    "Ghazal": "ghazal_deal"
}

# Display the top 5 brands for the selected shark
selected_shark_column = sharks[shark_selection_for_plot]
top_brands = top_brands_per_shark(selected_shark_column, 'deal_equity')

# Plotting with Plotly (interactive bar chart)
fig = px.bar(
    top_brands, 
    x='brand_name', 
    y='deal_equity', 
    title=f"Top 5 Brands for {shark_selection_for_plot} by Deal Equity",
    labels={'deal_equity': 'Deal Equity', 'brand_name': 'Brand Name'},
    color='brand_name',  # Different colors for each bar
    hover_data={'deal_equity': True}  # Show deal equity on hover
)

# Customize the layout for better readability
fig.update_layout(
    xaxis_title="Brand Name",
    yaxis_title="Deal Equity",
    xaxis_tickangle=45,  # Rotate x-axis labels
    legend_title="Brand Names",  # Title for the legend
    legend=dict(
        x=1.02,  # Place the legend outside the chart area (to the right)
        y=1,  # Align the legend at the top-right corner
        bgcolor="rgba(255,255,255,0.8)",  # Semi-transparent background for the legend
        bordercolor="Black",
        borderwidth=1
    )
)

# Display the interactive plot in Streamlit
st.plotly_chart(fig)

#Shreyashi graph end -------------------------------------------------------------------------------





