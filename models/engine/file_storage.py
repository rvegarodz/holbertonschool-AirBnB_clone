#!/usr/bin/python3
"""COMMENT"""

import json
from os import path
from models.base_model import BaseModel


class FileStorage:
    """Class that serializes and deserializes"""
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return self.__objects

    def new(self, obj):
        key_nm = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key_nm] = obj

    def save(self):
        with open(self.__file_path, "w+", encoding='utf-8') as file:
            for k, v in self.__objects.items():
                self.__objects[k] = v.to_dict()
            json.dump(self.__objects, file)

    def reload(self):
        try:
            with open(self.__file_path, encoding='utf-8') as file:
                    for k, v in json.load(file).items():
                        self.__objects[k] = BaseModel(**v)
        except Exception:
            pass