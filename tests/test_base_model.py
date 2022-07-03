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
        self.assertEqual(str(type(base)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(base, BaseModel)
        self.assertTrue(issubclass(type(base), BaseModel))
