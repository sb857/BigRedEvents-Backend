from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, Unicode
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()

class Building(db.Model):
    __tablename__ = "building"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)

    def __init__(self, **kwargs):
        """
        Initializes Building object
        """
        self.name = kwargs.get('name', '')

    def serialize(self):
        """
        Returns a dicitonary the contents of a Building object
        """
        return {
        'id': self.id,
        'name' :self.name,
        }


class Host(db.Model):
    __tablename__ = "host"
    id = db.Column(db.Integer, primary_key = True)
    Pno = db.Column(db.BigInteger)
    name  = db.Column(db.String, nullable = False)
    def __init__(self, **kwargs):
        """
        Initializes Host object
        """
        self.name = kwargs.get('name', '')
        self.Pno = kwargs.get('Pno','N/A')

    def serialize(self):
        """
        Returns a dicitonary the contents of a Building object
        """
        return {
            'id': self.id,
            'name': self.name,
            'Pno':self.Pno
        }


class Event(db.Model):
    __tablename__ = "event"
    id = db.Column(db.Integer, primary_key = "true")
    name  = db.Column(db.String ,nullable = False)
    date = db.Column(db.String, nullable = False)
    time = db.Column(db.String, nullable = False)
    tags = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)
    organizerName = db.Column(db.String, nullable = False)
    organizerContact = db.Column(db.String, nullable = False)
    dorm_id = db.Column(db.String, ForeignKey(Building.id))

    def __init__(self, **kwargs):
        """
        Initializes an Event object
        """
        self.name = kwargs.get('name','')
        self.date = kwargs.get('date', '')
        self.time = kwargs.get('time', '')
        self.tags = kwargs.get('tags', '')
        self.description = kwargs.get('description')
        self.organizerName = kwargs.get('organizerName','')
        self.organizerContact = kwargs.get('organizerContact','')
        self.dorm_id = kwargs.get('dorm_id')

    def serialize(self):
        """
        Returns a dicitonary the contents of an event object
        """
        s = {"1" : "Court Kay Bauer", "2" : "Mary Donlon", "3" : "Low Rise 7",
        "4": "High Rise 5", "5": "Clara Dickson Hall"}
        return {
            'id': self.id,
            'name':self.name,
            'date': self.date,
            'time': self.time,
            'tags':self.tags,
            'description': self.description,
            'organizerName':self.organizerName,
            'organizerContact':self.organizerContact,
            'dorm_id': s[self.dorm_id]
        }
