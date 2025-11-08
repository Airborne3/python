import pytest
from src.cat_original import Cat


class TestCatParametrized:

    @pytest.mark.parametrize(
        "time_input, expected_mood, expected_energy",
        [
            (0, 101, 101),
            (1, 101, 101),
            (5, 101, 101),
            (100, 101, 101),
            (-10, 101, 101),
        ],
        ids=["time=0", "time=1", "time=5", "time=100", "time=-10"]
    )
    def test_play_ignores_time_parameter(self, time_input, expected_mood, expected_energy):
        cat = Cat()
        cat.set_name("Мурзик")  # mood=100, energy=100
        cat.play(time_input)
        assert cat.mood == expected_mood
        assert cat.energy == expected_energy