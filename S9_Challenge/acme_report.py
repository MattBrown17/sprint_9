"""This module contains functions related to the ACME Corporation
classes: Product

Attributes
----------
ADJECTIVES : list : str
    list of len = 5 containing strings of varying length
    used to provide descriptions to the Products generated

NOUNS : list : str
    list of len = 5 containing strings of varying length
    used to provide base name to the Products generated
"""

import random
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """Constructs num_products worth of Product class in a list

    Parameters
    ----------
    num_products : int
        length of the generated list

    Returns
    -------
    product_list : Product
        len(product_list) = num_products
    """
    product_list = []

    for _ in range(num_products):
        name = str(random.choice(ADJECTIVES)) + " " + str(random.choice(NOUNS))
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)
        product = Product(name, price, weight, flammability)
        product_list.append(product)

    return product_list


def inventory_report(product_list):
    """Given a list of Products gives basic information

    Parameters
    ----------
    product_list : list : Product
        size mutable

    Returns
    -------
    info : tuple
        num_unique : number of unique names in product_list
        mean_price : mean of price attribute
        mean_weight : mean of weight attribute
        mean_flam : mean of flammability attribute
    """
    name_list = set()
    sum_price = 0
    sum_weight = 0
    sum_flam = 0

    for product in product_list:
        name_list.add(product.name)
        sum_price += product.price
        sum_weight += product.weight
        sum_flam += product.flammability

    num_unique = len(name_list)
    mean_price = sum_price / len(product_list)
    mean_weight = sum_weight / len(product_list)
    mean_flam = sum_flam / len(product_list)

    return num_unique, mean_price, mean_weight, mean_flam


if __name__ == '__main__':
    print(inventory_report(generate_products()))
