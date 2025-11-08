import pytest
from src.cat_original import Cat


def test_cat_initial_state(cat):
    """Тест: проверка начального состояния кота из фикстуры"""
    assert cat.get_name() == "Мурзик"
    assert cat.mood == 100
    assert cat.energy == 100


def test_play_increments_mood_and_energy_by_1(cat):
    """Тест: после play() — mood и energy увеличиваются на 1 (фактическое поведение)"""
    initial_mood = cat.mood      # 100
    initial_energy = cat.energy  # 100

    cat.play(5)  # time=5, но эффект: +1/+1

    assert cat.mood == initial_mood + 1      # 101
    assert cat.energy == initial_energy + 1  # 101

    """ Фикстуру можно расширить @pytest.fixture(params=["Мурзик", "Барсик", "Снежок"])
    Устраняет дублирование.
    Упрощает поддержку: если логика инициализации изменится — правим в одном месте (conftest.py).
    
    Поддерживает isolation: каждый тест получает свежего кота, 
    потому что фикстура по умолчанию имеет scope=function."""