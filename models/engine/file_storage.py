#!/usr/bin/python3
"""
Write a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances
"""
import json
import os


class FileStorage:
    """ FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def __init__(self, *args, **kwargs):
        """ Constructor method """

    def all(self):
        """ Public method to return all the objects previusly saved"""
        return FileStorage.__objects

    def new(self, obj):
        """Public method to create a new entry for the objects dict"""
        name = obj.__class__.__name__
        id_num = obj.id

        FileStorage.__objects[f"{name}.{id}"] = obj

    def save(self):
        """ Public method to save an object"""
        my_json_dict = {}

        for key, value in FileStorage.__objects.items():
            my_json_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as F:
            json.dump(my_json_dict, F)

    def reload(self):
        """ Public method to reload all the objects saved"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding='utf-8') as F:
                FileStorage.__objects = json.loads(F.read())
