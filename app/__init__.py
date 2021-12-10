from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
from app.user_handler.controllers import user_handler as user_module

app.register_blueprint(user_module)
db.create_all()
