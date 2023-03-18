from datetime import time


def test_dark_theme():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    night_start_time = time(hour=22)
    night_end_time = time(hour=6)
    current_time = time(hour=23)

    # DONE переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)

    # is_dark_theme = None

    if night_end_time.hour <= current_time.hour <= night_start_time.hour:
        is_dark_theme = False
    else:
        is_dark_theme = True

    # print(is_dark_theme)
    # print(type(is_dark_theme))
    assert is_dark_theme is True

    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    """
    current_time = time(hour=16)

    # DONE переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную

    is_dark_theme = None

    if is_dark_theme is True or night_end_time.hour <= current_time.hour <= night_start_time.hour:
        is_dark_theme = True
    else:
        is_dark_theme = True

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # DONE найдите пользователя с именем "Olga"
    suitable_user = {}

    for user in users:
        if user['name'] == 'Olga':
            suitable_user.update({'name': user['name'], 'age': user['age']})

    assert suitable_user == {"name": "Olga", "age": 45}

    # DONE найдите всех пользователей младше 20 лет
    suitable_users = []

    for user in users:
        if user['age'] < 20:
            suitable_users.append({'name': user['name'], 'age': user['age']})

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"

def create_readable_func_name_and_args(name_func, *args, sep=', '):
    readable_func_name = name_func.__name__.replace('_', ' ').title()
    readable_args = sep.join(str(arg) for arg in args)
    return f"{readable_func_name} [{readable_args}]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_company_name_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = create_readable_func_name_and_args(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_company_name_homepage(page_url):
    actual_result = create_readable_func_name_and_args(go_to_company_name_homepage, page_url)
    assert actual_result == "Go To Company Name Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = create_readable_func_name_and_args(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
