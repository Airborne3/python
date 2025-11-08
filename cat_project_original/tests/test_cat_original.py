import pytest
from src.cat_original import Cat


class TestCatOriginal:
    def test_set_name_initializes_state(self):
        """Поведение оригинального класса: после set_name → mood=100, energy=100"""
        cat = Cat()
        cat.set_name("Мурка")
        assert cat.get_name() == "Мурка"
        assert cat.mood == 100
        assert cat.energy == 100

    def test_play_increases_both_mood_and_energy_by_1(self):
        """Фактическое поведение (ошибка!): play() добавляет +1 к mood И +1 к energy, НЕЗАВИСИМО от time"""
        cat = Cat()
        cat.set_name("Барсик")
        cat.play(5)   # time=5, но изменения: +1 и +1
        assert cat.mood == 101   #  ОШИБКА: превышает 100, и не зависит от time
        assert cat.energy == 101 # ОШИБКА: растёт, а должна падать

    def test_play_called_multiple_times(self):
        """Каждый вызов play() даёт +1/+1, даже с time=0 или time=100"""
        cat = Cat()
        cat.set_name("Рыжик")
        cat.play(0)    # time=0 всё равно +1/+1
        cat.play(100)  # time=100  опять +1/+1
        assert cat.mood == 102
        assert cat.energy == 102

    def test_no_bounds_on_mood_or_energy(self):
        """В оригинальном классе НЕТ ограничений: mood и energy могут быть >100 или <0"""
        cat = Cat()
        cat.set_name("Снежок")
        for _ in range(50):
            cat.play(10)  # 50 раз по +1/+1
        assert cat.mood == 150   # >100 — нарушение ТЗ
        assert cat.energy == 150 # >100 — нарушение ТЗ (и вообще растёт!)

    @pytest.mark.parametrize("time_input", [0, 1, 10, 100, -5])
    def test_play_ignores_time_parameter(self, time_input):
        """Параметризованный тест: play() НЕ использует аргумент time — эффект всегда +1/+1"""
        cat = Cat()
        cat.set_name("Тестик")
        initial_mood = cat.mood
        initial_energy = cat.energy

        cat.play(time_input)

        assert cat.mood == initial_mood + 1
        assert cat.energy == initial_energy + 1
        # time_input не влияет — это ошибка!

        '''Все тесты проходят, потому что они проверяют фактическое поведение, а не ожидаемое.
            Но результаты выявляют расхождения с ТЗ:
            энергия растёт, а должна падать;
            настроение не ограничено 100;
            параметр time игнорируется;
            за 1 секунду должно меняться на ±1, но здесь — за 1 вызов, независимо от длительности.'''