#!/usr/bin/python3
"""
BaseModel class module
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Defines all common attributes/methods
    for other classes
    """

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = {}
        obj_dict['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = (datetime.isoformat(
                                        self.__dict__.get('created_at')))
        self.__dict__['updated_at'] = (datetime.isoformat(
                                        self.__dict__.get('updated_at')))
        self.__dict__.update(obj_dict)
        return self.__dict__
