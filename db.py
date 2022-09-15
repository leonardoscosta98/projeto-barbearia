import psycopg2

import click
from flask import g, current_app
from flask.cli import with_appcontext

def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    if "db" not in g:   
      g.db = psycopg2.connect(
                  port=5432,
                  host='ec2-44-193-178-122.compute-1.amazonaws.com',
                  database='d4aj93bmc9lc86',
                  user='xtovtbsiqlzhxn',
                  password='4dba616192b60af529bbeac82113cc2bd5dae8a7b8c670544ef4f45a6a1becbd'
            )

    return g.db


def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    db = g.pop("db", None)

    if db is not None:
        db.close()



def init_db():
    """Clear existing data and create new tables."""
    get_db()    


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)    


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def execQuery(sql, first=False, onlyExec=False):
    db = get_db()

    with db.cursor() as cursor: 
        try:
            cursor.execute(sql)
        except:
            cursor.execute("rollback")
            cursor.execute(sql)
    
        if onlyExec == True:
            db.commit()
            return None

        row = dictfetchall(cursor)

        if first == True:
            if len(row) > 0:
                row = row[0]
            elif len(row) == 0:
                row = None

    return row