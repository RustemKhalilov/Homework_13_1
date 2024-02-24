import pytest

from My_Objects import Category
from My_Objects import Product


def test_Category():
    product_list = [{"Карандаши": 105}]
    category_1 = Category("Карандаши", "Канцтовары", product_list, 10, 2)
    assert category_1.name == "Карандаши"
    assert category_1.description == "Канцтовары"
    assert category_1.number_of_categories == 10
    assert category_1.total_number_of_unique_product == 2


def test_Product():
    Product_1 = Product("Карандаш", "Письменные принадлежности", 35.43, 523)
    assert Product_1.name == "Карандаш"
    assert Product_1.description == "Письменные принадлежности"
    assert Product_1.price == 35.43
    assert Product_1.quantity == 523



def test_counter_category():
    product_list = [{"Карандаши": 105}]
    category_1 = Category("Канцтовары", "Карандаши", product_list,10, 2)
    product_list = [{"Помидоры": 60}]
    category_2 = Category("Продукты", "Помидоры", product_list,10, 2)
    product_list = [{"Тархун": 1020},
                    {"Груша": 1020},
                    {"Хлеб": 1020},
                    {"Чай": 1020}]
    category_3 = Category("Напитки", "Чай", product_list,10, 2)
    assert category_3.category_count == 3
    assert category_3.product_count == 6



