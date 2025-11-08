import pytest
from src.cat_original import Cat


@pytest.fixture
def cat():
    """
    Фикстура: создаёт кота с именем "Мурзик", mood=100, energy=100.
    Позволяет избежать дублирования:
        cat = Cat()
        cat.set_name("Мурзик")
    в каждом тесте.
    """
    c = Cat()
    c.set_name("Мурзик")
    return c
