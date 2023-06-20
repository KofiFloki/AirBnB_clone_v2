#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity

class Amenity(BaseModel, Base):
    """defines the class amenity"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"

        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity,
                                       back_populates="amenities")

    else:
        name = ""
