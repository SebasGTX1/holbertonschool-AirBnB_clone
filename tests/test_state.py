#!/usr/bin/python3
""" Test file for User class """

import unittest
from models.base_model import BaseModel
from models.state import State
from models import storage
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
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

    def test_state_instantiation(self):
        """State instance attributes"""
        state = State()
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")
        self.assertIsInstance(state, State)
        self.assertTrue(issubclass(type(state), BaseModel))
