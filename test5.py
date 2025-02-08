import pandas as pd
import folium
from folium.plugins import HeatMap

# Load your Air Pollution dataset
canada_air_pollution = pd.read_csv("Canada_Air_Pollution_Data.csv")

# Calculate the average AQI for each city
average_aqi_per_city = canada_air_pollution.groupby("City")["AQI Value"].mean().reset_index()

# Predefined city coordinates
city_coordinates = {
    "Toronto": [43.7, -79.42],
    "Vancouver": [49.28, -123.12],
    "Montreal": [45.50, -73.57],
    "Calgary": [51.05, -114.07],
    "Edmonton": [53.55, -113.49],
    "Ottawa": [45.42, -75.69],
    "Winnipeg": [49.90, -97.14],
    "Quebec City": [46.81, -71.21],
    "Halifax": [44.65, -63.58],
    "Saskatoon": [52.13, -106.67],
    "Whitehorse": [60.7212, -135.0568],
    "Kamloops": [50.6745, -120.3273]
}

# Add coordinates to the dataframe
average_aqi_per_city["Latitude"] = average_aqi_per_city["City"].map(lambda x: city_coordinates.get(x, [None, None])[0])
average_aqi_per_city["Longitude"] = average_aqi_per_city["City"].map(lambda x: city_coordinates.get(x, [None, None])[1])

# Remove rows with missing coordinates
average_aqi_per_city = average_aqi_per_city.dropna(subset=["Latitude", "Longitude"])

# Create a base map centered on Canada
canada_map = folium.Map(location=[56.1304, -106.3468], zoom_start=4)

# Prepare heatmap data
heat_data = list(zip(
    average_aqi_per_city["Latitude"],
    average_aqi_per_city["Longitude"],
    average_aqi_per_city["AQI Value"]
))

# Add HeatMap layer
HeatMap(heat_data).add_to(canada_map)

# Load highway data (GeoJSON)
highways_geojson_path = "path_to_highway_data.geojson"  # Replace with actual path
folium.GeoJson(highways_geojson_path, name="Highways", style_function=lambda x: {
    'color': 'blue',
    'weight': 2,
    'opacity': 0.7
}).add_to(canada_map)

# Add layer control
folium.LayerControl().add_to(canada_map)

# Save the heatmap to an HTML file
canada_map.save("canada_aqi_highways_map.html")

print("Heatmap with highways saved as 'canada_aqi_highways_map.html'. Open this file in a web browser to view the map.")