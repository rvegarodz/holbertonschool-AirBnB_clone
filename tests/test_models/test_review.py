import unittest
import io 
import unittest.mock
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.review import Review


class TestReview(unittest.TestCase):
    """Test for class User"""

    def test_place_id(self):
        """Test class attributes named email"""
        obj = Review()
        self.assertEqual(obj.place_id, "")
        obj.place_id = "gabrielitotititotitito"
        self.assertEqual(obj.place_id, "gabrielitotititotitito")

    def test_user_id(self):
        """Test class attributes named email"""
        obj = Review()
        self.assertEqual(obj.user_id, "")
        obj.user_id = "gabrielitotititotitito"
        self.assertEqual(obj.user_id, "gabrielitotititotitito")

    def test_text(self):
        """Test class attributes named email"""
        obj = Review()
        self.assertEqual(obj.text, "")
        obj.text = "gabrielitotititotitito"
        self.assertEqual(obj.text, "gabrielitotititotitito")


if __name__ == '__main__':
    unittest.main()
