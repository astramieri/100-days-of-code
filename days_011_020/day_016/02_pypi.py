# PyPI Python Package Index
# https://pypi.org/

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"], "l")
table.add_column("Type", ["Eletric", "Water", "Fire"], "l")

table.align = "r"

print(table)