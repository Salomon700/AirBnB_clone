#!/usr/bin/python3
"""Unittests for BaseModel class"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def test_instance_attributes(self):
        """Test instance attributes"""
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_str_method(self):
        """Test __str__ method"""
        my_model = BaseModel()
        string_representation = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), string_representation)

    def test_save_method(self):
        """Test save method"""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method"""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertTrue('__class__' in my_model_dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')


if __name__ == '__main__':
    unittest.main()
