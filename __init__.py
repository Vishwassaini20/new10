from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz_master.db'
    app.config['SECRET_KEY'] = b'\x8f\xe0\x8d\xde\xe3k3\x7fz\x01\xf9\xb3n#\xca\xc7\xe0\x8e\xde\x0e4\xf2\x99\x01'
    db.init_app(app)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
