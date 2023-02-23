from faker import Faker

fake = Faker()


class BaseContact:
    def __init__(self, name, surname, phone_number, email):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email
        self._name_length = len(self.name) + 1 + len(self.surname)

    def contact(self):
        print(
            f"Wybieram numer {self.phone_number} i dzwonię do {self.name} {self.surname}."
        )

    @property
    def name_length(self):
        return self._name_length


class BusinessContact(BaseContact):
    def __init__(self, work_number, company, job, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.work_number = work_number
        self.company = company
        self.job = job

    def contact(self):
        print(
            f"Wybieram numer {self.work_number} i dzwonię do {self.name} {self.surname}."
        )


# returns list of chosen number of random contacts with specified type
def create_contacts(number_of_contacts, contact_type):
    list_of_contacts = []
    for i in range(number_of_contacts):
        if contact_type == "Base":
            new_contact = BaseContact(
                name=fake.first_name(),
                surname=fake.last_name(),
                phone_number=fake.phone_number(),
                email=fake.free_email(),
            )
        elif contact_type == "Business":
            # there is possiblity that phone_number == work_number
            new_contact = BusinessContact(
                name=fake.first_name(),
                surname=fake.last_name(),
                phone_number=fake.phone_number(),
                email=fake.free_email(),
                work_number=fake.phone_number(),
                company=fake.company(),
                job=fake.job(),
            )
        else:
            print("Zły typ wizytówki")
            break
        list_of_contacts.append(new_contact)
    return list_of_contacts


# example of use
if __name__ == "__main__":
    contacts_list = create_contacts(72, "Business")
    for single_contact in contacts_list:
        single_contact.contact()
