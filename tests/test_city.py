#!/usr/bin/python3
""" Test file for User class """

import unittest

from numpy import place
from models.base_model import BaseModel
from models.city import City
from models import storage
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
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

    def test_city_instantiation(self):
        """City instance attributes"""
        city = City()
        self.assertEqual(str(type(city)), "<class 'models.city.City'>")
        self.assertIsInstance(city, City)
        self.assertTrue(issubclass(type(city), BaseModel))
