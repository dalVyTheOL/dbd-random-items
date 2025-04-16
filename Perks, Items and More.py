import random
from colorama import Fore, Style

Perks = {
    1: "Связь",
    2: "Прояви себя",
    3: "Лидер",
    4: "Спокойствие духа",
    5: "Железная воля",
    6: "Крушитель",
    7: "Ловкое приземление",
    8: "Городской бег",
    9: "Уроки Улиц",
    10: "Туз в рукаве",
    11: "Повысить ставки",
    12: "Игра в открытую",
    13: "Познания в ботанике",
    14: "Сострадание",
    15: "Сам себе доктор",
    16: "Адреналин",
    17: "Быстрый и тихий",
    18: "Спринтер",
    19: "Единственный выживший",
    20: "Решающий удар",
    21: "Объект одержимости",
    22: "Одолженное время",
    23: "Оставленный позади",
    24: "Несокрушимый",
    25: "Тревога",
    26: "Гибкость",
    27: "Техник",
    28: "Мы будем жить вечно",
    29: "Крепкий орешек",
    30: "Без сожаления",
    31: "Потанцуй со мной",
    32: "Уникальная возможность",
    33: "Через край",
    34: "Уход за больным",
    35: "Поломка",
    36: "Искажение",
    37: "Любыми средствами",
    38: "Форсаж",
    39: "Везение",
    40: "Стиснув зубы",
    41: "Световая граната",
    42: "Дух новичка",
    43: "Фугасная мина",
    44: "Поправка",
    45: "Противодействие",
    46: "Жучок",
    47: "Ниже травы",
    48: "Поспешное лечение",
    49: "Как новенький",
    50: "Ободрение",
    51: "Полная сосредоточенность",
    52: "Драматургия",
    53: "Партнер по сцене",
    54: "Вот это поворот",
    55: "Ясновиденение",
    56: "Дар: Круг исцеления",
    57: "Дар: Уход в тень",
    58: "Раскачка",
    59: "Пристегнись",
    60: "Проверка на прочность",
    61: "Скользкое мясо",
    62: "Муражки по спине",
    63: "Дежавю",
    64: "Кровные узы",
    65: "Надежда",
    66: "Мы справимся",
    67: "Мелкая дичь",
    68: "Устойчивость",
    69: "Легковес",
    70: "Мародёрское чутье",
    71: "Воин света",
    72: "Дар: Освещение",
    73: "Дэдлайн",
    74: "Чары: Пауки прядильщики",
    75: "Сила во мраке",
    76: "Дерзость",
    77: "Вдохновение барда",
    78: "Зеркальная иллюзия",
    79: "Замри и увидишь",
    80: "Сноровка",
    81: "Специалист",
    82: "Закалка",
    83: "Ради людей",
    84: "Обман во благо",
    85: "Без огласки"
}

def get_random_perks(perks_dict, num_perks):
    random_perks = random.sample(list(perks_dict.values()), num_perks)
    return random_perks

num_perks_to_select = 4

print(Fore.MAGENTA + "Перки для игры:" + Style.RESET_ALL)
print()

random_perks = get_random_perks(Perks, num_perks_to_select)
for perk in random_perks:
    print(Fore.MAGENTA + perk + Style.RESET_ALL)
print()
print()

Items = {
    1: "Аптечка",
    2: "Инструменты",
    3: "Ключ",
    4: "Карта",
    5: "Фонарик",
    6: "Хлопушка"
}

def get_random_items(items_dict, num_items):
    random_items = random.sample(list(items_dict.values()), num_items)
    return random_items

num_items_to_select = 1

print(Fore.YELLOW + "Предметы для игры:" + Style.RESET_ALL)
print()

random_items = get_random_items(Items, num_items_to_select)
for item in random_items:
    print(Fore.YELLOW + item + Style.RESET_ALL)
print()
print()

Offerings = {
    1: "Bloody-Party",
    2: "Люк в хижине убийцы",
    3: "Люк в основном здании",
    4: "Реагент",
    5: "Банка Виго или другой айтем на удачу",
    6: "Платок",
    7: "Монета",
    8: "Дуб",
    9: "Подвал в основном здании",
    10: "Подвал в хижине",
    11: "Карта(измерение)"
}

def get_random_offerings(offerings_dict, num_offerings):
    random_offerings = random.sample(list(offerings_dict.values()), num_offerings)
    return random_offerings

num_offerings_to_select = 1

print(Fore.RED + "Подношения для игры:" + Style.RESET_ALL)
print()

random_offerings = get_random_offerings(Offerings, num_offerings_to_select)
for offering in random_offerings:
    print(Fore.RED + offering + Style.RESET_ALL)
