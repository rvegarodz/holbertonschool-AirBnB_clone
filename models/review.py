#!/usr/bin/python3
"""Module provide User class"""
from models.base_model import BaseModel
from models.place import Place

class User(BaseModel):
    """User class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
