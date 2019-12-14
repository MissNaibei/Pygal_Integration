from app import db


class Inventories (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    type = db.Column(db.String, unique=False, nullable=False)
    buying_price = db.Column(db.Integer(100), unique=False, nullable=False)
    selling_price = db.Column(db.Integer(100), unique=False, nullable=False)
    stock = db.Column(db.Integer(100), unique=False, nullable=False)