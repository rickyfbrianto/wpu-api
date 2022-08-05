from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/db_tes'
    db.init_app(app)

    lm = LoginManager()
    lm.login_view = 'auth.login'
    lm.login_message = "Anda perlu login"
    lm.login_message_category = "danger"
    lm.init_app(app)

    from .view import view
    from .auth import auth
    from .model import User

    @lm.user_loader
    def load_user(id):
        return User.query.get(int(id))

    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
