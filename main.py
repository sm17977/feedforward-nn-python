import numpy as np
import pandas
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
pandas.set_option('display.max_columns', None)


# Read in dataset
path = 'pp-2021.csv'
data = pandas.read_csv(path, sep=',', skiprows=1)

# Pre-processing
# Remove duplicates, columns and rows we are not using

data = data.drop(data.columns[[0, 2, 7, 8, 9, 10, 12, 14, 15]], axis=1)
data.columns = ["Price", "Postcode", "PropertyType", "OldNew", "Duration", "City", "County"]
print("Initial Data Shape: ", data.shape)


data = data[~data["PropertyType"].isin(["F", "O"])]
print("Data Shape after removing rows with PropertyType O and F", data.shape)

# Property Type: D = Detached, S = Semi-Detached, T = Terraced, F = Flats/Maisonettes, O = Other
# Old/New: Y = a newly built property, N = an established residential building
# Duration - Relates to the tenure: F = Freehold, L= Leasehold etc.

#print(len(data.City.unique()))

city_stats = data.groupby('City')['City'].agg('count').sort_values(ascending=False)
#print(city_stats)



city_stats_less_than_1000 = city_stats[city_stats <= 600]

data["City"] = data["City"].apply(lambda x: 'Other' if x in city_stats_less_than_1000 else x)

city_stats = data.groupby('City')['City'].agg('count').sort_values(ascending=False)
#print(city_stats)

print(data.Price.describe())

data = data[data["Price"] > 40000]
data = data[data["Price"] < 5000000]


print(data.Price.describe())

price_data = data["Price"]
ax = price_data.plot.kde()
ax.set_xticks(20)
ax.set_yticks(20)

plt.show()