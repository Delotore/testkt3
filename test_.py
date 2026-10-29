import pytest

from main import (
    search_products,
    get_product,
    add_todo,
    add_product,
    BASE_URL,
)


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def product_id():
    return 1


@pytest.fixture
def todo_data():
    return {
        "todo": "Новая задача",
        "completed": False,
        "user_id": 5,
    }


@pytest.fixture
def product_data():
    return {
        "title": "Тестовый товар",
        "price": 99.99,
    }


class TestProducts:
    def test_search_products(self, base_url):
        data = search_products("phone", base_url)

        assert "products" in data
        assert isinstance(data["products"], list)
        assert data["total"] > 0

    def test_get_product(self, base_url, product_id):
        product = get_product(product_id, base_url)

        assert product["id"] == product_id
        assert "title" in product
        assert "price" in product

    def test_add_product(self, base_url, product_data):
        product = add_product(
            **product_data,
            base_url=base_url,
        )

        assert product["title"] == product_data["title"]
        assert product["price"] == product_data["price"]
        assert "id" in product


class TestTodos:
    def test_add_todo(self, base_url, todo_data):
        todo = add_todo(
            **todo_data,
            base_url=base_url,
        )

        assert todo["todo"] == todo_data["todo"]
        assert todo["completed"] is False
        assert todo["userId"] == todo_data["user_id"]
        assert "id" in todo