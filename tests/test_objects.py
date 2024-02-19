from My_Objects import Category
from My_Objects import Product


def test_Category():
    category_1 = Category("Канстовары", "Письменные принадлежности", "Карандаши", 10, 2)

    assert category_1.name == "Канстовары"
    assert category_1.description == "Письменные принадлежности"
    assert category_1.description == "Письменные принадлежности"
    assert category_1.products == "Карандаши"
    assert category_1.number_of_categories == 10
    assert category_1.total_number_of_unique_product == 2


def test_Product():
    Product_1 = Product("Карандаш", "Письменные принадлежности", 35.43, 523)
    assert Product_1.name == "Карандаш"
    assert Product_1.description == "Письменные принадлежности"
    assert Product_1.price == 35.43
    assert Product_1.quantity == 523
