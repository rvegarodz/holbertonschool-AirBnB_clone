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
<<<<<<< HEAD

    def __init__(self, *args, **kwargs):
        """State instance creation"""
        super().__init__(*args, **kwargs)
        self.name = ""
=======
>>>>>>> e8cb7d56ecbb45b64324a7008bb72c27ddd10847
