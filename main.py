from address_book import AddressBook
from record import Record
import pickle

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"

    return inner

def index_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Contact don't exist"

    return inner

def key_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Phone don't exist"

    return inner


def parse_input(user_input: str) -> list:
    """
    Parse console input

    Returns: 
        Parsed values of command and arguments
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book: AddressBook):
    """
    Add contact to dictionary

    Returns:
        Console message of result
    """
    name, phone, *_ = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        if phone:
            record.add_phone(phone)
        book.add_record(record)
        return "Contact added"
    if phone:
        record.add_phone(phone)
    return "Contact updated"

@input_error
def change_contact(args: list, book: AddressBook) -> str:
    """
    Change contact in dictionary

    Returns:
        Console message of result
    """
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        return "Contact does not exist"
    else:
        record.edit_phone(old_phone, new_phone)
        return "Phone changed"

@key_error
@index_error
@input_error
def show_phone(args: list, book: AddressBook) -> str:
    """
    Show phone number of contact from dictionary

    Returns:
        Console message of result
    """
    name = args[0]
    record = book.find(name)
    if record is None:
        return "Contact does not exist"
    return record

@input_error
def add_birthday(args, book: AddressBook):
    """
    Add birthday to a contact in a dictionary

    Returns:
        Console message of result
    """
    name, birthday, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact does not exist"
    record.add_birthday(birthday)
    return "Birthday added."

@input_error
def show_birthday(args, book: AddressBook):
    """
    Add birthday to a contact in a dictionary

    Returns:
        Console message of result
    """
    name = args[0]
    record = book.find(name)
    if record:
        if record.birthday:
            return record.birthday
        return "Birthday not added to this contact"
    return "Contact does not exist"

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            if not book:
                print("Contacts list empty")
            else:
                print(book)
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(book.get_upcoming_birthdays())
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()