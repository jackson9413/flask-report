from application import db
from application import app
from datetime import datetime

class IncomeExpenses(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.String(30), default = "income", nullable = False)
    category = db.Column(db.String(30), nullable = False, default = "rent")
    date = db.Column(db.Date, nullable = False, default = datetime.utcnow)
    amount = db.Column(db.Integer, nullable = False)  
    
    def __str__(self):
        return self.id 
    
# Creation of the database tables within the application context.
with app.app_context():
    db.create_all()
    