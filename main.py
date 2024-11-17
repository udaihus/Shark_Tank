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
selected_shark = st.sidebar.selectbox("Select a shark for Scorecard", shark_names)

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
# Highest amount invested - scorecard

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
# --------------------------------------------------------------------------------------------------------
# Calculate the average equity for the selected shark or all sharks

equity_column = 'equity_per_shark'
if selected_shark == 'ALL':
    # For all sharks, calculate the average equity where shark_deal == 1
    average_equity = (df[names].multiply(df[equity_column], axis=0) * df[names].eq(1)).sum(axis=0)
    total_deals = (df[names] == 1).sum(axis=0)
    average_equity_all = (average_equity / total_deals).round(2)
    he = "Average Equity by All Sharks"
    avg_equity = round(average_equity_all.mean(), 2)  # Calculate overall average for all sharks
else:
    selected_shark_col = f"{selected_shark.lower()}_deal"
    shark_deals = df[df[selected_shark_col] == 1]
    
    # Calculate the average equity for the selected shark
    avg_equity = round(shark_deals[equity_column].mean(), 2)
    he = f"Average Equity by - {selected_shark}"

# Create a scorecard box for displaying the result
scorecard_hd = f"""
<div style="background-color: #f0f4f8; padding: 10px 10px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); width: 170px; margin-top: 10px; margin-right: 5px; border: 3px solid yellow;">
    <h2 style="color: #333; text-align: left; font-size: 14px; font-weight: bold; margin-bottom: 5px;">{he}</h2>
    <h1 style="color: #4CAF50; text-align: left; font-size: 20px; font-weight: bold; margin-top: 5px;">{avg_equity}%</h1>
</div>
"""
#-------------------------------------------------------------------------------------------------------------------

# Calculate the average deal amount invested by sharks
if selected_shark == 'ALL':
    # Filter deals where any shark has invested (sum(axis=1) > 0 means any shark has invested in the deal)
    total_i = df[df[names].sum(axis=1) > 0]['deal_amount'].sum()
    total_deals = df[df[names].sum(axis=1) > 0].shape[0]  # Count of deals where any shark has invested
    avg_deal_amount = total_i / total_deals if total_deals > 0 else 0
    head_dealll = "Average Deal Amount by All Sharks"
else:
    selected_shark_col = f"{selected_shark.lower()}_deal"
    # Filter the deals where the selected shark has invested
    shark_deals = df[df[selected_shark_col] == 1]
    total_i = shark_deals['deal_amount'].sum()
    total_deals = shark_deals.shape[0]  # Number of deals by the selected shark
    avg_deal_amount = total_i / total_deals if total_deals > 0 else 0
    head_dealll = f"Average Deal Amount by {selected_shark}"

# Create a scorecard box to display the average deal amount
scorecard_hhht = f"""
<div style="background-color: #f0f4f8; padding: 10px 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); width: 200px; margin-top: 10px; margin-right: 5px; border: 3px solid yellow;">
    <h2 style="color: #333; text-align: left; font-size: 14px; font-weight: bold; margin-bottom: 5px;">{head_dealll}</h2>
    <h1 style="color: #4CAF50; text-align: left; font-size: 20px; font-weight: bold; margin-top: 5px;">{round(avg_deal_amount, 2)} Lakhs</h1>
</div>
"""

#------------------------------------------------------------------------------------------------------------------------------
# Display the scorecard box
col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])

with col1:
    st.markdown(scorecard_html, unsafe_allow_html=True)

with col2:
    st.markdown(scorecard_h, unsafe_allow_html=True)

with col3:
    st.markdown(scorecard_ht, unsafe_allow_html=True)

with col4:
    st.markdown(scorecard_hd, unsafe_allow_html=True)

with col5:
    st.markdown(scorecard_hhht, unsafe_allow_html=True)

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

st.markdown(
    "<h3 style='text-align: center; color: #4CAF50;'>Shark Tank India - Total Investment & Deal by Each Shark (in Crs)</h3>",
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
# Nissi Grace


df['metric'] = (df['deal_amount'] * df['deal_equity']) / (df['total_sharks_invested']*100)
def top_brands_per_shark(shark_column, amount_column): 
    shark_investments = df[df[shark_column] > 0][['brand_name', 'metric']] 
    top_brands = shark_investments.sort_values(by='metric', ascending=False).head(5)
    return top_brands 

shark_selection = st.sidebar.selectbox(
    "Select a Shark for individual Visualization", 
    ["Ashneer", "Anupam", "Aman", "Namita", "Vineeta", "Peyush", "Ghazal"], 
    index=0  # Default to Ashneer
)

# Shark-deal mapping
sharks = {
    "Ashneer": "ashneer_deal",
    "Anupam": "anupam_deal",
    "Aman": "aman_deal",
    "Namita": "namita_deal",
    "Vineeta": "vineeta_deal",
    "Peyush": "peyush_deal",
    "Ghazal": "ghazal_deal"
}

# Get the selected shark's column
selected_shark_column = sharks[shark_selection]

# Filter data for the selected shark's deals
shark_deals = df[df[selected_shark_column] > 0]

# --- Visualization 1: Line Plot ---
st.markdown(f"<h3 style='text-align: center;color: #4CAF50;'>Equity Comparison for {shark_selection} based on different Brands</h3>", unsafe_allow_html=True)

if not shark_deals.empty:
    line_fig = px.line(
        shark_deals, 
        x="brand_name", 
        y=["ask_equity", "equity_per_shark", "deal_equity"], 
        #title=f"Equity Metrics for {shark_selection}",
        labels={"value": "Equity (%)", "variable": "Equity Type"},
        markers=True,  # Add markers for each point
        color_discrete_map={
            "ask_equity": "red",
            "equity_per_shark": "blue",
            "deal_equity": "green"
        }
    )
    line_fig.update_layout(
        xaxis_title="Brand Name",
        yaxis_title="Equity (%)",
        xaxis_tickangle=90  # Rotate x-axis labels
    )
    st.plotly_chart(line_fig, use_container_width=True) 
#-----------------------------------------------------------------------------------------------------
# nissi  and shreyashi
# --- Visualization 2: Bar Graph ---
st.markdown(f"<h3 style='text-align: center;color: #4CAF50;'>Top 5 Brands for {shark_selection} by Value of Equity</h3>", unsafe_allow_html=True)

top_brands = top_brands_per_shark(selected_shark_column, "metric")

if not top_brands.empty:
    bar_fig = px.bar(
        top_brands,
        x="brand_name",
        y="metric",  # Changed to use the new metric
        #title=f"Top 5 Brands for {shark_selection} by Value of equity",
        labels={"metric": "Ownership Value", "brand_name": "Brand Name"},
        color="brand_name",  # Different colors for each bar
        hover_data={"metric": True}  # Show metric on hover
    )
    bar_fig.update_layout(
        xaxis_title="Brand Name",
        yaxis_title="Ownership Value",  # Changed to reflect the new metric
        xaxis_tickangle=45,  # Rotate x-axis labels
        legend_title="Brand Names",
        bargap=0.4,
        legend=dict(
            x=1.02,  # Place the legend outside the chart area
            y=1,
            bgcolor="rgba(255,255,255,0.8)",  # Semi-transparent legend background
            bordercolor="Black",
            borderwidth=1
        )
    )
    st.plotly_chart(bar_fig, use_container_width=True) 
else:
    st.warning(f"No top brands found for {shark_selection}.")

#----------------------------------------------------------------------------------------------------
#Nissi Grace

# Function to calculate shark participation and deal frequencies
def shark_participation_and_deal_counts():
    # Mapping of sharks to their respective presence and deal columns
    sharks = {
        "Ashneer": ["ashneer_present", "ashneer_deal"],
        "Anupam": ["anupam_present", "anupam_deal"],
        "Aman": ["aman_present", "aman_deal"],
        "Namita": ["namita_present", "namita_deal"],
        "Vineeta": ["vineeta_present", "vineeta_deal"],
        "Peyush": ["peyush_present", "peyush_deal"],
        "Ghazal": ["ghazal_deal"]  # Ghazal only has a 'deal' column
    }
    
    # Dictionaries to store counts for participation and deal
    participation_counts = {shark: 0 for shark in sharks}
    deal_counts = {shark: 0 for shark in sharks}
    
    # Iterate through each row to count participation and deal presence
    for _, row in df.iterrows():
        for shark, columns in sharks.items():
            # Count participation (if presence column exists and is 1)
            if len(columns) > 1 and row[columns[0]] == 1:  # Check if presence column exists
                participation_counts[shark] += 1
            # Count deals (always check if deal column exists)
            if row[columns[-1]] == 1:  # Use the last column in the list, which is always a deal column
                deal_counts[shark] += 1
    
    return participation_counts, deal_counts

# Get the participation and deal counts for each shark
participation_counts, deal_counts = shark_participation_and_deal_counts()

# Create columns for displaying the pie chart and the table side by side
col1, col2 = st.columns(2)

# In the first column, display the pie chart for shark deal participation distribution
with col1:
    total_deals = sum(deal_counts.values())  # Total deals across all sharks
    st.subheader("Shark Deals Across All Pitches")
    
    # Calculate the percentage of deals for each shark
    deal_percentages = {shark: count / total_deals * 100 for shark, count in deal_counts.items()}
    
    fig, ax = plt.subplots(figsize=(5, 5))  # Smaller pie chart
    wedges, texts, autotexts = ax.pie(deal_percentages.values(), labels=deal_percentages.keys(),
                                      autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set2", len(deal_percentages)))
    ax.set_title(f"Shark Deal Percentage\nTotal Deals: {total_deals}")
    
    # Add legend for the deal chart
    ax.legend(wedges, deal_percentages.keys(), title="Sharks", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    st.pyplot(fig)

# In the second column, display the shark participation and deal summary table
with col2:
    # Create a DataFrame to summarize participation and deals
    sharks_summary = pd.DataFrame({
        'Shark': list(participation_counts.keys()),
        'Total Presence (Pitches)': list(participation_counts.values()),
        'Total Deals': list(deal_counts.values())
    })

    # Display the table with background color gradient for better readability
    st.subheader("Shark Participation and Deal Summary")
    st.dataframe(sharks_summary.style.background_gradient(cmap='Blues', axis=0), use_container_width=True)# Neetu Kumari:
# Episode wise deal amount and count of deal # Line plot

#-----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#shreyshi code

# List of shark columns (each representing a shark's deal)
st.markdown(
    "<h3 style='text-align: center; color: #4CAF50;'>Average Equity Per Shark</h3>",
    unsafe_allow_html=True
)

shark_columns = ['ashneer_deal', 'anupam_deal', 'aman_deal', 'namita_deal', 'vineeta_deal', 'peyush_deal', 'ghazal_deal']
equity_column = 'equity_per_shark'

# Calculate Total and Average Equity per Shark
equity_data = {}
for shark in shark_columns:
    # Get the equity for the shark where their deal is 1 (participated in the deal)
    shark_equity = df[df[shark] == 1][equity_column]
    
    # Store the total and average equity for the shark
    equity_data[shark.split('_')[0].capitalize()] = {
        'Total Equity': shark_equity.sum(),
        'Average Equity': shark_equity.mean()
    }

# Convert dictionary to DataFrame for easy table and plotting
equity_df = pd.DataFrame(equity_data).T.reset_index()
equity_df.columns = ['Shark', 'Total Equity', 'Average Equity']


# Plot an interactive bar chart for Average Equity with a different single color
fig_average_equity = px.bar(
    equity_df,
    x='Shark',
    y='Average Equity',
    #title="Average Equity per Shark",
    labels={'Average Equity': 'Average Equity (%)'},
    hover_data={'Average Equity': ':.2f'},
    color_discrete_sequence=['Orange'] 
)

# Display the total equity chart

# Display the average equity chart
st.plotly_chart(fig_average_equity)


#------------------------------------------------------------------------------------------------------------
# Neetu Kumari's Code:

# Centered Title with better styling
st.markdown(
    "<h3 style='text-align: center; color: #4CAF50; font-weight: bold; font-family: Arial, sans-serif;'>Episode-wise Analysis</h3>",
    unsafe_allow_html=True
)

# Grouping the data by episode_number to get the summary
summary = df[df['deal'] == 1].groupby('episode_number').agg(
    total_deal_amount=('deal_amount', 'sum'),
    deal_count=('deal', 'count')
).reset_index()

# Round the 'total_deal_amount' column to the nearest integer
summary['total_deal_amount'] = summary['total_deal_amount'].round(0).astype(int)

# Creating columns for layout
col9, col10 = st.columns([2, 4])

# Displaying the DataFrame with styled background gradient and enhanced formatting
with col9:
    st.dataframe(
        summary.style
        .background_gradient(cmap='Blues', axis=0)  # Color gradient for background
        #.highlight_max(axis=0, color='light green')      # Highlight the maximum value in each column
        .set_table_styles([                        # Adding table styling
            {'selector': 'thead th', 'props': [('background-color', '#4CAF50'), ('color', 'white')]},
            {'selector': 'tbody td', 'props': [('padding', '10px'), ('border', '1px solid #ddd')]},
            {'selector': 'thead', 'props': [('font-weight', 'bold'), ('font-size', '14px')]}
        ]), 
        use_container_width=True
    )

# Plot (if you still want to display the plot)
with col10:
    st.line_chart(summary.set_index('episode_number')[['total_deal_amount', 'deal_count']])

