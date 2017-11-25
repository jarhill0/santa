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


def test_loop():
    restrictions = {john: [sally, guido], sally: [john]}
    people = [john, sally, linus, guido]

    try:
        santa.solver.loop(people, restrictions)
    except santa.SolvingError:
        assert False
    else:
        assert True

    restrictions = {john: [sally, guido, linus]}

    try:
        santa.solver.loop(people, restrictions)
    except santa.SolvingError:
        assert True
    else:
        assert False


def test_draw():
    def validate_solution(gifters, restr):
        for gifter, recipient in gifters.items():
            if recipient in restr.get(gifter, []):
                return False
        return True

    restrictions = {john: [sally], sally: [guido], guido: [linus], linus: [john]}  # last year's pairings
    people = [john, sally, linus, guido]

    for _ in range(10):
        try:
            solved = santa.solver.draw(people)
        except santa.SolvingError:
            assert False
        else:
            assert validate_solution(solved, dict())

    for _ in range(10):
        try:
            solved = santa.solver.draw(people, restrictions)
        except santa.SolvingError:
            assert False
        else:
            assert validate_solution(solved, restrictions)

    restrictions = {john: [sally, linus, guido]}

    for _ in range(3):
        try:
            santa.solver.draw(people, restrictions)
        except santa.SolvingError:
            assert True
        else:
            assert False
