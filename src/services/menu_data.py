from src.models.ingredient import Ingredient
from src.models.dish import Dish
import csv


# Req 3
def get_dishes(path):
    dishes = []

    with open(path, mode="r") as file:
        data = csv.DictReader(file, delimiter=",", quotechar='"')
        list = [e for e in data]
        for dict1 in list:
            dish = {
                "name": dict1["dish"],
                "price": dict1["price"],
                "ingredients": [
                    tuple((dict2["ingredient"], dict2["recipe_amount"]))
                    for dict2 in list if dict1["dish"] == dict2["dish"]
                ]
            }
            if dish not in dishes:
                dishes.append(dish)

    return dishes


class MenuData:
    def __init__(self, source_path: str) -> None:
        dishes = set()

        for dict in get_dishes(source_path):
            dish = Dish(dict["name"], float(dict["price"]))
            for tuple in dict["ingredients"]:
                ingredient = Ingredient(tuple[0])
                dish.add_ingredient_dependency(ingredient, int(tuple[1]))

            dishes.add(dish)

        self.dishes = dishes
