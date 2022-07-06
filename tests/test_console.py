#!/usr/bin/python3
"""Test Module for HBNBCommand class."""
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import unittest
import datetime
from unittest.mock import patch
import os
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    """Tests for HBNBCommand console"""

    def setUp(self):
        """Sets up test cases."""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        self.resetStorage()

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_help_console(self):
        """Tests the help command."""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        s = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

"""
        self.assertEqual(s, f.getvalue())

    def test_help_EOF(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
        s = 'Type EOF to exit the command interpreter\n'
        self.assertEqual(s, f.getvalue())

    def test_help_quit(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        s = 'Type quit to exit the command interpreter\n'
        self.assertEqual(s, f.getvalue())

    def test_help_create(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        s = 'Creates a new Instance\n'
        self.assertEqual(s, f.getvalue())

    def test_help_show(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        s = "Prints the string representation of an instance base " + \
            "on\n        the class name and id\n        \n"
        self.assertEqual(s, f.getvalue())

    def test_help_destroy(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
        s = "Deletes an instance based on the class name and " + \
            "id\n        Exmaple: (hbnb) destroy User a8d30b54-af4d-" + \
            "401e-ba78-4c11c8294264\n        \n"
        self.assertEqual(s, f.getvalue())

    def test_help_all(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
        s = "Prints all string representation of " + \
            "all instances\n        based or not on the class name\n        \n"
        self.assertEqual(s, f.getvalue())

    def test_help_count(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
        s = "Method to count instances\n"
        self.assertEqual(s, f.getvalue())

    def test_help_update(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
        s1 = 'Updates an instance based on the class name\n        '

        s2 = 'and id by adding or updating attribute\n        \n'
        s = s1 + s2
        self.assertEqual(s, f.getvalue())

    def test_emptyline(self):
        """Tests emptyline functionality."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        s = ""
        self.assertEqual(s, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("                  \n")
        s = ""
        self.assertEqual(s, f.getvalue())

    def test_do_quit(self):
        """Tests quit commmand."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

    def test_do_EOF(self):
        """Tests EOF commmand."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

    def test_do_create(self):
        """Tests create for all classes."""
        for class_name in self.classes():
            self.help_test_do_create(class_name)

    def help_test_do_create(self, class_name):
        """Helper method to test the create commmand."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(class_name))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)
        key = "{}.{}".format(class_name, uid)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all {}".format(class_name))
        self.assertTrue(uid in f.getvalue())

if __name__ == "__main__":
    unittest.main()
