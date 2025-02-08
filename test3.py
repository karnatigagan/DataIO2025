import pandas as pd
import folium
from folium.plugins import HeatMap
from geopy.geocoders import Nominatim
import time

# Load your Air Pollution dataset
canada_air_pollution = pd.read_csv("Canada_Air_Pollution_Data.csv")

# Calculate the average AQI for each city
average_aqi_per_city = canada_air_pollution.groupby("City")["AQI Value"].mean().reset_index()

# Initialize geolocator
geolocator = Nominatim(user_agent="geoapiExercises")

# Dictionary to store city coordinates
city_coordinates = {}

# Loop through each city and get its coordinates
for city in average_aqi_per_city["City"].unique():
    try:
        location = geolocator.geocode(city + ", Canada")
        if location:
            city_coordinates[city] = [location.latitude, location.longitude]
        else:
            city_coordinates[city] = [None, None]
        time.sleep(1)  # Prevent API rate limits
    except Exception as e:
        city_coordinates[city] = [None, None]

# Add coordinates to the dataframe
average_aqi_per_city["Latitude"] = average_aqi_per_city["City"].map(lambda x: city_coordinates.get(x, [None, None])[0])
average_aqi_per_city["Longitude"] = average_aqi_per_city["City"].map(lambda x: city_coordinates.get(x, [None, None])[1])

# Remove rows with missing coordinates
average_aqi_per_city = average_aqi_per_city.dropna(subset=["Latitude", "Longitude"])

# Create a base map centered on Canada
canada_map = folium.Map(location=[56.1304, -106.3468], zoom_start=4)

# Prepare heatmap data (latitude, longitude, AQI Value)
heat_data = list(zip(
    average_aqi_per_city["Latitude"],
    average_aqi_per_city["Longitude"],
    average_aqi_per_city["AQI Value"]
))

# Add HeatMap layer
HeatMap(heat_data).add_to(canada_map)

# Save the heatmap to an HTML file
canada_map.save("canada_aqi_heatmap.html")

print("Heatmap saved as 'canada_aqi_heatmap.html'. Open this file in a web browser to view the heatmap.")