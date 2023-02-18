import unittest
from models.base_model import BaseModel
import io 
import unittest.mock
from datetime import datetime

from models.engine.file_storage import FileStorage


class TestBaseModel2(unittest.TestCase):
    """
    Test Base Model class
    """
    def test_storage_all(self):
        storage = FileStorage()
        all_objs = storage.all()
        #Testing __objects dict at the beginning 
        self.assertEqual(all_objs, {})
        obj1 = BaseModel()
        all_objs = storage.all()
        # Testing __objects dict after creating object
        self.assertNotEqual(all_objs, {})

    def test_storage_save(self):
        storage = FileStorage()
        all_objs1 = storage.all()
        obj2 = BaseModel()
        obj2.name = "My_First_Model"
        obj2.my_number = 89
        obj2.save()

        for key, value in all_objs1.items():
            if obj2.name in value:
                self.assertIn(obj2.name, key.values())

if __name__ == '__main__':
    unittest.main()