#!/user/bin/python3
"""Place Class"""

from models.base_model import BaseModel

class Place(BaseModel):
    """Palce Class"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = 0
    price_by_night = 0
    latitude = 0
    longitude = 0
    amenity_ids = []
