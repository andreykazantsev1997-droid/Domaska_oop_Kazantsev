import pytest

from src.task import Category, LawnGrass, Product, Smartphone


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
    expected_products = "Смартфоны, количество продуктов: 6 шт."
    category_1 = Category("Смартфоны", "Описание смартфона", products_list)
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Описание смартфона"
    assert category_1.products == expected_products
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_add_product():
    p1 = Product("Товар 1", "Описание 1", 100.0, 5)
    category = Category("Смартфоны", "Мобильные телефоны", [p1])
    p2 = Product("Товар 2", "Описание 2", 200.0, 10)
    category.add_product(p2)
    assert Category.product_count == 4


def test_category_products_property():
    p1 = Product("Samsung Galaxy S23", "Флагман", 180000.0, 5)
    category = Category("Смартфоны", "Мобильные телефоны", [p1])
    expected_info = "Смартфоны, количество продуктов: 5 шт."
    assert category.products == expected_info


def test_new_product():
    product_dict = {
        "name": "Наушники",
        "description": "Беспроводные",
        "price": 5000.0,
        "quantity": 25,
    }
    product = Product.new_product(product_dict)
    assert product.name == "Наушники"
    assert product.price == 5000.0
    assert product.quantity == 25


def test_price_update():
    product = Product("Телевизор", "Плазменный", 50000.0, 5)
    product.price = 55000.0
    product.price = -100
    assert product.price == 55000.0
    assert product.price == 55000.0


def test_product_str():
    product = Product(
        name="Samsung Galaxy", description="Смартфон", price=70000.0, quantity=5
    )
    expected_str = "Samsung Galaxy, 70000.0 руб. Остаток: 5 шт."
    assert str(product) == expected_str


def test_product_add_zero_quantity():
    product1 = Product(
        name="iPhone 15", description="Apple", price=100000.0, quantity=0
    )
    product2 = Product(name="Чехол", description="Аксессуар", price=1500.0, quantity=10)
    assert product1 + product2 == 15000.0


@pytest.fixture
def data():
    category = Category("Тест", "Описание", [])
    phone = Smartphone("iPhone", "Описание", 1000, 2, "High", "15", "128", "Black")
    grass = LawnGrass("Трава", "Описание", 100, 5, "Россия", "10 дней", "Зеленая")
    return category, phone, grass


def test_add_correct_product(data):
    category, phone, _ = data
    category.add_product(phone)
    assert phone in category._Category__products


def test_products_addition_type_error(data):
    _, phone, grass = data
    with pytest.raises(TypeError):
        phone + grass


def test_add_product_type_error(data):
    category, _, _ = data
    with pytest.raises(TypeError):
        category.add_product("Просто строка текста")
