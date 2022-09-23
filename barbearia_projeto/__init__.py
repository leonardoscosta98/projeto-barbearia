from flask import Flask
from decouple import config

def create_app(test_config=None):   
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=config("SECRET_KEY"),
        # store the database in the instance folder        
        DATABASE_HOST=config("DATABASE_HOST"),
        DATABASE_NAME=config("DATABASE_NAME"),
        DATABASE_USER=config("DATABASE_USER"),
        DATABASE_PASSWORD=config("DATABASE_PASSWORD"),    
    )

    # register the database commands
    from barbearia_projeto import db

    db.init_app(app)

    from barbearia_projeto import main

    app.register_blueprint(main.bp)

    app.add_url_rule("/", endpoint="index")
   
   
    return app

app = create_app()
