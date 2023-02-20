from faker import Faker
fake = Faker()

class visiting_card:
    def __init__(self, name, surname, company, position, email):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.email = email
    def __str__(self):
        return f"{self.name} {self.surname}, {self.position} in {self.company}, e-mail adress: {self.email}"
    def contact(self):
        print(f"Kontaktuję się z {self.name} {self.surname}, {self.position}, {self.email}.")    
    @property
    def name_length(self):
        return len(self.name) + 1 + len(self.surname)
    
def make_fake():
    return visiting_card(name=fake.first_name(), surname=fake.last_name(), company=fake.company(), position=fake.job(), email=fake.free_email())

