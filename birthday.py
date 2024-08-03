from datetime import datetime
from field import Field

class Birthday(Field):
    """Class for address book record birthday field"""
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
