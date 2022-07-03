#!/usr/bin/python3
""" Test file for User class """

import unittest

from numpy import place
from models.base_model import BaseModel
from models.place import Place
from models import storage
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):
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

    def test_place_instantiation(self):
        """Place instance attributes"""
        place = Place()
        self.assertEqual(str(type(place)), "<class 'models.place.Place'>")
        self.assertIsInstance(place, Place)
        self.assertTrue(issubclass(type(place), BaseModel))
