from .email_util import send_interface
from .person import Person
from .solver import loop, draw
from .text_util import save


def run(person_list, invalid_links=None, **kwargs):
    """Solve and output. Raises SolvingError if it cannot solve."""
    if invalid_links is None:
        invalid_links = dict()
    if not isinstance(person_list, list):
        raise ValueError('person_list must be a list')
    if not isinstance(invalid_links, dict):
        raise ValueError('invalid_links must be a dict')
    if not all(isinstance(p, Person) for p in person_list):
        raise ValueError('Every item in person_list must be a Person')

    message = kwargs.get('message', '')
    subject = kwargs.get('subject', 'Secret Santa')
    username = kwargs.get('username', None)
    password = kwargs.get('password', None)
    out_mode = kwargs.get('out_mode', 'email').lower()
    solve_mode = kwargs.get('solve_mode', 'loop').lower()

    # solve
    if solve_mode == 'loop':
        solved = loop(person_list, invalid_links)
    elif solve_mode == 'draw':
        solved = draw(person_list, invalid_links)
    else:
        raise ValueError('Unknown solve mode "{}"'.format(solve_mode))

    # output
    if out_mode == 'email':
        failed = send_interface(solved, message, subject, username, password)  # send emails (errors are returned)
        if failed:
            print('{} failures: {}'.format(len(failed), failed))
    elif out_mode == 'text':
        save(solved)
    else:
        raise ValueError('Unknown output mode "{}"'.format(out_mode))
