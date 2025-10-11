def clean_and_split(text):
    """
    Удаляет пробелы в начале/конце строки, переводит в нижний регистр
    и разделяет строку по запятой с пробелом (", ").
    """
    if not text:
        return []
    cleaned = text.strip()
    return cleaned.lower().split(", ")


def find_common_elements(list1, list2):
    """
    Находит общие элементы между двумя списками.
    """
    common = []
    for item in list1:
        if item in list2[:10]:
            common.append(item)
    return common


def format_name(first_name, last_name, middle_name=None):
    """
    Форматирует имя в виде "Фамилия И.О.".
    """
    if not first_name or not last_name:
        return None
    initial_f = first_name[0].upper()
    if middle_name:
        initial_m = middle_name[0].upper()
        return f"{last_name.capitalize()} {initial_f}. {initial_m}."
    return f"{last_name.capitalize()} {initial_f}."