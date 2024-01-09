import csv
import re

# prompt user to add ingredients
# store all ingredients
total = []

while True:
    prompt = input("What ingredients do you have? (Press Enter to Exit) ")
    if not prompt:
        break
    total.append(prompt.lower())  # Convert user input to lowercase for case-insensitive matching

# return all possible recipes based on ingredients provided
with open('recipes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        dish_name = row[4].replace("-"," ").title()  # Accessing the first column (index 0) which contains names
        dish_name = re.sub(r'\d+', '', dish_name)
        ingredients = row[1].split(',')  # Split the ingredients string into a list
        matching_ingredients = [ingredient.lower().strip() for ingredient in ingredients if any(word in ingredient.lower().strip() for word in total)]
        if matching_ingredients:
            print(f'Dish: "{dish_name}" possibly available with these ingredient(s): {", ".join(matching_ingredients)}')

