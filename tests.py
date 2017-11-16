import santa

john = santa.Person('John Doe', 'jdoe@example.com')
sally = santa.Person('Sally Salamander', 'sally@example.com')
linus = santa.Person('Linus Torvalds', 'torvalds@example.com')
guido = santa.Person('Guido van Rossum', 'guido@example.org')


def test_personhood():
    names = ('John Doe', 'Sally Salamander', 'Linus Torvalds', 'Guido van Rossum')
    addresses = ('jdoe@example.com', 'sally@example.com', 'torvalds@example.com', 'guido@example.org')
    people = [john, sally, linus, guido]
    for name, address, person in zip(names, addresses, people):
        assert name == person.name
        assert address == person.address


def test_equality():
    other_john = santa.Person('John Doe', 'jdoe@example.com')
    lowercase_john = santa.Person('john doe', 'jdoe@example.com')

    assert john == other_john
    assert john != sally
    assert john != lowercase_john


def test_dictize():
    people = [john, sally, linus, guido]
    expected = {john: sally, sally: linus, linus: guido, guido: john}

    assert expected == santa.solver.dictize(people)


def test_validation():
    restrictions = {john: [sally, guido], sally: [john]}
    sol1 = {john: sally, sally: linus, linus: guido, guido: john}
    sol2 = {john: linus, sally: guido, guido: john, linus: sally}

    assert not santa.solver.is_valid(sol1, restrictions)
    assert santa.solver.is_valid(sol2, restrictions)


def test_solving():
    restrictions = {john: [sally, guido], sally: [john]}
    people = [john, sally, linus, guido]

    try:
        santa.solver.solve(people, restrictions)
    except santa.SolvingError:
        assert False
    else:
        assert True

    restrictions = {john: [sally, guido, linus]}

    try:
        santa.solver.solve(people, restrictions)
    except santa.SolvingError:
        assert True
    else:
        assert False
