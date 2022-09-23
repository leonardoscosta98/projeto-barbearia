from flask import Flask
from decouple import config
from flask_talisman import Talisman

app = Flask(__name__)

app.config.from_mapping(
        SECRET_KEY=config("SECRET_KEY"),
        # store the database in the instance folder        
        DATABASE_HOST=config("DATABASE_HOST"),
        DATABASE_NAME=config("DATABASE_NAME"),
        DATABASE_NAME_TEST=config("DATABASE_NAME_TEST", default=None),
        DATABASE_USER=config("DATABASE_USER"),
        DATABASE_PASSWORD=config("DATABASE_PASSWORD"),    
    )

from barbearia_projeto import main

app.register_blueprint(main.bp)


# def create_app(test_config=None):   
#     """Create and configure an instance of the Flask application."""
#     app = Flask(__name__, instance_relative_config=True)
#     Talisman(app, content_security_policy=None)
#     app.config.from_mapping(
#         SECRET_KEY=config("SECRET_KEY"),
#         # store the database in the instance folder        
#         DATABASE_HOST=config("DATABASE_HOST"),
#         DATABASE_NAME=config("DATABASE_NAME"),
#         DATABASE_NAME_TEST=config("DATABASE_NAME_TEST", default=None),
#         DATABASE_USER=config("DATABASE_USER"),
#         DATABASE_PASSWORD=config("DATABASE_PASSWORD"),    
#     )

#     # register the database commands
#     from barbearia_projeto import db

#     db.init_app(app)

#     from barbearia_projeto import main

#     app.register_blueprint(main.bp)

#     app.add_url_rule("/", endpoint="index")
   
   
#     return app
