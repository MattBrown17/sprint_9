"""Test File designed to test ACME Product class
and generate_products function"""

from acme import Product
# from acme_report import generate_products, Adj, Noun


def test_default_product_price():
    """"Tests default price == 10"""
    prod = Product('Test Product')
    assert prod.price == 10


def test_explode_method():
    """Uses instance of product to test explode method"""
    prod1 = Product('prod1', weight=10, flammability=0.8)
    prod2 = Product('prod2', weight=10, flammability=1.2)
    prod3 = Product('prod3', weight=10, flammability=5.5)
    assert prod1.explode()[3] == 'f'
    assert prod2.explode()[3] == 'b'
    assert prod3.explode()[4] == 'A'
