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
        # I don't know if this is a valid way to hash and prevent collisions
        return hash(self.name) * hash(self.address)
