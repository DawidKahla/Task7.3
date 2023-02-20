from faker import Faker
fake = Faker()
# 'John'

class visiting_card:
    def __init__(self, name, surname, company, position, email):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.email = email
    def __str__(self):
        return f"{self.name} {self.surname}, {self.position} in {self.company}, e-mail adress: {self.email}"

for _ in range(10):
    card = visiting_card(name=fake.first_name(), surname=fake.last_name(), company=fake.company(), position=fake.job(), email=fake.free_email())
    print(card)
