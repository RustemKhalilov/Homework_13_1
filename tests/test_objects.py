import pytest

from My_Objects import Category
from My_Objects import Product


def test_Category():
    Product_1 = Product("Карандаш", "Канцтовары", 35.43, 105)
    product_list = [{'name': Product_1.name, 'quantity': Product_1.quantity, 'price': Product_1.price}]
    category_1 = Category("Карандаши", "Канцтовары", product_list)
    assert category_1.name == "Карандаши"
    assert category_1.description == "Канцтовары"
    category_1.products == 'Карандаш 35.43 руб. Остаток 105 шт.\n'


def test_Product():
    Product_1 = Product("Карандаш", "Канцтовары", 35.43, 523)
    assert Product_1.name == "Карандаш"
    assert Product_1.description == "Канцтовары"
    assert Product_1.price == 35.43
    assert Product_1.quantity == 523
    assert Product_1.price == 35.43


def test_counter_category():
    Product_1 = Product("Карандаши", "Канцтовары", 35.43, 105)
    product_list = [{'name': Product_1.name, 'quantity': Product_1.quantity, 'price': Product_1.price}]
    category_1 = Category("Канцтовары", "Карандаши", product_list)
    category_1.product_conter()

    Product_2 = Product("Помидоры", "Продукты", 150, 305)
    product_list = [{'name': Product_2.name, 'quantity': Product_2.quantity, 'price': Product_2.price}]
    category_2 = Category("Продукты", "Помидоры", product_list)
    category_2.product_conter()

    Product_3 = Product("Чай", "Напитки", 250, 400)
    product_list = [{'name': Product_3.name, 'quantity': Product_3.quantity, 'price': Product_3.price}]
    Product_4 = Product("Тархун", "Напитки", 70, 700)
    product_list.append({'name': Product_4.name, 'quantity': Product_4.quantity, 'price': Product_4.price})
    Product_5 = Product("Груша", "Напитки", 150, 200)
    product_list.append({'name': Product_5.name, 'quantity': Product_5.quantity, 'price': Product_5.price})
    category_3 = Category("Напитки", "Чай", product_list)
    category_3.product_conter()
    assert category_3.category_count == 3
    assert category_3.product_count == 5
