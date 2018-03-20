to run locally, in one terminal window run:

    $ rethinkdb --bind all

then cd into CleanEugene-api in another terminal window:
    $ gunicorn --bind 0.0.0.0:8000 app:api