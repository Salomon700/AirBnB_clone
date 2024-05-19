#!/usr/bin/python3
"""Defines the BaseModel class."""

import uuid
from datetime import datetime


class BaseModel:
    """Defines the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return the string representation"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ 'updated_at' with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing all keys/values of the instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
