#!/usr/bin/python3
"""
Write a class BaseModel that defines all common
attributes/methods for other classes
"""
import uuid
from datetime import datetime
import json
from models import storage


class BaseModel:
    """Class Base Model"""
    def __init__(self, *args, **kwargs):
        """Initialization"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    date_format = "%Y-%m-%dT%H:%M:%S.%f"
                    date_time_obj = datetime.strptime(value, date_format)
                    setattr(self, key, date_time_obj)
                    continue
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        my_dict = {}

        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                my_dict[key] = value.isoformat()
                continue
            if value:
                my_dict[key] = value
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
