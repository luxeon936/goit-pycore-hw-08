class Field:
    """Base class for address book record fields"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
