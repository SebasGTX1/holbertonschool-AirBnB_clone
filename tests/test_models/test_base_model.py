#!/usr/bin/python3
""" Test file for Base class """
import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import datetime


class BaseModelTests(unittest.TestCase):
    """ Suite of Console Tests """

    my_model = BaseModel()

    def testBaseModel1(self):
        """ Test for a BaseModel instance """

        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        self.my_model.save()
        my_model_json = self.my_model.to_dict()

        self.assertEqual(self.my_model.name, my_model_json['name'])
        self.assertEqual(self.my_model.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.my_model.id, my_model_json['id'])

    def testSave(self):
        """ Test for a BaseModel instance """
        my_m = BaseModel()
        my_m.first_name = "First"
        my_m.save()

        self.assertIsInstance(my_m.id, str)
        self.assertIsInstance(my_m.created_at, datetime.datetime)
        self.assertIsInstance(my_m.updated_at, datetime.datetime)

        first_dict = my_m.to_dict()

        my_m.first_name = "Second"
        my_m.save()
        sec_dict = my_m.to_dict()

        self.assertEqual(first_dict['created_at'], sec_dict['created_at'])
        self.assertNotEqual(first_dict['updated_at'], sec_dict['updated_at'])


if __name__ == '__main__':
    unittest.main()
