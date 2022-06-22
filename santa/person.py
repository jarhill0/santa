class Person:
    """A class to represent a person with an email address."""

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return '{} <{}>'.format(self.name, self.address)

    def __eq__(self, other):
        return isinstance(other, Person) and self.address == other.address and self.name == other.name

    def __hash__(self):
        return hash((self.name, self.address))
