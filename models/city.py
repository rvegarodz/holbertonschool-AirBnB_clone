#!/usr/bin/python3
"""
Module with Class City
"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """
    Defines class City
    """
    state_id = ""
    name = ""

