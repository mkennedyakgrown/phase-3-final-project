# lib/models/teacher.py
from models.__init__ import CONN, CURSOR

class Teacher:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, classes, id=None):
        self.name = name
        self.classes = classes
        self.id = id
