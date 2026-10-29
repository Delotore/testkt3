import requests

BASE_URL = "https://dummyjson.com"


def search_products(query, base_url=BASE_URL):
    response = requests.get(
        f"{base_url}/products/search",
        params={"q": query},
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


def get_product(product_id, base_url=BASE_URL):
    response = requests.get(
        f"{base_url}/products/{product_id}",
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


def add_todo(todo, completed, user_id, base_url=BASE_URL):
    response = requests.post(
        f"{base_url}/todos/add",
        json={
            "todo": todo,
            "completed": completed,
            "userId": user_id,
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


def add_product(title, price, base_url=BASE_URL):
    response = requests.post(
        f"{base_url}/products/add",
        json={
            "title": title,
            "price": price,
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()