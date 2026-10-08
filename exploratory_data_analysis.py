import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv(r"C:\Users\adars\OneDrive\Desktop\SWYNEX-Exploratory-Data-Analysis\india_aqi_cleaned.csv")
print(df)

# 2. Basic info about the data
print(df.head())
print(df.shape)
print(list(df.columns))
print(df.isnull().sum())
print("Duplicate values: ", df.duplicated().sum())

# 3. Basic statistics
print(df.describe())

# Average AQI for each city
avg_aqi_city = df.groupby("City")["AQI"].mean().sort_values(ascending=False)
print("\nAverage AQI by City:")
print(avg_aqi_city)

# How many days fall in each AQI category
print("\nAQI Bucket counts:")
print(df["AQI_Bucket"].value_counts())

# Correlation between AQI and other pollutants
print("\nCorrelation with AQI:")
print(df.corr(numeric_only=True)["AQI"].sort_values(ascending=False))

# Simple anomaly check - find days with unusually high or low AQI
# (using mean and standard deviation)
mean_aqi = df["AQI"].mean()
std_aqi = df["AQI"].std()
upper_limit = mean_aqi + 2 * std_aqi
lower_limit = mean_aqi - 2 * std_aqi

anomalies = df[(df["AQI"] > upper_limit) | (df["AQI"] < lower_limit)]

print(f"\nNormal AQI range (mean +/- 2*std): {lower_limit:.1f} to {upper_limit:.1f}")
print(f"Number of anomaly days found: {len(anomalies)}")
if len(anomalies) > 0:
    print(anomalies[["City", "Date", "AQI", "AQI_Bucket"]])
else:
    print("No extreme anomalies found. AQI values stay within a normal range, even though many days are 'Severe'.")

# 4. Charts
# Chart 1: Bar chart - Average AQI per city
plt.figure(figsize=(8, 5))
avg_aqi_city.plot(kind="bar", color="orange")
plt.title("Average AQI by City")
plt.xlabel("City")
plt.ylabel("Average AQI")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("chart1_avg_aqi_by_city.png")


# Chart 2: Pie chart - AQI category distribution
plt.figure(figsize=(6, 6))
df["AQI_Bucket"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("AQI Category Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("chart2_aqi_category_pie.png")


# Chart 3: Scatter plot - PM2.5 vs AQI
plt.figure(figsize=(7, 5))
plt.scatter(df["PM2.5"], df["AQI"], color="green")
plt.title("PM2.5 vs AQI")
plt.xlabel("PM2.5")
plt.ylabel("AQI")
plt.tight_layout()
plt.savefig("chart3_pm25_vs_aqi.png")


# Chart 4: Histogram - AQI distribution
plt.figure(figsize=(7, 5))
df["AQI"].plot(kind="hist", bins=10, color="skyblue", edgecolor="black")
plt.title("Distribution of AQI Values")
plt.xlabel("AQI")
plt.tight_layout()
plt.savefig("chart4_aqi_histogram.png")


# Chart 5: Line chart - AQI trend over time
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df_sorted = df.sort_values("Date")
plt.figure(figsize=(9, 5))
plt.plot(df_sorted["Date"], df_sorted["AQI"], marker="o", linestyle="-", color="red")
plt.title("AQI Trend Over Time")
plt.xlabel("Date")
plt.ylabel("AQI")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("chart5_aqi_trend.png")

plt.show()

print("\nAll charts saved as PNG files.")

# 5. Insights

print("\n----- KEY INSIGHTS -----")
print(f"1. {avg_aqi_city.idxmax()} has the highest average AQI, meaning it has the worst air quality among the cities in this data.")
print(f"2. {avg_aqi_city.idxmin()} has the lowest average AQI, meaning it has the cleanest air among the cities in this data.")
print("3. Most of the days in the data fall under the 'Severe' AQI category, showing that poor air quality is very common.")
print("4. PM2.5 has the strongest correlation with AQI, meaning it is the main pollutant affecting the AQI value.")
print("5. AQI values go up and down a lot over time, showing that pollution levels change daily rather than staying steady.")