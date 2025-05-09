import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load data with new caching system
@st.cache_data
def load_data():
    day_df = pd.read_csv('data/day.csv')
    hour_df = pd.read_csv('data/hour.csv')

    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
    combined_df = pd.merge(day_df, hour_df, on='dteday', how='outer')

    # Cleaning data
    combined_df = combined_df.drop_duplicates()
    
    # Replacing missing values (e.g., using median for numerical columns and mode for categorical)
    for col in combined_df.select_dtypes(include=[np.number]).columns:
        combined_df[col].fillna(combined_df[col].median(), inplace=True)
    
    for col in combined_df.select_dtypes(include=[object, 'category']).columns:
        combined_df[col].fillna(combined_df[col].mode()[0], inplace=True)

    combined_df['dteday'] = pd.to_datetime(combined_df['dteday'])
    
    # Changing dtype of relevant variables
    combined_df['season_x'] = combined_df['season_x'].astype('category')
    combined_df['weekday_x'] = combined_df['weekday_x'].astype('category')
    
    return combined_df

# Title of the dashboard
st.title('🚲 **Bike Sharing Analysis Dashboard**')

# Brief Introduction to the dataset and its objectives
st.markdown("""
### 📊 **Introduction**
This dashboard provides an analysis of a **Bike Sharing dataset**. It includes daily and hourly rental counts of bikes from a bike-sharing system. Explore the distributions of weather variables, trends over time, and clustering patterns in bike rentals.

### 🔍 **Key Questions**:
1. **How do temperature, humidity, and wind speed affect bike rentals?**
2. **What are the trends in bike rentals over time (daily, weekly)?**

### 📧 **Contact Info**:
- **Name**: mocitaz
- **Email**: [luthfafiwork@gmail.com](mailto:luthfafiwork@gmail.com)
""")

# Load data
combined_df = load_data()

# Sidebar Features for Filtering
st.sidebar.header('Filter Data')

# Date Range filter
start_date = st.sidebar.date_input('Start Date', min_value=combined_df['dteday'].min(), max_value=combined_df['dteday'].max(), value=combined_df['dteday'].min())
end_date = st.sidebar.date_input('End Date', min_value=combined_df['dteday'].min(), max_value=combined_df['dteday'].max(), value=combined_df['dteday'].max())

# Season Filter
season_options = ['All', 'Spring', 'Summer', 'Fall', 'Winter']
season_filter = st.sidebar.selectbox('Select Season', season_options)

# Weather Filter (e.g., clear, cloudy, rainy)
weather_options = ['All', 'Clear', 'Cloudy', 'Rainy']
weather_filter = st.sidebar.selectbox('Select Weather Type', weather_options)

# Filtering data based on selected inputs
filtered_df = combined_df[(combined_df['dteday'] >= pd.to_datetime(start_date)) & (combined_df['dteday'] <= pd.to_datetime(end_date))]

if season_filter != 'All':
    season_dict = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    season_id = season_dict.get(season_filter, 1)
    filtered_df = filtered_df[filtered_df['season_x'] == season_id]

if weather_filter != 'All':
    weather_dict = {1: 'Clear', 2: 'Cloudy', 3: 'Rainy'}
    weather_id = weather_dict.get(weather_filter, 1)
    filtered_df = filtered_df[filtered_df['weathersit_x'] == weather_id]

# Show the filtered data preview
st.sidebar.subheader('Filtered Data Preview')
st.dataframe(filtered_df.head())

# Option to download filtered data as CSV
st.sidebar.subheader('Download Filtered Data')
csv = filtered_df.to_csv(index=False)
st.sidebar.download_button(
    label="Download Data",
    data=csv,
    file_name='filtered_bike_sharing_data.csv',
    mime='text/csv'
)

# Show the filtered data
st.write(f"Showing data from {start_date} to {end_date}, Season: {season_filter}, Weather: {weather_filter}")
st.dataframe(filtered_df)

# Distribution of Variables (Directly shown without filter)
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

# Trends over Time (Directly shown without filter)
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

# Clustering of Bike Rentals (Directly shown without filter)
st.header('📍 Clustering of Bike Rentals')
st.markdown("""
This section demonstrates **K-Means clustering** to identify different groups of bike rentals based on **temperature** and **rental count**. 
The goal is to understand how temperature impacts the frequency of bike rentals.
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
