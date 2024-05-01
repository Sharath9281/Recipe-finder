import pandas as pd

def recommend_recipe(ingredients, recipes):
    # Create a list to store recommended recipes
    recommended_recipes = []

    # Iterate through each recipe
    for index, recipe in recipes.iterrows():
        recipe_ingredients = recipe['Ingredients'].lower().split(', ')

        # Check if any ingredient in the recipe is a superset of the given ingredients
        for ingredient in ingredients:
            if any(ingredient.strip().lower() in recipe_ingredient for recipe_ingredient in recipe_ingredients):
                recommended_recipes.append(recipe)
                break

    return recommended_recipes

# Read recipe data from CSV file
recipes = pd.read_csv('Recipes Dataset.csv')

# Get user input for ingredients
print("Enter the ingredients (enter 'done' when finished):")

user_ingredients = []
while True:
    ingredient = input("Ingredient: ")
    if ingredient.lower() == 'done':
        break
    user_ingredients.append(ingredient)

recommendations = recommend_recipe(user_ingredients, recipes)

if recommendations:
    print("Recommended Recipes:")
    for index, recipe in enumerate(recommendations):
        print(f"{index+1}. {recipe['Title']}")

    recipe_choice = int(input("Enter the number of the recipe to view its instructions: "))

    print("\nNote that the recipies may contain ingredients other than you entered\n")

if 1 <= recipe_choice <= len(recommendations):
        chosen_recipe = recommendations[recipe_choice - 1]
        instruction = chosen_recipe['Instructions']
        print(f"\nInstruction for {chosen_recipe['Title']}:\n")

        # Print instructions without breaking words
        line_length = 180
        words = instruction.split()
        current_line = ""
        for word in words:
            if len(current_line + word) <= line_length:
                current_line += word + " "
            else:
                print(current_line)
                current_line = word + " "
        if current_line:
            print(current_line)
        else:
          print("Invalid recipe choice.")
else:
  print("No recipes found for the given ingredients.")