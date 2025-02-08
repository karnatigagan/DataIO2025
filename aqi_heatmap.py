import pandas as pd
import folium
from folium.plugins import HeatMap

# Load your Air Pollution dataset
canada_air_pollution = pd.read_csv("Canada_Air_Pollution_Data.csv")

# Calculate the average AQI for each city
average_aqi_per_city = canada_air_pollution.groupby("City")["AQI Value"].mean().reset_index()

# Predefine latitudes and longitudes for cities
# city_coordinates = {
#     "Toronto": [43.7, -79.42],
#     "Vancouver": [49.28, -123.12],
#     "Montreal": [45.50, -73.57],
#     "Calgary": [51.05, -114.07],
#     "Edmonton": [53.55, -113.49],
#     "Ottawa": [45.42, -75.69],
#     "Winnipeg": [49.90, -97.14],
#     "Quebec City": [46.81, -71.21],
#     "Halifax": [44.65, -63.58],
#     "Saskatoon": [52.13, -106.67]
# }

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
    "Alma": [48.5501, -71.6501],
    "Saint Thomas": [42.7777, -81.1901],
    "Prince George": [53.9171, -122.7497],
    "Powell River": [49.8356, -124.5246],
    "Saint Hyacinthe": [45.6263, -72.9657],
    "Corner Brook": [48.9489, -57.9333],
    "Campbell River": [50.0244, -125.2442],
    "Edmundston": [47.3739, -68.3251],
    "Beloeil": [45.5692, -73.2045],
    "Abbotsford": [49.0546, -122.328],
    "Wetaskiwin": [52.9693, -113.3765],
    "Sarnia": [42.9745, -82.4066],
    "Smiths Falls": [44.9035, -76.0223],
    "Guelph": [43.5448, -80.2482],
    "Fort Saint John": [56.2527, -120.846],
    "Bathurst": [47.6187, -65.6501],
    "Cornwall": [45.0183, -74.7286],
    "Courtenay": [49.6898, -125.0031],
    "Cowansville": [45.2017, -72.7453],
    "Matane": [48.8519, -67.5341],
    "Granby": [45.4001, -72.7333],
    "Leamington": [42.0534, -82.5993],
    "Regina": [50.4452, -104.6189],
    "Amherstburg": [42.1017, -83.1122],
    "Parksville": [49.3196, -124.3163],
    "Canmore": [51.089, -115.359],
    "Salaberry De Valleyfield": [45.2571, -74.1324],
    "Nanticoke": [42.7933, -80.0542],
    "Terrace": [54.5158, -128.6036],
    "Owen Sound": [44.5691, -80.943],
    "Oshawa": [43.8975, -78.8638],
    "Thunder Bay": [48.382, -89.2465],
    "Cobourg": [43.9592, -78.1673],
    "Glace Bay": [46.1973, -59.9567],
    "North Bay": [46.3091, -79.4608],
    "Orangeville": [43.919, -80.0943],
    "Cochrane": [51.1895, -114.467],
    "Belleville": [44.1628, -77.3853],
    "Bay Roberts": [47.599, -53.2644],
    "Prince Albert": [53.2033, -105.7506],
    "Lethbridge": [49.6935, -112.8418],
    "North Battleford": [52.7797, -108.296],
    "Yellowknife": [62.454, -114.3718],
    "Strathroy": [42.9552, -81.6166],
    "White Rock": [49.0262, -122.8026],
    "Aldergrove": [49.058, -122.4703],
    "Moose Jaw": [50.393, -105.5511],
    "Saint John": [45.2733, -66.0633],
    "Sydney Mines": [46.237, -60.2197],
    "Petawawa": [45.8941, -77.2785],
    "Strathmore": [51.0407, -113.4005],
    "Shawinigan": [46.5667, -72.7503],
    "Charlottetown": [46.2382, -63.1311],
    "Sherbrooke": [45.4001, -71.8991],
    "Kitchener": [43.4516, -80.4925],
    "Rimouski": [48.452, -68.5235],
    "Red Deer": [52.2681, -113.8114],
    "Brantford": [43.1394, -80.2644],
    "Yorkton": [51.2139, -102.4627],
    "Camrose": [53.0164, -112.8367],
    "Kelowna": [49.887, -119.496],
    "Sudbury": [46.49, -81.01],
    "Fort Erie": [42.9001, -78.9717],
    "Leduc": [53.268, -113.5502],
    "Midland": [44.7493, -79.892],
    "Wallaceburg": [42.5926, -82.3934],
    "Kenora": [49.763, -94.4893],
    "Kentville": [45.0777, -64.4933],
    "Ingersoll": [43.0383, -80.8835],
    "Quesnel": [52.9784, -122.502],
    "Lloydminster": [53.2784, -110.0016],
    "Tilsonburg": [42.8667, -80.7333],
    "Chilliwack": [49.1579, -121.9515],
    "Saskatoon": [52.1579, -106.6702],
    "Okotoks": [50.725, -113.9754],
    "Medicine Hat": [50.0405, -110.6765],
    "Moncton": [46.132, -64.7722],
    "Edmonton": [53.5461, -113.4938],
    "Winnipeg": [49.8951, -97.1384],
    "Kamloops": [50.6745, -120.3273],
    "Fredericton": [45.9636, -66.6431],
    "Quebec": [46.8139, -71.2082],
    "Peterborough": [44.3091, -78.3197],
    "Calgary": [51.0447, -114.0719]
}

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

# open -a "Google Chrome" canada_aqi_heatmap.html