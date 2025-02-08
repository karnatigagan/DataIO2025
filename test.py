import folium
import pandas as pd

# Load the dataset
canada_charging_stations = pd.read_csv("Canada_Charging_Stations.csv", low_memory=False)

# Identify the correct Latitude and Longitude column names
latitude_column = "Latitude"  # Adjust if necessary
longitude_column = "Longitude"  # Adjust if necessary

# Create a map centered around Canada
canada_map = folium.Map(location=[56.1304, -106.3468], zoom_start=4)

# Add charging station markers
for _, row in canada_charging_stations.iterrows():
    if pd.notnull(row[latitude_column]) and pd.notnull(row[longitude_column]):  # Ensure coordinates exist
        folium.Marker(
            location=[row[latitude_column], row[longitude_column]],
            popup=row["Station Name"],
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(canada_map)

# Save the map as an HTML file
canada_map.save("canada_charging_stations_map.html")