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

    def all(self):
        """ Public method to return all the objects previusly saved"""
        return FileStorage.__objects

    def new(self, obj):
        """Public method to create a new entry for the objects dict"""
        name = obj.__class__.__name__
        id_num = obj.id
        key = name + "." + id_num

        FileStorage.__objects[key] = obj

    def save(self):
        """ Public method to save an object"""
        my_json_dict = {}

        for key, value in FileStorage.__objects.items():
            my_json_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as F:
            json.dump(my_json_dict, F)

    def reload(self):
        """ Public method to reload all the objects saved"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_arb = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review}

        my_dict = {}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r",encoding='utf-8') as F:
                my_dict = json.load(F)
        for key, value in my_dict.items():
            my_dict[key] = class_arb[value["__class__"]](**value)
        FileStorage.__objects = my_dict

    def class_arb(self):
        """Returns a dictionary with the classes"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_arb = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review}
        return class_arb
