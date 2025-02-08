import folium

# Create a map centered around Canada
canada_map = folium.Map(location=[56.1304, -106.3468], zoom_start=4)

# Add charging station markers
for _, row in df_canada_new.iterrows():
    folium.Marker(
        location=[row[latitude_column], row[longitude_column]],
        popup=row["Station Name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(canada_map)

# Display the map
canada_map