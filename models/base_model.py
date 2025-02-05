#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import models

time = "%Y-%m-%dT%H:%M:%S.%f"
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if kwargs.get("created_at"):
                kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.created_at = datetime.now()
        if kwargs.get("created_at"):
            kwargs["updated_at"] = datetime.strptime(
                kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.updated_at = datetime.now()
        for key, val in kwargs.items():
            if "__class__" not in key:
                setattr(self, key, val)
        if not self.id:
            self.id = str(uuid.uuid4())

    def __str__(self):
        """Returns a string representation of the instance"""

        return ('[{}] ({}) {}'.format(self.__class__.__name__, self.id,
                                     self.__dict__))

    def __repr__(self):
        """returns a string representation of the instance"""
        return ('[{}] ({}) {}'.format(self.__class__.__name__, self.id,
                            self.__dict__))

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        cp_dct = dict(self.__dict__)
        cp_dct['__class__'] = self.__class__.__name__
        cp_dct['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        cp_dct['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        if hasattr(self, "_sa_instance_state"):
            del cp_dct["_sa_instance_state"]
        return (cp_dct)

    def delete(self):
        from models import storage
        """Deletes the current instance from the storage"""
        storage.delete(self)
