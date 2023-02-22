import unittest
import io 
import unittest.mock
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity


class TestUser(unittest.TestCase):
    """Test for class User"""

    def test_name(self):
        """Test class attributes named email"""
        obj = Amenity()
        self.assertEqual(obj.name, "")
        obj.name = "gabrielitotititotitito"
        self.assertEqual(obj.name, "gabrielitotititotitito")


if __name__ == '__main__':
    unittest.main()