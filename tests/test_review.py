#!/usr/bin/python3
""" Test file for User class """

import unittest
from models.base_model import BaseModel
from models.review import Review
from models import storage
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
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

    def test_review_instantiation(self):
        """Review instance attributes"""
        review = Review()
        self.assertEqual(str(type(review)), "<class 'models.review.Review'>")
        self.assertIsInstance(review, Review)
        self.assertTrue(issubclass(type(review), BaseModel))
