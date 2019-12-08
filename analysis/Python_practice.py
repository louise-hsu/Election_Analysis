print("Hello World")

type(3)
type(2019)
type(73.81)
type(True)
type("True")

1.5+2*3
2.8//5-3

countries = ["Arapahoe", "Denver", "Jefferson"]


counties = ["A", "b", "c"]

counties[2]

counties[1:3]
counties[1:2]
counties[0]
counties[1]
counties[2]


counties.append("El Paso")
counties

counties.insert(2, "El Paso")
counties

counties.remove("El Paso")
counties

range(5)
range(0, 5)
print(range(5))
range(0, 5)


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    
    print(f"{county} country has {voters:,} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]



for county_dict in voting_data:
    print(f"{county_dict['county']} country has {county_dict['registered_voters']:,} registered voters.")


# Import the datetime dependency.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is,", now)

import csv
dir(csv)
dir(int)
dir(float)
dir(bool)
dir(list)
dir(tuple)
dir(dict)
print(dir(datetime))    
