"""This file contains the class of ACME products
titled Product
"""

import random


class Product:
    """ACME Corporation product details

    Attributes
    ----------
    name : str
        no default value
    price : int
        default value of 10
    weight : int
        default value of 20
    flammability : float
        default value of 0.5
    identifier : int
        no default value
        ranges from 1_000_000 to 9_999_999
    """
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        """ Constructor for Product class with name required
        Parameters
        ----------
        name : str
            identifies product by name
            no default value
        price : int
            intentifies product cost
            default value = 10
        weight : int
            identifies product weight
            default value = 20
        flammability : float
            identifies likelihood of becoming on fire
            default value = 0.5
        """
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        """Returns a value to describe how easy it is to steal"""
        if (self.price / self.weight) < 0.5:
            return "Not so stealable..."
        if (self.price / self.weight) < 1.0:
            return "Kinda stealable"
        return "Very stealable"

    def explode(self):
        """Calculates a measure of explosion : flammability * weight"""
        if (self.flammability * self.weight) < 10:
            return "...fizzle."
        if (self.flammability * self.weight) < 50:
            return "...boom!"
        return "...BABOOM!!"


class BoxingGlove(Product):
    """ACME Corporation Boxing Glove
    Attributes
    ----------
    name : str
        no default value
        price : int
        default value of 10
    weight : int
        default value of 10
    flammability : float
        default value of 0.5
    identifier : int
        no default value
        ranges from 1_000_000 to 9_999_999
    """

    def __init__(self, name, price=10, weight=10, flammability=0.5):
        """ Constructor for Boxing Glove class with name required
        Parameters
        ----------
        name : str
            identifies product by name
            no default value
        price : int
            intentifies product cost
            default value = 10
        weight : int
            identifies product weight
            default value = 20
        flammability : float
            identifies likelihood of becoming on fire
            default value = 0.5
        """
        Product.__init__(self, name, price, weight, flammability)

    def explode(self):
        """Boxing Gloves do not explode"""
        return "...it's a glove"

    def punch(self):
        """Determines intensity of punch"""
        if self.weight < 5:
            return "That tickles."
        if self.weight < 15:
            return "Hey that hurt!"
        return "Ouch"
