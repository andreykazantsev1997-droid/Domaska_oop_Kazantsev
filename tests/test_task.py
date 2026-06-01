from itertools import product

import pytest
from src.task import Product, Category

@pytest.fixture
def products_list():
    product_1 = Product("Samsung Galaxy S23 Ultra", "256GB", 180000.0, 5)
    product_2 = Product("OnePlus", "512GB", 500000.0, 1)
    return product_1, product_2

def test_product_init():
    product = Product("OnePlus", "512GB", 500000.0, 1)
    assert product.name == "OnePlus"
    assert product.description == "512GB"
    assert product.price == 500000.0
    assert product.quantity == 1

def test_category_init(products_list):
    Category.category_count = 0
    Category.product_count = 0
    category1 = Category("Смартфоны", "Описание смартфона", products_list)
    assert category1.name == "Смартфоны"
    assert category1.description == "Описание смартфона"
    assert category1.products == products_list
    assert Category.category_count == 1
    assert Category.product_count == 2

    product3 = Product("Телевизор", "4K", 100000.0, 1)
    category2 = Category("Телевизоры", "Описание ТВ", [product3])
    assert Category.category_count == 2
    assert Category.product_count == 3
