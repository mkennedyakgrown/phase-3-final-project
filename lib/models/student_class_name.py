# lib/models/student_class_name.py
from models.__init__ import CONN, CURSOR
from models.student import Student
from models.class_name import Class_Name

class Student_Class_Name:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, class_name_id, student_id, id=None):
        self.class_name_id = class_name_id
        self.student_id = student_id
        self.id = id

    def __repr__(self):
        return (
            f"Student_Class_Name {self.id}: {self.class_name_id} {self.student_id}"
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
    def student_id(self):
        return self._student_id
    
    @student_id.setter
    def student_id(self, student_id):
        if isinstance(student_id, int) and Student.all[student_id]:
            self._student_id = student_id
        else:
            raise ValueError(
                "Student not found."
            )
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Student_Class_Name instances in the database. """
        sql = """
            CREATE TABLE IF NOT EXISTS student_class_name (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            class_name_id INTEGER NOT NULL,
            student_id INTEGER NOT NULL,
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table used to persist the attributes of Student_Class_Name instances in the database. """
        sql = """
            DROP TABLE IF EXISTS student_class_name
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Save the student_class_name to the database. """

        sql = """
            INSERT INTO student_class_name (class_name_id, student_id)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.class_name_id, self.student_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, class_name_id, student_id):
        """ Create a new student_class_name instance and save it to the database. """

        student_class_name = cls(class_name_id, student_id)
        student_class_name.save()
        return student_class_name
    
    def delete(self):
        """ Delete the student_class_name from the database. """

        sql = """
            DELETE FROM student_class_name
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """ Return a student_class_name instance from the database. """

        student_class_name = cls.all.get(row[0])
        if student_class_name:
            student_class_name.class_name_id = row[1]
            student_class_name.student_id = row[2]
        else:
            student_class_name = cls(row[1], row[2])
            student_class_name.id = row[0]
            cls.all[student_class_name.id] = student_class_name
        return student_class_name
    
    @classmethod
    def get_all(cls):
        """ Return all instances of Student_Class_Name. """

        sql = """
            SELECT *
            FROM student_class_name
        """
        
        rows = CURSOR.execute(sql).fetchall()
        student_class_names = []
        
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """ Return the student_class_name with the given id. """

        sql = """
            SELECT * 
            FROM student_class_name 
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row)
    
    @classmethod
    def find_by_class_name_id(cls, class_name_id):
        """ Return the student_class_name with the given class_name_id. """

        sql = """
            SELECT * 
            FROM student_class_name 
            WHERE class_name_id = ?
        """
        rows = CURSOR.execute(sql, (class_name_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_student_id(cls, student_id):
        """ Return the student_class_name with the given student_id. """

        sql = """
            SELECT * 
            FROM student_class_name 
            WHERE student_id = ?
        """
        rows = CURSOR.execute(sql, (student_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]