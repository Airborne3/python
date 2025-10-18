import pytest
from test_data_processor import clean_and_split, find_common_elements, format_name


class TestCleanAndSplit:
    """Тесты для функции clean_and_split."""

    def test_normal_input(self):
        assert clean_and_split("Apple, Banana, Cherry") == ["apple", "banana", "cherry"]

    def test_empty_string(self):
        assert clean_and_split("") == []

    def test_none_input(self):
        assert clean_and_split(None) == []

    def test_only_spaces(self):
        assert clean_and_split("   ") == []

    def test_no_comma(self):
        assert clean_and_split("apple") == ["apple"]

    def test_extra_spaces_around_comma(self):
        assert clean_and_split("apple,  banana") == ["apple", " banana"]
    def test_mixed_case(self):
        assert clean_and_split("APPLE, banana, ChErRy") == ["apple", "banana", "cherry"]


class TestFindCommonElements:

    def test_normal_common_elements(self):
        list1 = ["a", "b", "c"]
        list2 = ["b", "d", "a", "e", "f", "g", "h", "i", "j", "k", "c"]
        assert find_common_elements(list1, list2) == ["a", "b"]  # "c" не в первых 10 list2!

    def test_no_common_elements(self):
        assert find_common_elements(["x", "y"], ["a", "b"]) == []

    def test_empty_lists(self):
        assert find_common_elements([], ["a", "b"]) == []
        assert find_common_elements(["a"], []) == []
        assert find_common_elements([], []) == []

    def test_list2_shorter_than_10(self):
        list1 = ["a", "b", "c"]
        list2 = ["b", "c"]
        assert find_common_elements(list1, list2) == ["b", "c"]

    def test_duplicates_in_list1(self):
        list1 = ["a", "a", "b"]
        list2 = ["a", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
        assert find_common_elements(list1, list2) == ["a", "a"]

    def test_case_sensitivity(self):
        list1 = ["Apple"]
        list2 = ["apple"]
        assert find_common_elements(list1, list2) == []  # Потому что "Apple" != "apple"

    def test_list2_has_more_than_10_elements(self):
        list1 = ["z"]
        list2 = ["a"] * 10 + ["z"]
        assert find_common_elements(list1, list2) == []  # "z" за пределами первых 10


class TestFormatName:

    def test_full_name_with_middle(self):
        assert format_name("ivan", "petrov", "sergeevich") == "Petrov I. S"

    def test_full_name_no_middle(self):
        assert format_name("anna", "smirnova") == "Smirnova A."

    def test_empty_first_name(self):
        assert format_name("", "smith") is None
        assert format_name(None, "smith") is None

    def test_empty_last_name(self):
        assert format_name("john", "") is None
        assert format_name("john", None) is None

    def test_single_letter_names(self):
        assert format_name("a", "b", "c") == "B A. C"

    def test_capitalization_of_last_name(self):
        assert format_name("john", "o'connor") == "O'connor J."
        assert format_name("marie", "van der waals") == "Van der waals M."

    def test_middle_name_none_vs_empty_string(self):
        assert format_name("alex", "brown", None) == "Brown A."
        assert format_name("alex", "brown", "") == "Brown A. "  # ← БАГ: лишний пробел и точка отсутствует у отчества

    def test_case_of_input_names(self):
        assert format_name("IVAN", "PETROV", "SERGEEVICH") == "Petrov I. S"
        assert format_name("iVaN", "pEtRoV") == "Petrov I."