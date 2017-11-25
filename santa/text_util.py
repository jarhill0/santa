def save(solved_dict):
    for gifter, recipient in solved_dict.items():
        with open('Assignment for {}.txt'.format(gifter.name), 'w') as f:
            f.write('Your recipient is {}.\n'.format(recipient.name))
