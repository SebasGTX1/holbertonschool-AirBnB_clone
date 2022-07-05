#!/usr/bin/python3
""" Test file for Base class """
import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class BaseTests(unittest.TestCase):
    """ Suite to test Base class """

    def setUp(self):
        """
        the setUp() method raises an exception
        while the test is running
        """
        pass

    def tearDown(self):
        """
        a tearDown() method that tidies up after
        the test method has been run
        """
        pass

    def test_instantiation(self):
        """BaseModel instance attributes"""
        base = BaseModel()
        s = "<class 'models.base_model.BaseModel'>"
        self.assertEqual(str(type(base)), s)
        self.assertIsInstance(base, BaseModel)
        self.assertTrue(issubclass(type(base), BaseModel))

    def test_instantiation_2(self):
        """BaseModel instance attributes **kwards"""
        base = BaseModel()
        base.name = "Holberton"
        base.my_number = 89
        base_dict = base.to_dict()
        base_dict = BaseModel(**base_dict)
        self.assertEqual(base_dict.to_dict(), base.to_dict())


if __name__ == '__main__':
    unittest.main()
