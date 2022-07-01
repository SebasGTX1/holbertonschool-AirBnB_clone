#!/usr/bin/python3
"""
Write a class BaseModel that defines all common 
attributes/methods for other classes
"""

import uuid
from datetime import datetime

class BaseModel:
    """Class Base Model"""
    def __init__(self, id, created_at):
        """Initialization"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>""" 
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")