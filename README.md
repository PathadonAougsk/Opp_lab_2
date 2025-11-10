Overview
This project is based / Heavy rely on OOP principle.

Psudo Overview..?
-> load csv file
-> extract to dictionary
-> filter / aggregate the data in dictionary

Starting from the top.

Class: DataLoader
This class is all about handling CSV file loading and converting it into a list containing dictionaries.
Each dictionary represents a row of data, making it easier to process programmatically.

Class: Table
This class represents the data table itself.
It contain methods to:
  - Filter(lamda) rows based on a given condition
  - Aggregate(key : str, condtion : lamda) specific columns using custom functions (like average, max, or count).

The idea is to should make it easier to code/edit by following OOP principles such as encapsulation and reusability.
