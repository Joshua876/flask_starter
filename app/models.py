from . import db

class propertyDetails(db.Model):
    
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String())
    description=db.Column(db.String())
    bedrooms=db.Column(db.String())
    bathrooms=db.Column(db.String())
    price=db.Column(db.String())
    prop_type=db.Column(db.String())
    location=db.Column(db.String())
    photo=db.Column(db.String())