#!/usr/bin/python3
""" Test file for User class """

import unittest

from numpy import place
from models import amenity
from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage
from models.engine.file_storage import FileStorage
import datetime


class TestAmenity(unittest.TestCase):
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

    def test_amenity_instantiation(self):
        """Amenity instance attributes"""
        amenity = Amenity()
        self.assertEqual(str(type(amenity)), "<class 'models.amenity.BaseModel'>")
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(issubclass(type(amenity), BaseModel))

    def test_amenity_Attributes(self):
        """Test Attributes exist"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))

    def test_amenity_types(self):
        """Amenity correct attributes' types"""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime.datetime)
        self.assertIsInstance(amenity.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
