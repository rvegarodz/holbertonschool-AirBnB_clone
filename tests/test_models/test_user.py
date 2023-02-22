import unittest
import io 
import unittest.mock
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


class TestUser(unittest.TestCase):
    """Test for class User"""

    def test_email(self):
        """Test class attributes named email"""
        obj = User()
        self.assertEqual(obj.email, "")
        obj.email = "gabrielitotititotitito"
        self.assertEqual(obj.email, "gabrielitotititotitito")

    def test_password(self):
        """Test class attributes named email"""
        obj = User()
        self.assertEqual(obj.password, "")
        obj.password = "gabrielitotititotitito"
        self.assertEqual(obj.password, "gabrielitotititotitito")

    def test_first_name(self):
        """Test class attributes named email"""
        obj = User()
        self.assertEqual(obj.first_name, "")
        obj.first_name = "gabrielitotititotitito"
        self.assertEqual(obj.first_name, "gabrielitotititotitito")

    def test_email(self):
        """Test class attributes named email"""
        obj = User()
        self.assertEqual(obj.last_name, "")
        obj.last_name = "gabrielitotititotitito"
        self.assertEqual(obj.last_name, "gabrielitotititotitito")


if __name__ == '__main__':
    unittest.main()