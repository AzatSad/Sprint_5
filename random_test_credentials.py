import random


class RandomTestCredentials:
    name = f"Azat{random.randint(1, 9999)}"
    email = f"azat_sadertdonov_4_{random.randint(1, 9999)}@yandex.ru"
    password = f"{random.randint(100, 99999999)}"
    incorrect_password = f"{random.randint(10, 99)}"