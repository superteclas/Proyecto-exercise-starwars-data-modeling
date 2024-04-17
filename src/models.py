import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favoritesPerson = relationship('Characters_favoritos', backref='user', lazy=True)
    favorites = relationship('favorites', backref='user', lazy=True)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(String(250))
    mass = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    person_id = Column(Integer, ForeignKey('user.id'))
    person = relationship(User)

class Characters_Favoritos(Base):
    __tablename__ = 'Characters_favoritos'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    planet_id = Column(Integer, ForeignKey('characters.id'))


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    diameter = Column(String(250))
    rotation_period = Column(String(250))
    orbital_operiod = Column(String(250))
    gravity = Column(String(250))
    population = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(String(250))
    person_id = Column(Integer, ForeignKey('user.id'))
    person = relationship(User)
class PlanetFavorites(Base):
    __tablename__ = 'planet_favorites'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    

class Vehicles (Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    vehicle_class = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(String(250))
    lenght = Column(String(250))
    crew = Column(String(250))
    passengers = Column(String(250))
    max_speed = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))
    person_id = Column(Integer, ForeignKey('user.id'))
    person = relationship(User)

class VehicleFavorites(Base):
    __tablename__ = 'vehicle_favorites'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
