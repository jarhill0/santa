Santa
=====

A Python 3 project to randomly pair Secret Santa gifters and recipients, following a set of constraints, and email
them, all without the operator seeing the assignments.

Requirements
------------

- yagmail

Installation
------------

Install with ``pip3 install santa`` or ``python3 -m pip install santa``. Preceded either command with ``sudo`` if it
fails due to insufficient permissions.

Usage
-----

1. Create `Person` objects for all participants with their names and addresses:

.. code-block:: python

    import santa

    john = santa.Person('John Doe', 'jdoe@example.com')
    sally = santa.Person('Sally Salamander', 'sally@mander.com')
    linus = santa.Person('Linus Torvalds', 'torvalds@transmeta.com')
    guido = santa.Person('Guido van Rossum', 'guido@python.org')

2. Put them into a list:

.. code-block:: python

    people = [john, sally, linus, guido]

3. If any participants have restrictions on who they can give to (say, John and Sally are married and will be getting
   each other gifts regardless), create a dictionary with the giver as the key and the banned recipients in a list as the 
   value:
 
.. code-block:: python

    # not only are John and Sally married, but Sally hates Linus and will not get him a gift.
    restrictions = {john: [sally],
                    sally: [john, linus]}

4. Pass these into the function ``santa.run(person_list, invalid_links=None, *, message='', subject='Secret Santa')``. 
   This will match people and send emails. If a match is not found, the program will raise ``santa.SolvingError``. If you
   haven't already `configured yagmail <https://github.com/kootenpv/yagmail/blob/master/README.md#username-and-password>`_, it
   will prompt you for a username and password.

.. code-block:: python

    santa.run(people, restrictions, message='Thank you for participating.')

5. If there are any errors sending emails, they will be printed to the console in the form of a list of tuples of ``(gifter, recipient)``. You, the operator, must decide how to handle this.
