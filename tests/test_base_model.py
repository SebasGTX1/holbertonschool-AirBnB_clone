#!/usr/bin/python3
""" Test file for Base class """
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import json
from unittest.mock import patch


class BaseTests(unittest.TestCase):
    """ Suite to test Base class """
    
