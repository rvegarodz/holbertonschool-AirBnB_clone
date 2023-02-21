#!/usr/bin/python3
"""Module provide User class"""
from models.base_model import BaseModel

class User(BaseModel):
    """User class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""


    def __init__(self, *args, **kwargs):
        """Review instance creation"""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
