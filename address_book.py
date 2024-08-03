from collections import UserDict
from datetime import datetime, timedelta
from record import Record

class AddressBook(UserDict):
    """Class for address book"""
    def add_record(self, record: Record):
        """Method to add a record to address book"""
        self.data[record.name.value] = record

    def find(self, name):
        """Method to find a record by name"""
        #if name not in self.data:
            #raise KeyError(f"Record with name '{name}' not found.")
        return self.data.get(name)

    def delete(self, name):
        """Method to delete a record from address book"""
        if name not in self.data:
            raise KeyError(f"Record with name '{name}' not found")
        del self.data[name]

    def get_upcoming_birthdays(self) -> list[dict]:
        """
        Calculation of celebration dates

        Returns:
            List of celebration dates
        """
        today = datetime.today()
        upcoming_birthdays = []
        for name, record in self.data.items():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                if birthday_this_year.weekday() in [5, 6]:
                    birthday_this_year = birthday_this_year.replace(
                        day=birthday_this_year.day + (7 - birthday_this_year.weekday()))
                if birthday_this_year <= today + timedelta(days=7):
                    upcoming_birthdays.append(
                        {
                            "name": name,
                            "congratulation_date": birthday_this_year.strftime("%Y.%m.%d"),
                        }
                    )
        return upcoming_birthdays
    def __str__(self):
        lines = [str(record) for record in self.data.values()]
        return "\n".join(lines)
