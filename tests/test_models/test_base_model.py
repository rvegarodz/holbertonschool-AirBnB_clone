import unittest
import io 
import unittest.mock
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """
    Test Base Model class
    """

    def test_fs_all_empty(self):
        #Testing __objects dict at the beginning 
        self.assertEqual(FileStorage().all(), {})
        #Itering in __objects dict at the beginning
        for key in FileStorage().all():
            obj = all_objs[key]
            self.assertIsNone(obj)
    
    def test_fs_all(self):
        storage = FileStorage()
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
    
    def test_init(self):
        obj_1 = BaseModel()
        self.assertIsNotNone(obj_1.id)
        self.assertIsNotNone(obj_1.created_at)
        self.assertEqual(obj_1.created_at, obj_1.updated_at)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, expected_output, obj, mock_stdout):
        print(obj)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        obj = BaseModel()
        obj_str = f'[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}\n'
        self.assert_stdout(obj_str, obj)

    def test_save(self):
        obj = BaseModel()
        obj.save()
        self.assertNotEqual(obj.created_at, obj.updated_at)

    def test_to_dict(self):
        obj = BaseModel()
        a_dict = obj.to_dict()
        obj_dict = {
            'id': obj.id,
            '__class__': obj.__class__.__name__,
            'created_at': obj.created_at.isoformat(),
            'updated_at': obj.updated_at.isoformat()}
        self.assertDictEqual(a_dict, obj_dict)

if __name__ == '__main__':
    unittest.main()