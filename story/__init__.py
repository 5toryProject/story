from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    migrate = Migrate()


    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///story.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    migrate.init_app(app, db)

    @app.route('/')
    def index():
        return "flaks team project"

    return app