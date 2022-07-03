#!/usr/bin/python3
""" Test file for User class """

import unittest
from models.base_model import BaseModel
from models.state import State
from models import storage
from models.engine.file_storage import FileStorage
import datetime


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

    def test_state_Attributes(self):
        """State Attributes exist"""
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))

    def test_state_types(self):
        """State correct attributes' types"""
        state = State()
        self.assertIsInstance(state.name, str)
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime.datetime)
        self.assertIsInstance(state.updated_at, datetime.datetime)
