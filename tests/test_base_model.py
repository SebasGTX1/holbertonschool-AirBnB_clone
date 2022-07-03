#!/usr/bin/python3
""" Test file for Base class """
import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class BaseTests(unittest.TestCase):
    """ Suite to test Base class """
    
    def setUp(self):
        """Set Up for test"""
        pass
