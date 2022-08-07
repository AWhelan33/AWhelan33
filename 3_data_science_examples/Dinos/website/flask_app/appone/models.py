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
    id = db.Column(db.Integer, primary_key=True)
    reccommendations = db.Column(db.String)
    date = db.Column(db.DateTime, default=datetime.utcnow())


def __repr__(self):
    return f"DinosaurSelections('{self.id}', '{self.reccommendations}', '{self.date}'"


class DinosaurLiked(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    likedDinosaur = db.Column(db.String)


def __repr__(self):
    return f"DinosaurLiked('{self.likedDinosaur}'"
