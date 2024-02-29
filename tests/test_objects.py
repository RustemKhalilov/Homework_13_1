import pytest

from My_Objects import Category
from My_Objects import Product


def test_Category():
    Product_1 = Product("Карандаш", "Канцтовары", 35.43, 105)
    category_1 = Category("Карандаши", "Канцтовары")
    assert category_1.name == "Карандаши"
    assert category_1.description == "Канцтовары"
    category_1.add_product(Product_1)
    category_1.products == {'name': "Карандаш", 'quantity': 105, 'price': 35.43}


def test_Product():
    Product_1 = Product("Карандаш", "Канцтовары", 35.43, 523)
    assert Product_1.name == "Карандаш"
    assert Product_1.description == "Канцтовары"
    assert Product_1.price == 35.43
    assert Product_1.quantity == 523
    assert Product_1.price == 35.43


def test_counter_category():
    category_1 = Category("Канцтовары", "Карандаши")
    Product_1 = Product("Карандаши", "Канцтовары", 35.43, 105)
    category_1.add_product(Product_1)
    category_1.product_conter()
    category_2 = Category("Продукты", "Помидоры")
    Product_2 = Product("Помидоры", "Продукты", 150, 305)
    category_2.add_product(Product_2)
    category_2.product_conter()
    category_3 = Category("Напитки", "Чай")
    Product_3 = Product("Чай", "Напитки", 250, 400)
    Product_4 = Product("Тархун", "Напитки", 70, 700)
    Product_5 = Product("Груша", "Напитки", 150, 200)
    category_3.add_product(Product_3)
    category_3.add_product(Product_4)
    category_3.add_product(Product_5)
    category_3.product_conter()
    assert category_3.category_count == 3
    assert category_3.product_count == 5

