import random
import time

TIMEOUT = 0.2


def solve(people, invalid_links):
    """Determine who gives to whom. `people`: a list of Person objects. `invalid_links`: a dict that defines who
    can't give to whom. Returns a dict. Raises SolvingError if it cannot solve."""
    start_time = time.time()
    random.shuffle(people)
    while not is_valid(dictize(people), invalid_links):
        random.shuffle(people)
        if start_time + TIMEOUT < time.time():
            raise SolvingError('Could not solve.')
    return dictize(people)


def is_valid(people_dict, invalid_links):
    for gifter, giftee in people_dict.items():
        if giftee in invalid_links.get(gifter, ()):
            return False
    return True


def dictize(people_list):
    people = {}
    last_person = people_list[-1]
    for this_person in people_list:
        people[last_person] = this_person
        last_person = this_person
    return people


class SolvingError(Exception):
    pass
