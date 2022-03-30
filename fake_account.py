from random import randint, choice

from faker import Faker


class FakeAccount:

    FAKER = Faker()
    DIGITS = '123456789'
    SYMBOLS = '._-'

    def __init__(self):
        self.first_name = self.FAKER.first_name()
        self.last_name = self.FAKER.last_name()
        self.digits_count = randint(5, 7)

    @property
    def username(self):
        username = (
            f'{self.first_name.lower()}'
            f'{choice(self.SYMBOLS)}'
            f'{self.last_name.lower()}'
            f'{"".join([choice(self.DIGITS) for _ in range(self.digits_count - 2)])}'
        )
        return username if len(username) <= 32 else username[:32]

    @property
    def password(self):
        password = (
            f'{self.last_name}'
            f'{choice(self.DIGITS)}'
            f'{self.first_name}'
            f'{"".join([choice(self.DIGITS) for _ in range(self.digits_count)])}'
        )
        return password if len(password) <= 32 else password[:32]

    @property
    def secret_answer(self):
        return int(''.join(choice(self.DIGITS) for _ in range(4)))
