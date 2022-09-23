barbearia_projeto
======

Install
-------

Create a virtualenv and activate it::

    $ python3 -m venv venv
    $ . venv/bin/activate

Or on Windows cmd::

    $ py -3 -m venv venv
    $ venv\Scripts\activate.bat

Install admin_area::

    $ pip install -e .

Or if you are using the main branch, install Flask from source before
installing admin_area::

    $ pip install -e ../..
    $ pip install -e .


Run
---

::

    $ export FLASK_APP=barbearia_projeto
    $ export FLASK_ENV=development
    $ flask run

Or on Windows cmd::

    > set FLASK_APP=barbearia_projeto
    > set FLASK_ENV=development
    > flask run

Open http://127.0.0.1:5000 in a browser.
