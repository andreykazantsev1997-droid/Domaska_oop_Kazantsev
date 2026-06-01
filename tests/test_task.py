import pytest

from src.task import Category, Product


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
    category_1 = Category("Смартфоны", "Описание смартфона", products_list)
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Описание смартфона"
    assert category_1.products == products_list
    assert Category.category_count == 1
    assert Category.product_count == 2
