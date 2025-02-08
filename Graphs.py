import numpy as np
import seaborn as sns

# Create a figure
plt.figure(figsize=(10, 6))

# Fit trend lines for better visualization of patterns
city_fit = np.polyfit(df['Fuel Consumption City (L/100 km)'], df['CO2 Emissions(g/km)'], 1)
hwy_fit = np.polyfit(df['Fuel Consumption Hwy (L/100 km)'], df['CO2 Emissions(g/km)'], 1)
comb_fit = np.polyfit(df['Fuel Consumption Comb (L/100 km)'], df['CO2 Emissions(g/km)'], 1)

# Scatter plots with trend lines
sns.regplot(x=df['Fuel Consumption City (L/100 km)'], y=df['CO2 Emissions(g/km)'], color='red', 
            scatter_kws={'s': 70, 'alpha': 0.5}, line_kws={'label': "City Trend", 'color': 'red'})

sns.regplot(x=df['Fuel Consumption Hwy (L/100 km)'], y=df['CO2 Emissions(g/km)'], color='blue', 
            scatter_kws={'s': 50, 'alpha': 0.5}, line_kws={'label': "Highway Trend", 'color': 'blue'})

sns.regplot(x=df['Fuel Consumption Comb (L/100 km)'], y=df['CO2 Emissions(g/km)'], color='green', 
            scatter_kws={'s': 60, 'alpha': 0.5}, line_kws={'label': "Combined Trend", 'color': 'green'})

# Labels and title
plt.xlabel("Fuel Consumption (L/100 km)")
plt.ylabel("CO2 Emissions (g/km)")
plt.title("City Fuel Consumption Has the Worst CO2 Impact", fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Show the updated visualization with trend lines
plt.show()






# Use color mapping to show CO2 emissions in city driving
plt.figure(figsize=(8, 6))
scatter = plt.scatter(city_fuel, highway_fuel, c=df["CO2 Emissions(g/km)"], cmap='coolwarm', alpha=0.7, edgecolors='black')

# Add a color bar to indicate CO2 emission levels
cbar = plt.colorbar(scatter)
cbar.set_label("CO2 Emissions (g/km)")

# Labels and title
plt.xlabel("City Fuel Consumption (L/100 km)")
plt.ylabel("Highway Fuel Consumption (L/100 km)")
plt.title("City vs. Highway Fuel Consumption (CO2 Emissions Indicated by Color)")
plt.grid(True)

# Show plot
plt.show()



# Create a box plot comparing CO2 emissions for city and highway fuel consumption
plt.figure(figsize=(8, 6))

# Prepare data for boxplot
data = [df["Fuel Consumption City (L/100 km)"], df["Fuel Consumption Hwy (L/100 km)"]]
labels = ["City Fuel Consumption", "Highway Fuel Consumption"]

# Boxplot visualization
plt.boxplot(data, labels=labels, patch_artist=True, boxprops=dict(facecolor="lightblue"), medianprops=dict(color="red"))

# Labels and title
plt.ylabel("Fuel Consumption (L/100 km)")
plt.title("Comparison of Fuel Consumption in City vs. Highway")

plt.grid(True)
plt.show()




# Reload the dataset to include necessary columns
df = pd.read_csv("/mnt/data/CO2 Emissions_Canada.csv")

# Extract relevant columns
df = df[['Make', 'Fuel Consumption Comb (L/100 km)']]

# Aggregate data by car manufacturer (Make) - average fuel consumption
make_avg_fuel = df.groupby('Make')['Fuel Consumption Comb (L/100 km)'].mean()

# Sort values for better visualization
make_avg_fuel = make_avg_fuel.sort_values()

# Plot the results
plt.figure(figsize=(12, 6))
make_avg_fuel.plot(kind='bar', color='purple', edgecolor='black')
plt.xlabel("Car Manufacturer (Make)")
plt.ylabel("Average Fuel Consumption (L/100 km)")
plt.title("Comparison of Car Manufacturer and Fuel Consumption in Canada")
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()




# Extract relevant data for Canada from the Cement Emissions dataset
cement_canada = cement_df[['Year', 'Canada']].dropna()
cement_canada.rename(columns={'Canada': 'Cement CO2 Emissions (Mt)'}, inplace=True)

# Plot Cement CO2 Emissions over time
plt.figure(figsize=(10, 6))
plt.plot(cement_canada['Year'], cement_canada['Cement CO2 Emissions (Mt)'], marker='o', linestyle='-', color='brown', label="Cement CO₂ Emissions")
plt.xlabel("Year")
plt.ylabel("CO₂ Emissions (Million Tonnes)")
plt.title("Cement CO₂ Emissions in Canada Over Time")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()



