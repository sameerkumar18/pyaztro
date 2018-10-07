PyAztro
============

PyAztro is a client library for `aztro <https://github.com/sameerkumar18/aztro>`_ written in Python.

aztro provides horoscope info for sun signs such as Lucky Number, Lucky Color, Mood, Color, Compatibility with other sun signs, description of a sign for that day etc.

Documentation for aztro API is available `here <https://aztro.sameerkumar.website>`_, documentation for PyAztro is under development.

Requirements
---------------

* Python 3+ (Recommended)
* The ``requests`` and ``dateutils`` library. `pip` should handle this for you when installing pyaztro.

Installation
---------------
::

    pip install pyaztro

Example Usage
------------------
::

    >>> import pyaztro
    >>> horoscope = pyaztro.Aztro(sign='aries')
    >>> horoscope.description
    'Diligent'

Support
----------
If you encounter any bugs, please let me know by `creating an issue <https://github.com/sameerkumar18/pyaztro/issues/new>`_ or tweeting at me `@sameer_kumar018 <https://www.twitter.com/sameer_kumar018>`_.

Contributing
---------------
Please see the repository's `CONTRIBUTING` file.

Say Thanks
---------------
`Say Thanks <https://saythanks.io/to/sameerkumar18>`_

Donate
---------------
`Paypal <https://www.paypal.me/sameerkumar18>`_