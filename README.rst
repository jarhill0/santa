Santa
=====

A Python 3 project to randomly pair Secret Santa gifters and recipients, following a set of constraints, and email
them, all without the operator seeing the assignments.

Requirements
------------

- yagmail

Installation
------------

Install with ``pip3 install santa`` or ``python3 -m pip install santa``. Precede either command with ``sudo`` if it
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
   This will match people and send emails. If a match is not found, the program will raise ``santa.SolvingError``. If
   you haven't already `configured yagmail <https://github.com/kootenpv/yagmail/blob/master/README
   .md#username-and-password>`_, it will prompt you for a username and password.

.. code-block:: python

    santa.run(people, restrictions, message='Thank you for participating.')

5. If there are any errors sending emails, they will be printed to the console in the form of a list of tuples of
   ``(gifter, recipient)``. You, the operator, must decide how to handle this.

Options
-------

By default, santa will solve using the ``'loop'`` strategy, which results in a "gifting loop." As of version 0.2,
santa can also solve with the method ``'draw'``, which simulates drawing tickets from a hat. This method will not
necessarily result in a loop, but it will be possible for "pairs" of two gifters giving to each other to occur.

To set a solving mode, pass it into ``santa.run()`` like so:

.. code-block:: python

    santa.run(people, restrictions, solve_mode='loop')

The current list of solving modes is as follows:

- ``'loop'`` (default)
- ``'draw'``

Santa also has options for output modes. By default, it will email recipients. But as of version 0.2, it also has the
option to save output to text files in the current working directory. These can be attached to emails and sent
without the operator having to find out who is assigned to whom.

To set an output mode, pass it into ``santa.run()`` like so:

.. code-block:: python

    santa.run(people, restrictions, out_mode='text')

The current list of output modes is as follows:

- ``'email'`` (default)
- ``'text'``
