
# I have used two classes for the recipe manager with the methods underneath.

class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions


class RecipeManager:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        self.save_recipes()
        print(f"\nRecipe '{recipe.name}' added successfully")

    def display_recipe(self, recipe_name):
        recipe = self.find_recipes(recipe_name)
        if recipe:
            print(f"\nRecipe:{recipe.name}")
            print("ingredients:")
            for ingredient in recipe.ingredients:
                print(" - " + ingredient)

            print("instructions:")
            for step, instruction in enumerate(recipe.instructions, 1):
                print(f"{step}.{instruction}")
        else:
            print(f"Recipe '{recipe_name}' not found")

    def search_recipe(self, recipe_name):
        found = False
        for recipe in self.recipes:
            if recipe_name.lower().strip() in recipe.name.lower():
                print(f"\nFound Recipe: '{recipe.name}' ")
                print("ingredients:")
                for ingredient in recipe.ingredients:
                    print("-" + ingredient)

                print("instructions:")
                for step, instruction in enumerate(recipe.instructions, 1):
                    print(f"'{step}','{instruction}'")
                found = True

        if not found:
           print(f"No recipe found for '{recipe_name}'")

    def save_recipes(self):
        import json
        with open("Recipes.json", "w", encoding="utf-8") as file:
            json.dump([r.__dict__ for r in self.recipes], file, ensure_ascii=False, indent=4)

    def edit_recipe(self, recipe_name):
        recipe = self.find_recipes(recipe_name)
        if recipe:
            print(f"\nEdit Recipe:'{recipe_name}'")
            print("A. Edit Name")
            print("B. Edit ingredients")
            print("C. Edit instructions")
            edit_choice = input("What would you like to edit (A-C)").strip().upper()

            if edit_choice == "A":
               new_name = input("Enter new recipe name:")
               recipe.name = new_name.strip()
            elif edit_choice == "B":
                new_ingredients = input("Enter new recipe ingredients(comma-separated):")
                recipe.ingredients = [i.strip() for i in new_ingredients.split(",")]
            elif edit_choice == "C":
                new_instructions = []
                print("Enter new recipe instructions (type 'end' to finish):")
                while True:
                  step = input('>')
                  if step.strip().lower() == "end":
                      break
                  new_instructions.append(step.strip())
                recipe.instructions = new_instructions
            else:
                print("Choice not available")
                return

            self.save_recipes()
            print(f"Recipe '{recipe.name}' edited successfully")

        else:
            print(f"Recipe '{recipe_name}' not found")



    def delete_recipe(self,recipe_name):
        recipe= self.find_recipes(recipe_name)
        if recipe:
            self.recipes.remove(recipe)
            self.save_recipes()
            print(f"Recipe '{recipe.name}' deleted successfully")
        else:
            print(f"Recipe '{recipe_name}' not found")


    def load_recipes(self):
        import json, os
        if os.path.exists("Recipes.json"):
            with open("Recipes.json",'r', encoding="utf-8") as file:
                try:
                    data =json.load(file)
                    self.recipes = [Recipe(d["name"],d["ingredients"],d["instructions"]) for d in data]
                except json.JSONDecodeError:
                 self.recipes=[]

    def find_recipes(self, recipe_name):
        name = recipe_name.lower().strip()
        for recipe in self.recipes:
            if recipe.name.lower().strip() == name:
                return recipe
        return None



# This is the recipe manager.

manager = RecipeManager()
manager.load_recipes()


def add_recipe():
    name = input("Enter recipe name:")
    ingredients = input("Enter ingredients (comma-seperated): ").split(",")
    instructions_list = []
    print("Enter instructions (type 'end' to finish)")
    while True:
        instructions=input('>')
        if instructions.strip().lower() == "end":
            break
        instructions_list.append(instructions.strip())

    recipe = Recipe(name, ingredients, instructions_list)
    manager.add_recipe(recipe)

#These are the functions for the recipe manager

def display_recipe():
    recipe_name = input("Enter recipe name:")
    manager.display_recipe(recipe_name)

def search_recipe():
    recipe_name = input("Enter recipe name:")
    manager.search_recipe(recipe_name)

def edit_recipe():
    recipe_name = input("Edit recipe name:")
    manager.edit_recipe(recipe_name)

def delete_recipe():
    recipe_name=input("Delete Recipe:")
    manager.delete_recipe(recipe_name)

# This is the main menu

while True:
    print("\nRecipe Manager")
    print("1.Add Recipe")
    print("2.Display Recipes")
    print("3.Search Recipe")
    print("4.Edit Recipe")
    print("5.Delete Recipe")
    print("6.Exit")

    choice = input("Enter your Choice 1-6:").strip()
    if choice == "1":
        add_recipe()
    elif choice == "2":
        display_recipe()
    elif choice == "3":
        search_recipe()
    elif choice == "4":
        edit_recipe()
    elif choice == "5":
        delete_recipe()
    elif choice == "6":
        print("End")
        break
    else:
        print("Invalid choice")

# Above is the full code for this Recipe Manager project.
#To use this code follow the instructions in the portal, select the following option you wish to chose, enjoy!