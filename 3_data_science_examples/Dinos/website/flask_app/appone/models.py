from appone import db
from datetime import datetime

class DinosaurDB(db.Model):
    name = db.Column(db.String, primary_key=True)
    diet = db.Column(db.String)
    lived_in = db.Column(db.String)
    type = db.Column(db.String)
    period_name = db.Column(db.String)


def __repr__(self):
    return f"DinosaurDB('{self.name}', '{self.diet}', '{self.lived_in}', '{self.type}', '{self.period_name}')"

class DinosaurSelections(db.Model):
    name = db.Column(db.String, primary_key=True)
    recommendationOne = db.Column(db.String)
    recommendationTwo = db.Column(db.String)
    recommendationThree = db.Column(db.String)
    date = db.Column(db.DateTime, default=datetime.utcnow())
    likeSelectionIndicator = db.Column(db.Boolean)


def __repr__(self):
    return f"DinosaurSelections('{self.name}', '{self.recommendationOne}', '{self.recommendationTwo}', '{self.recommendationThree}', '{self.date}', '{self.likeSelectionIndicator}')"
