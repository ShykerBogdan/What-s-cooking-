import json
from pprint import pprint
import numpy as np


def get_data_x(path):
    data = readFromTo(path)
    ingredients_dict = parseIngredients(path)
    data_x_ind = [np.array([ingredients_dict[ingredient]
                            for ingredient in recipe['ingredients']]) for recipe in data]
    data_x = np.zeros((len(data_x_ind), len(ingredients_dict.keys())))
    for i, x in enumerate(data_x_ind):
        data_x[i, x] = 1
    return data_x


def get_data_y(path):
    data = readFromTo(path)
    countries_dict = parseCountries(path)
    data_y_ind = np.array([countries_dict[recipe['cuisine']]
                           for recipe in data])
    data_y = np.zeros((len(data_y_ind), len(countries_dict.keys())))
    for i, x in enumerate(data_y_ind):
        data_y[i, x] = 1
    return data_y


def parseIngredientsCount(path):
    data = readFromTo(path)
    ingredients_dict = dict()
    for recipe in data:
        for ingredient in recipe['ingredients']:
            if ingredient in ingredients_dict:
                ingredients_dict[ingredient] += 1
            else:
                ingredients_dict[ingredient] = 1
    return ingredients_dict


def parseIngredients(path):
    data = readFromTo(path)
    ingredients_set = set()
    [[ingredients_set.add(ingredient)
      for ingredient in recipe['ingredients']] for recipe in data]
    ingredients_dict = dict(zip(ingredients_set, range(len(ingredients_set))))
    return ingredients_dict


def parseCountries(path):
    data = readFromTo(path)
    countries_set = set()
    [countries_set.add(recipe['cuisine']) for recipe in data]
    countries_dict = dict(zip(countries_set, range(len(countries_set))))
    return countries_dict


def parseTestIngredients(path):
    data = readFromTo(path)
    ingredients_set = set()
    [[ingredients_set.add(ingredient)
        for ingredient in recipe['ingredients']] for recipe in data]
    ingredients_dict = dict(zip(ingredients_set, range(len(ingredients_set))))
    return ingredients_dict

def saveNpy(numpyArray, name):
    np.save(name, numpyArray)


def writeTo(path, info):
    with open(path, 'w') as file:
        file.write(json.dumps(info))


def readFromTo(path):
    with open(path) as f:
        return json.load(f)


# # train data
# writeTo("Ingredients.txt", parseIngredients('DataSet//train.json'))
# writeTo("Cuisines.txt", parseCountries('DataSet//train.json'))
# writeTo('IngredientsCount.txt', parseIngredientsCount('DataSet//train.json'))

# saveNpy(get_data_y('DataSet//train.json'),'data_y.npy')
# saveNpy(get_data_x('DataSet//train.json'),'data_x.npy')


# test data
writeTo("IngredientsTest.txt", parseIngredients('DataSet//test.json'))
saveNpy(get_data_x('DataSet//test.json'),'test_data_x.npy')
