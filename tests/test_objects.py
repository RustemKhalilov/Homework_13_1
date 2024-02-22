from My_Objects import Category
from My_Objects import Product
from My_func import  counter_category, counter_product


def test_Category():
    category_1 = Category("Карандаши", "Канцтовары", 10, 2)
    assert category_1.name == "Карандаши"
    assert category_1.description == "Канцтовары"
    assert category_1.number_of_categories == 10
    assert category_1.total_number_of_unique_product == 2


def test_Product():
    Product_1 = Product("Карандаш", "Письменные принадлежности", 35.43, 523, "Карандаши")
    assert Product_1.name == "Карандаш"
    assert Product_1.description == "Письменные принадлежности"
    assert Product_1.price == 35.43
    assert Product_1.quantity == 523
    assert Product_1.category_name == "Карандаши"

def test_counter_category():
    category_1 = Category("Карандаши", "Канцтовары", 10, 2)
    category_2 = Category("Продукты", "Помидоры", 10, 2)
    category_3 = Category("Напитки", "Тархун", 10, 2)
    category_4 = Category("Продукты", "Груша", 10, 2)
    category_5 = Category("Продукты", "Хлеб", 10, 2)
    category_6 = Category("Напитки", "Чай", 10, 2)
    list_category = [category_1, category_2, category_3, category_4, category_5, category_6]
    assert counter_category(list_category) == 3

def test_counter_product():
    Product_1 = Product("Карандаш", "Письменные принадлежности", 35.43, 523, "Карандаши")
    Product_2 = Product("Телефон 1", "Смартфоны DEXP", 18400.00, 25, "Смартфоны")
    Product_3 = Product("Яблоки", "Продукты", 88, 250, "Продукты")
    Product_4 = Product("Ручка", "Письменные принадлежности", 34, 530, "Ручки")
    Product_5 = Product("Яблоки", "Продукты", 88, 500, "Продукты")
    Product_6 = Product("Телефон 1", "Смартфоны DEXP", 18400.00, 75, "Смартфоны")
    list_product = [Product_1, Product_2, Product_3, Product_4, Product_5, Product_6, Product_6]
    assert counter_product(list_product) == {'Карандаш': 523, 'Ручка': 530, 'Телефон 1': 175, 'Яблоки': 750}