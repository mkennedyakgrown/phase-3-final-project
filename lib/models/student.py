# lib/models/student.py
from models.__init__ import CONN, CURSOR

class Student:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        return (
            f"Student {self.id}: {self.name}"
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
        """ Create a new table to persist the attributes of Student instances in the database. """
        sql = """
            CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """ Drop the table used to persist the attributes of Student instances in the database. """
        sql = """
            DROP TABLE IF EXISTS students
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Save the student to the database. """

        sql = """
            INSERT INTO students (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """ Update the name of the student in the database. """

        sql = """
            UPDATE students
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        """ Delete the student from the database. """

        reports = self.get_reports()
        for report in reports:
            report.delete()

        sql = """
            DELETE FROM students
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        sql = """
            DELETE FROM student_class_names
            WHERE student_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def create(cls, name):
        """ Create a new student instance and save it to the database. """

        student = cls(name)
        student.save()
        return student
    
    @classmethod
    def instance_from_db(cls, row):
        """ Return a student instance from the database. """

        student = cls.all.get(row[0])
        if student:
            student.name = row[1]
        else:
            student = cls(row[1])
            student.id = row[0]
            cls.all[student.id] = student
        return student
    
    @classmethod
    def get_all(cls):
        """ Return all the students in the database. """

        sql = """
            SELECT * 
            FROM students
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """ Return the student with the given id. """

        sql = """
            SELECT * 
            FROM students 
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()

        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """ Return the student with the given name. """

        sql = """
            SELECT *
            FROM students
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()

        return cls.instance_from_db(row) if row else None
    
    def get_classes(self):
        """ Return all the classes that the student has. """
        from models.class_name import Class_Name
        from models.student_class_name import Student_Class_Name

        student_class_rows = Student_Class_Name.find_by_student_id(self.id)
        rows = [Class_Name.find_by_id(row.class_name_id) for row in student_class_rows]
        
        return [Class_Name.find_by_id(row.id) for row in rows]

    def get_teachers(self):
        """ Return all the teachers that the student has. """
        from models.teacher import Teacher
        
        classes = self.get_classes()

        rows = [class_name.get_teacher() for class_name in classes]

        return [Teacher.instance_from_db(row) for row in rows]
    
    def get_reports(self):
        """ Return all the reports for the student. """
        from models.report import Report

        rows = Report.get_student_reports(self.id)
        
        return [Report.instance_from_db([row.id, row.text, row.class_name_id, row.student_id]) for row in rows]