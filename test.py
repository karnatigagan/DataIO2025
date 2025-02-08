import pandas as pd

# Load your Air Pollution dataset
canada_air_pollution = pd.read_csv("Canada_Air_Pollution_Data.csv")

# Calculate the average AQI for each city
average_aqi_per_city = canada_air_pollution.groupby("City")["AQI Value"].mean().reset_index()

# Predefine latitudes and longitudes for cities (you can use a dictionary or geocoding)
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
    "Saskatoon": [52.13, -106.67]
}

# Add coordinates to the dataframe
average_aqi_per_city["Latitude"] = average_aqi_per_city["City"].map(lambda x: city_coordinates.get(x, [None, None])[0])
average_aqi_per_city["Longitude"] = average_aqi_per_city["City"].map(lambda x: city_coordinates.get(x, [None, None])[1])