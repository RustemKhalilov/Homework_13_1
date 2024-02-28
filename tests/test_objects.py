import pytest

from My_Objects import Category
from My_Objects import Product


def test_Category():
    product_list = [{"Карандаши": 105}]
    category_1 = Category("Карандаши", "Канцтовары")
    assert category_1.name == "Карандаши"
    assert category_1.description == "Канцтовары"
    category_1.add_list_product(product_list)
    category_1.get_list_product == f'Карандаши 105'


def test_Product():
    Product_1 = Product("Карандаш", "Письменные принадлежности", 35.43, 523)
    assert Product_1.name == "Карандаш"
    assert Product_1.description == "Письменные принадлежности"
    assert Product_1.price == 35.43
    assert Product_1.quantity == 523
    assert Product_1.price_list == f'Карандаш, 35.43 руб. Остаток 523 шт.'



def test_counter_category():
    product_list = [{"Карандаши": 105}]
    category_1 = Category("Канцтовары", "Карандаши")
    category_1.add_list_product(product_list)
    category_1.product_conter()
    product_list = [{"Помидоры": 60}]
    category_2 = Category("Продукты", "Помидоры")
    category_2.add_list_product(product_list)
    category_2.product_conter()
    product_list = [{"Тархун": 1020},
                    {"Груша": 1020},
                    {"Хлеб": 1020},
                    {"Чай": 1020}]
    category_3 = Category("Напитки", "Чай")
    category_3.add_list_product(product_list)
    category_3.product_conter()
    assert category_3.category_count == 3
    assert category_3.product_count == 6



