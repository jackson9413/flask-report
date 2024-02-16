from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expensesDB.db'
app.config['SECRET_KEY'] = '5a4f1a6f6a6f1a6f1a6f1a6f'

db = SQLAlchemy(app)

app.app_context().push() 
from application import routes