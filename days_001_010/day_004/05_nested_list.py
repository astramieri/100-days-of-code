dirty_fruits = "Strawberries,Peaches,Pears,Nectarines,Apples,Grapes,Cherries,Blueberries"
dirty_vegetables = "Spinach,Kale,Peppers,Green Beans"

fruits_list = dirty_fruits.split(",")
vegetables_list = dirty_vegetables.split(",")

dirty_dozen = [fruits_list, vegetables_list] ## nested list

print(dirty_dozen)