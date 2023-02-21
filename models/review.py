#!/usr/bin/python3
"""Module provide Review class"""
from models.base_model import BaseModel
from models.place import Place

class Review(BaseModel):
    """Review class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = Place.id
        self.user_id = User.id
        self.text = ""
    