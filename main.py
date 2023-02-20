from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self, name, surname, phone_number, email):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email 
    def contact(self):
        print(f"Wybieram numer +48 {self.phone_number} i dzwonię do {self.name} {self.surname}.")   
    @property
    def label_length(self):
        return len(self.name) + 1 + len(self.surname)

class BusinessContact(BaseContact):
    def __init__(self, work_number, company, job, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.work_number = work_number
        self.company = company
        self.job = job
    def contact(self):
        print(f"Wybieram numer +48 {self.work_number} i dzwonię do {self.name} {self.surname}.")   
    
def create_contacts():
    pass
    #return visiting_card(name=fake.first_name(), surname=fake.last_name(), company=fake.company(), position=fake.job(), email=fake.free_email())

