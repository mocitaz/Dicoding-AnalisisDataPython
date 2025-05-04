import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load data with caching
@st.cache_data
def load_data():
    day_df = pd.read_csv('data/day.csv')
    hour_df = pd.read_csv('data/hour.csv')

    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
    combined_df = pd.merge(day_df, hour_df, on='dteday', how='outer')

    # Cleaning data
    combined_df = combined_df.drop_duplicates()
    combined_df.fillna(combined_df.mean(), inplace=True)
    combined_df['dteday'] = pd.to_datetime(combined_df['dteday'])
    
    # Changing dtype of relevant variables
    combined_df['season_x'] = combined_df['season_x'].astype('category')
    combined_df['weekday_x'] = combined_df['weekday_x'].astype('category')
    
    return combined_df

# Title of the dashboard
st.title('🚲 **Bike Sharing Analysis Dashboard**')

# Load data
combined_df = load_data()

# Sidebar for selecting analysis type and filtering
st.sidebar.header('Select Analysis Type')
options = st.sidebar.selectbox('Select Analysis', ('Distribution', 'Trends', 'Clustering'))

# Filter options: Date Range, Season, Weather
st.sidebar.header('Filters')

start_date = st.sidebar.date_input('Start Date', min_value=combined_df['dteday'].min(), max_value=combined_df['dteday'].max(), value=combined_df['dteday'].min())
end_date = st.sidebar.date_input('End Date', min_value=combined_df['dteday'].min(), max_value=combined_df['dteday'].max(), value=combined_df['dteday'].max())

season_filter = st.sidebar.selectbox('Season', options=['All', 'Spring', 'Summer', 'Fall', 'Winter'], index=0)

weather_filter = st.sidebar.selectbox('Weather', options=['All', 'Clear', 'Mist', 'Cloudy'], index=0)

# Filter data based on selections
filtered_df = combined_df[
    (combined_df['dteday'] >= pd.to_datetime(start_date)) &
    (combined_df['dteday'] <= pd.to_datetime(end_date))
]

if season_filter != 'All':
    filtered_df = filtered_df[filtered_df['season_x'] == season_filter]

if weather_filter != 'All':
    filtered_df = filtered_df[filtered_df['weathersit_x'] == weather_filter]

# Show the filtered data
st.write(f"Showing data from {start_date} to {end_date}, Season: {season_filter}, Weather: {weather_filter}")
st.dataframe(filtered_df)

# Distribution of Variables
if options == 'Distribution':
    st.header('🌦️ Distribution of Key Variables')
    st.markdown("""
    This section displays the distribution of weather-related variables such as **temperature**, **humidity**, and **windspeed**.
    """)

    # Display distribution of temperature
    st.subheader('🌡️ Temperature Distribution')
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))
    sns.histplot(filtered_df['temp_x'], kde=True, ax=ax[0])
    ax[0].set_title('Temperature Distribution')
    sns.boxplot(x=filtered_df['temp_x'], ax=ax[1])
    ax[1].set_title('Temperature Boxplot')
    st.pyplot(fig)

    # Display distribution of humidity
    st.subheader('💧 Humidity Distribution')
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))
    sns.histplot(filtered_df['hum_x'], kde=True, ax=ax[0])
    ax[0].set_title('Humidity Distribution')
    sns.boxplot(x=filtered_df['hum_x'], ax=ax[1])
    ax[1].set_title('Humidity Boxplot')
    st.pyplot(fig)

    # Display distribution of windspeed
    st.subheader('💨 Windspeed Distribution')
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))
    sns.histplot(filtered_df['windspeed_x'], kde=True, ax=ax[0])
    ax[0].set_title('Windspeed Distribution')
    sns.boxplot(x=filtered_df['windspeed_x'], ax=ax[1])
    ax[1].set_title('Windspeed Boxplot')
    st.pyplot(fig)

# Trends over Time
elif options == 'Trends':
    st.header('📅 Trends of Bike Rentals Over Time')
    st.markdown("""
    Explore how bike rentals vary over time, focusing on **monthly**, **weekly**, and **daily** rental trends.
    """)

    # Monthly trend of bike rentals
    st.subheader('📊 Monthly Trend of Bike Rentals')
    monthly_avg = filtered_df.groupby('mnth_x')['cnt_x'].mean().reset_index()
    sns.lineplot(x='mnth_x', y='cnt_x', data=monthly_avg)
    plt.title('Trends of Bike Rentals per Month')
    plt.xlabel('Month')
    plt.ylabel('Average Rentals')
    st.pyplot(plt)

    # Weekly trend of bike rentals
    st.subheader('📅 Weekly Trend of Bike Rentals')
    daily_avg = filtered_df.groupby('weekday_x')['cnt_x'].mean().reset_index()
    sns.lineplot(x='weekday_x', y='cnt_x', data=daily_avg)
    plt.title('Trends of Bike Rentals per Weekday')
    plt.xlabel('Weekday')
    plt.ylabel('Average Rentals')
    plt.xticks(ticks=range(7), labels=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    st.pyplot(plt)

# Clustering of Bike Rentals
elif options == 'Clustering':
    st.header('📍 Clustering of Bike Rentals')
    st.markdown("""
    This section demonstrates **K-Means clustering** to identify different groups of bike rentals based on **temperature** and **rental count**.
    """)

    # Clustering based on temperature and bike rentals
    st.subheader('📊 Clustering Based on Temperature and Rentals')
    X = filtered_df[['temp_x', 'cnt_x']]
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
    filtered_df['Cluster'] = kmeans.labels_

    # Show the clustering
    sns.scatterplot(x='temp_x', y='cnt_x', hue='Cluster', data=filtered_df, palette='Set1')
    plt.title('Clustering Based on Temperature and Bike Rentals')
    plt.xlabel('Temperature')
    plt.ylabel('Bike Rentals')
    st.pyplot(plt)
