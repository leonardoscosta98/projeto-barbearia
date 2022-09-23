from flask import Flask
from os import environ

def create_app(test_config=None):   
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
    app.config['DATABASE_HOST'] = environ.get('DATABASE_HOST')
    app.config['DATABASE_NAME'] = environ.get('DATABASE_NAME')
    app.config['DATABASE_USER'] = environ.get('DATABASE_USER')
    app.config['DATABASE_PASSWORD'] = environ.get('DATABASE_PASSWORD')
    
    # register the database commands
    from barbearia_projeto import db

    db.init_app(app)

    from barbearia_projeto import main

    app.register_blueprint(main.bp)

    app.add_url_rule("/", endpoint="index")
   
   
    return app

app = create_app()
