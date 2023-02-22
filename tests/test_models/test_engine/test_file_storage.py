import unittest
from models.base_model import BaseModel
import io 
import unittest.mock
from datetime import datetime
import os

from models.engine.file_storage import FileStorage


class TestBaseModel2(unittest.TestCase):
    """
    Test Base Model class
    """
            
    def test_all(self):
        storage = FileStorage()
        all_objs = storage.all()
        #Testing __objects dict at the beginning 
        self.assertEqual(all_objs, {})
        storage = FileStorage()
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj1.save()
        obj2.save()
        all_objects_reloaded = storage.reload()
        #Testing __objects dict at the beginning 
        self.assertNotEqual(all_objects_reloaded, all_objs)


    def test_new(self):
        storage = FileStorage()
        obj1 = BaseModel()
        storage.new(obj1)
        obj_name = f'BaseModel.{obj1.id}'
        var = storage.all()[obj_name]
        self.assertEqual(obj1, var)

    def test_save(self):
        storage = FileStorage()
        all_objs1 = storage.all()
        obj2 = BaseModel()
        obj2.name = "My_First_Model"
        obj2.my_number = 89
        obj2.save()
        for key, value in all_objs1.items():
            if obj2.name == value:
                self.assertIn(obj2.name, key.values())

    def test_reload(self):
        """Doc reload test"""
        storage = FileStorage()
        all_objs = storage.all()
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj1.save()
        obj2.save()
        all_objects_reloaded = storage.reload()
        #Testing __objects dict at the beginning 
        self.assertNotEqual(all_objects_reloaded, all_objs)
    

if __name__ == '__main__':
    unittest.main()