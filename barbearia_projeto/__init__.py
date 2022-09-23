from flask import Flask
from os import environ

def create_app(test_config=None):   
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
    
    # register the database commands
    from barbearia_projeto import db

    # db.init_app(app)

    from barbearia_projeto import main, admin

    app.register_blueprint(main.bp)
    app.register_blueprint(admin.bp)

    app.add_url_rule("/", endpoint="index")
   
   
    return app

app = create_app()
