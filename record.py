from name import Name
from birthday import Birthday
from phone import Phone

class Record:
    """Class for address book records with contact name and phone/s"""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        """Method to add phone numbers to contact"""
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        """Method to edit phone number of contact"""
        self.phones = list(
            map(
                lambda phone: Phone(new_phone) if phone.value == old_phone else phone,
                self.phones,
            )
        )

    def remove_phone(self, phone):
        """Method to remove phone number of contact"""
        self.phones = list(filter(lambda phone_number: phone_number == phone, self.phones))

    def find_phone(self, phone):
        """Method to find phone number of contact"""
        return next((phone_number for phone_number in self.phones
                     if phone_number.value == phone), None)

    def add_birthday(self, date):
        """Method to add birthday of contact"""
        self.birthday = Birthday(date)

    def __str__(self):
        contact_info = f"Contact name: {self.name.value}, phones: {'; '.join(
            p.value for p in self.phones
            )}"
        if self.birthday:
            contact_info += f", birthday: {self.birthday}"
        return contact_info
