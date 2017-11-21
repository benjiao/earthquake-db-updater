# GeoAlchemy Models

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float
from geoalchemy2 import Geometry

Base = declarative_base()


class Earthquake(Base):
    __tablename__ = 'earthquake'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(Date)
    location = Column(Geometry('POINT'))

    hour = Column(Integer)
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)
    minute = Column(Integer)
    second = Column(Float)

    focal_depth = Column(Float)
    magnitude = Column(Float)
    intensity = Column(Float)

    deaths = Column(Integer)
    missing = Column(Integer)
    damage = Column(Float)
    houses_destroyed = Column(Integer)
    houses_damaged = Column(Integer)

    total_deaths = Column(Integer)
    total_missing = Column(Integer)
    total_damage = Column(Float)
    total_houses_destroyed = Column(Integer)
    total_houses_damaged = Column(Integer)
