#!/usr/bin/python3
"""
Module with State Class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Defines a State
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
