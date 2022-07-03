#!/usr/bin/python3
""" Test file for User class """

import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
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

    def test_user_instantiation(self):
        """User instance attributes"""
        user = User()
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")
        self.assertIsInstance(user, User)
        self.assertTrue(issubclass(type(user), BaseModel))
