from field import Field

class Phone(Field):
    """Class for address book record phone field"""
    def __init__(self, phone: str):
        self.value = self.__validate_phone(phone)

    def __validate_phone(self, phone: str) -> bool:
        """
        Phone validation
        Returns phone if length is 10 and all chars are digits
        """
        if len(phone) != 10:
            raise ValueError("The phone number must contain 10 digits")

        if not phone.isdigit():
            raise ValueError("The phone number must contain only numbers")

        return phone
