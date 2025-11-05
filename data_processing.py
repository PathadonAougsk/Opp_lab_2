import csv, os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, "Cities.csv")) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city["temperature"]))
print(sum(temps) / len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city["temperature"]) for city in cities]
print(sum(temps) / len(temps))
print()

# Print all cities in Germany
print("All cities in Germany:")
citiesInGermany = [city["city"] for city in cities if city["country"] == "Germany"]
print("\n-".join(citiesInGermany))
print()

# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temp above 12°C")
citiesInSpain = [city for city in cities if city["country"] == "Spain"]
aboveCertainTemp = [
    city["city"] for city in citiesInSpain if float(city["temperature"]) > 12
]
print("\n-".join(aboveCertainTemp))
print()

# Count the number of unique countries
uniqueCountries = set([city["country"] for city in cities])
print(f"Amount of unique countries : {len(uniqueCountries)}")
print()

# Print the average temperature for all the cities in Germany
citiesInGermany = [city for city in cities if city["country"] == "Germany"]
germanyCitiesTemp = [float(city["temperature"]) for city in citiesInGermany]
print(
    f"Average temperature for all the cities in Germany is : {sum(germanyCitiesTemp) / len(germanyCitiesTemp):.2f}"
)

# Print the max temperature for all the cities in Italy
maxTempOfItaly = [
    float(city["temperature"]) for city in cities if city["country"] == "Italy"
]
print(f"max temperature for all the cities in Italy is : {max(maxTempOfItaly):.2f}")
