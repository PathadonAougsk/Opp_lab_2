import csv
from pathlib import Path
from types import LambdaType


class DataLoader:
    """Handles loading CSV data files."""

    def __init__(self, base_path=None):
        """Initialize the DataLoader with a base path for data files."""
        if base_path is None:
            self.base_path = Path(__file__).parent.resolve()
        else:
            self.base_path = Path(base_path)

    def load_csv(self, filename):
        """Load a CSV file and return its contents as a list of dictionaries."""
        filepath = self.base_path / filename
        data = []

        with filepath.open() as f:
            rows = csv.DictReader(f)
            for row in rows:
                data.append(dict(row))

        return data


class DB:
    def __init__(self) -> None:
        self.__dictOfTable = {}

    def insert(self, appendTable) -> None:
        name = appendTable.table_name
        self.__dictOfTable[name] = appendTable

    def search(self, userKey: str):
        if not self.__dictOfTable[userKey]:
            return None

        return self.__dictOfTable[userKey]


class Table:
    def __init__(self, name, dict) -> None:
        self.table_name = name
        self.table = dict

    def __str__(self):
        return self.table_name + ":" + str(self.table)

    def join(self, initTable, tableKey: str):
        tmp = []
        for rowInit in initTable.table:
            for rowSelf in self.table:
                if rowSelf["country"] == rowInit["country"]:
                    tmp.append(rowSelf | rowInit)

        tmp = sorted(tmp, key=lambda dict: dict["city"])
        return Table(tableKey, tmp)

    def filter(self, condition: LambdaType) -> list | None:
        temp = []

        for item in self.table:
            if condition(item):
                temp.append(item)

        return Table(self.table_name, temp)

    def aggregate(
        self,
        condition: LambdaType,
        key: str,
    ):
        if key not in ["city", "country", "EU", "coastline"]:
            temp = [float(x[key]) for x in self.table]
        else:
            temp = [x[key] for x in self.table]

        return condition(temp)


loader = DataLoader()
cities = loader.load_csv("Cities.csv")
table1 = Table("cities_filtered", cities)
countries = loader.load_csv("Countries.csv")
table2 = Table("countries_filtered", countries)

my_DB = DB()
my_DB.insert(table1)
my_DB.insert(table2)

my_table1 = my_DB.search("cities_filtered")
print("List all cities in Italy:")
my_table1_filtered = my_table1.filter(lambda x: x["country"] == "Italy")
print(my_table1_filtered)
print()

print("Average temperature for all cities in Italy:")
print(my_table1_filtered.aggregate(lambda x: sum(x) / len(x), "temperature"))
print()

my_table2 = my_DB.search("countries_filtered")
print("List all non-EU countries:")
my_table2_filtered = my_table2.filter(lambda x: x["EU"] == "no")
print(my_table2_filtered)
print()

print("Number of countries that have coastline:")
print(
    my_table2.filter(lambda x: x["coastline"] == "yes").aggregate(
        lambda x: len(x), "coastline"
    )
)
print()

my_table3 = my_table1.join(my_table2, "country")
print("First 5 entries of the joined table (cities and countries):")
for item in my_table3.table[:5]:
    print(item)
print()

print("Cities whose temperatures are below 5.0 in non-EU countries:")
my_table3_filtered = my_table3.filter(lambda x: x["EU"] == "no").filter(
    lambda x: float(x["temperature"]) < 5.0
)
print(my_table3_filtered.table)
print()

print(
    "The min and max temperatures for cities in EU countries that do not have coastlines"
)
my_table3_filtered = my_table3.filter(lambda x: x["EU"] == "yes").filter(
    lambda x: x["coastline"] == "no"
)
print("Min temp:", my_table3_filtered.aggregate(lambda x: min(x), "temperature"))
print("Max temp:", my_table3_filtered.aggregate(lambda x: max(x), "temperature"))
