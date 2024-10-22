"""
Протестируйте классы из модуля homework/models.py
"""
from itertools import count

import pytest

from models import Product
from models import Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert True == product.check_quantity(1000)
        assert False == product.check_quantity(1001)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(1000)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError) as e:
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add_product_added(self, cart, product):
        cart.add_product(product, 10)

        assert cart.products[product] == 10

    def test_cart_add_product_increased_quantity(self, cart, product):
        cart.add_product(product, 10)
        cart.add_product(product, 10)

        assert cart.products[product] == 20

    def test_cart_remove_product(self, cart, product):
        cart.add_product(product, 10)
        cart.remove_product(product)

        assert False == bool(cart.products.get(product))

    def test_cart_remove_product_too_many(self, cart, product):
        cart.add_product(product, 15)
        cart.remove_product(product, 20)

        assert False == bool(cart.products.get(product))

    def test_cart_remove_product_raise_exception(self, cart, product):
        cart.add_product(product, 15)

        t = Product("t", 10, "tt", 20)

        with pytest.raises(ValueError):
            cart.remove_product(t)

    def test_clear(self, cart, product):
        cart.add_product(product, 10)
        cart.clear()

        assert len(cart.products.keys()) == 0

    def test_total_price(self, cart, product):
        cart.add_product(product, 10)

        assert cart.get_total_price() == 1000

    def test_buy_empty(self, cart, product):
        with pytest.raises(ValueError):
            cart.buy()

    def test_buy(self, cart, product):
        cart.add_product(product, 10)
        cart.buy()

    def test_buy_too_many(self, cart, product):
        cart.add_product(product, 2000)
        with pytest.raises(ValueError):
            cart.buy()