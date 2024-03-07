# lib/models/teacher_class_name.py
from models.__init__ import CONN, CURSOR
from models.teacher import Teacher
from models.class_name import Class_Name

class Teacher_Class_Name:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, class_name_id, teacher_id, id=None):
        self.class_name_id = class_name_id
        self.teacher_id = teacher_id
        self.id = id

    def __repr__(self):
        return (
            f"Teacher_Class_Name {self.id}: {self.class_name_id} {self.teacher_id}"
        )
    
    @property
    def class_name_id(self):
        return self._class_name_id
    
    @class_name_id.setter
    def class_name_id(self, class_name_id):
        if isinstance(class_name_id, int) and Class_Name.all[class_name_id]:
            self._class_name_id = class_name_id
        else:
            raise ValueError(
                "Class not found."
            )
    
    @property
    def teacher_id(self):
        return self._teacher_id
    
    @teacher_id.setter
    def teacher_id(self, teacher_id):
        if isinstance(teacher_id, int) and Teacher.all[teacher_id]:
            self._teacher_id = teacher_id
        else:
            raise ValueError(
                "Teacher not found."
            )
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Teacher_Class_Name instances in the database. """
        sql = """
            CREATE TABLE IF NOT EXISTS teacher_class_name (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            class_name_id INTEGER NOT NULL,
            teacher_id INTEGER NOT NULL,
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table used to persist the attributes of Teacher_Class_Name instances in the database. """
        sql = """
            DROP TABLE IF EXISTS teacher_class_name
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Save the teacher_class_name to the database. """

        sql = """
            INSERT INTO teacher_class_name (class_name_id, teacher_id)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.class_name_id, self.teacher_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, class_name_id, teacher_id):
        """ Create a new teacher_class_name instance and save it to the database. """

        teacher_class_name = cls(class_name_id, teacher_id)
        teacher_class_name.save()
        return teacher_class_name
    
    def delete(self):
        """ Delete the teacher_class_name from the database. """

        sql = """
            DELETE FROM teacher_class_name
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """ Return a teacher_class_name instance from the database. """

        teacher_class_name = cls.all.get(row[0])
        if teacher_class_name:
            teacher_class_name.class_name_id = row[1]
            teacher_class_name.teacher_id = row[2]
        else:
            teacher_class_name = cls(row[1], row[2])
            teacher_class_name.id = row[0]
            cls.all[teacher_class_name.id] = teacher_class_name
        return teacher_class_name
    
    @classmethod
    def get_all(cls):
        """ Return all instances of Teacher_Class_Name. """

        sql = """
            SELECT *
            FROM teacher_class_name
        """
        
        rows = CURSOR.execute(sql).fetchall()
        teacher_class_names = []
        
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """ Return the teacher_class_name with the given id. """

        sql = """
            SELECT * 
            FROM teacher_class_name 
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row)
    
    @classmethod
    def find_by_class_name_id(cls, class_name_id):
        """ Return the teacher_class_name with the given class_name_id. """

        sql = """
            SELECT * 
            FROM teacher_class_name 
            WHERE class_name_id = ?
        """
        rows = CURSOR.execute(sql, (class_name_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_teacher_id(cls, teacher_id):
        """ Return the teacher_class_name with the given teacher_id. """

        sql = """
            SELECT * 
            FROM teacher_class_name 
            WHERE teacher_id = ?
        """
        rows = CURSOR.execute(sql, (teacher_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]