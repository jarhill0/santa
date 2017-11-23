from .email_util import send_interface
from .person import Person
from .solver import solve


def run(person_list, invalid_links=None, *, message='', subject='Secret Santa', username=None, password=None):
    """Solve and email gifters. Raises SolvingError if it cannot solve."""
    if invalid_links is None:
        invalid_links = dict()
    if not isinstance(person_list, list):
        raise ValueError('person_list must be a list')
    if not isinstance(invalid_links, dict):
        raise ValueError('invalid_links must be a dict')
    if not all(isinstance(p, Person) for p in person_list):
        raise ValueError('Every item in person_list must be a Person')

    solved = solve(person_list, invalid_links)  # solve
    failed = send_interface(solved, message, subject, username, password)  # send emails (errors are returned)

    if failed:
        print('{} failures: {}'.format(len(failed), failed))
