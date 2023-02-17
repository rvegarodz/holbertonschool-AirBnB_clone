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

    def __init__(self, *args, **kwargs):
        """
        Initialize instance attributes
            Attrs:
                id (str): instance identity
                created_at: date of instance creation
                updated_at: date of instance attrs change
        """
        if kwargs:
            for keys in kwargs:
                if keys != __class__:
                    self.__dict__[keys] = kwargs[keys]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        Returns string representation of instance
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """
        Changes the time of instance attrs change
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance including new attrs
        """
        obj_dict = {}
        obj_dict['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = (datetime.isoformat(
                                        self.__dict__.get('created_at')))
        self.__dict__['updated_at'] = (datetime.isoformat(
                                        self.__dict__.get('updated_at')))
        self.__dict__.update(obj_dict)
        return self.__dict__

