PyAztro 
============

PyAztro is a client library for `aztro <https://github.com/sameerkumar18/aztro>`_ written in Python.

aztro provides horoscope info for sun signs such as Lucky Number, Lucky Color, Mood, Color, Compatibility with other sun signs, description of a sign for that day etc.

Documentation for aztro API is available `here <https://aztro.sameerkumar.website>`_, documentation for PyAztro is under development.

|downloads|  |GitHub make-a-pull-requests|  |Maintenance yes|

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
|say thanks|

Donate
---------------
|Paypal|


.. |downloads| image:: https://pepy.tech/badge/pyaztro
    :target: https://pepy.tech/project/pyaztro

.. |GitHub make-a-pull-requests| image:: https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square
   :target: http://makeapullrequest.com

.. |say thanks| image:: https://img.shields.io/badge/say-thanks-ff69b4.svg
   :target: https://saythanks.io/to/sameerkumar18
   
.. |Maintenance yes| image:: https://img.shields.io/badge/Maintained%3F-yes-green.svg
   :target: https://gitHub.com/sameerkumar18/pyaztro

.. |Paypal| image:: https://img.shields.io/badge/Paypal-Donate-blue.svg
   :target: https://www.paypal.me/sameerkumar18
