from prat import db

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    purchase_price = db.Column(db.Float, nullable=False)

    def __init__(self, name, purchase_price):
        self.name = name
        self.purchase_price = purchase_price

    def __repr__(self):
        return f'<Item {self.id}: {self.name}>'