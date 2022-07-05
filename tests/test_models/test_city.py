#!/usr/bin/python3
""" Test file for User class """
import unittest
from numpy import place
from models.base_model import BaseModel
from models.city import City
from models import storage
from models.engine.file_storage import FileStorage
import datetime


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

    def test_cityAttributes(self):
        """Test Attributes exist"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))

    def test_city_types(self):
        """City correct attributes' types"""
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime.datetime)
        self.assertIsInstance(city.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
