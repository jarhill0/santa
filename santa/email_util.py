import yagmail

yag = yagmail.SMTP()


def _send(address, gifter_name, giftee_name, message, subject):
    """Format and send a message to alert a participant about their assigned recipient."""
    body = 'Hi {},\n\n'.format(gifter_name) + message.strip() + '\n\nYour assigned recipient is {}.'.format(giftee_name)
    yag.send(to=address, subject=subject, contents=body)


def send_interface(solved_dict, message, subject):
    failed = []
    for gifter, recipient in solved_dict.items():
        add = gifter.address
        g_name = gifter.name
        r_name = recipient.name
        try:
            _send(add, g_name, r_name, message, subject)
        except Exception:
            failed.append((gifter, recipient))
    return failed
