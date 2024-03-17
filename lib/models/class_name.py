# lib/models/class_name.py
from models.__init__ import CONN, CURSOR
from models.teacher import Teacher
from models.student import Student
from models.student_class_name import Student_Class_Name
from models.teacher_class_name import Teacher_Class_Name

class Class_Name:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        return (
            f"Class Name {self.id}: {self.name}"
        )
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string."
            )
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Class_Name instances in the database. """
        sql = """
            CREATE TABLE IF NOT EXISTS class_names (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """ Drop the table used to persist the attributes of Class_Name instances in the database. """
        sql = """
            DROP TABLE IF EXISTS class_names
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Save the class_name to the database. """

        sql = """
            INSERT INTO class_names (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """ Update the name of the class_name in the database. """

        sql = """
            UPDATE class_names
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        """ Delete the class_name from the database. """

        sql = """
            DELETE FROM class_names
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def create(cls, name):
        """ Create a new class_name instance and save it to the database. """

        class_name = cls(name)
        class_name.save()
        return class_name
    
    @classmethod
    def instance_from_db(cls, row):
        """ Return a class_name instance from the database. """

        class_name = cls.all.get(row[0])
        if class_name:
            class_name.name = row[1]
        else:
            class_name = cls(row[1])
            class_name.id = row[0]
            cls.all[class_name.id] = class_name
        return class_name
    
    @classmethod
    def get_all(cls):
        """ Return all the class_names in the database. """

        sql = """
            SELECT * 
            FROM class_names
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """ Return the class_name with the given id. """

        sql = """
            SELECT * 
            FROM class_names 
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()

        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """ Return the class_name with the given name. """

        sql = """
            SELECT *
            FROM class_names
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()

        return cls.instance_from_db(row) if row else None
    
    def get_teachers(self):
        """ Return all the teachers for the class. """

        teacher_class_name_rows = Teacher_Class_Name.find_by_class_name_id(self.id)
        teacher_rows = [Teacher.find_by_id(row.teacher_id) for row in teacher_class_name_rows]

        return [Teacher.instance_from_db([row.id, row.name]) for row in teacher_rows]
    
    def get_students(self):
        """ Return all the students for the class. """

        student_class_name_rows = Student_Class_Name.find_by_class_name_id(self.id)
        student_rows = [Student.find_by_id(row.student_id) for row in student_class_name_rows]

        return [Student.instance_from_db([row.id, row.name]) for row in student_rows]