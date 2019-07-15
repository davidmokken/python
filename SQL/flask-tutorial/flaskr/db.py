import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    # g is a special object that is unique for each request. 
    # It is used to store data that might be accessed by multiple functions during the request. 
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            dtect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

