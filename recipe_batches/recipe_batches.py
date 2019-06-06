#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    maximum = -1
    for k, v in recipe.items():
        ingredient = ingredients.get(k)
        if not ingredient:
            maximum = 0
            break
        ing_max = ingredient//v
        if maximum == -1:
            maximum = ing_max
        elif ing_max < maximum:
            maximum = ing_max
    return maximum


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
