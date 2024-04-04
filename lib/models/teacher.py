# lib/models/teacher.py
from models.__init__ import CONN, CURSOR

class Teacher:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        return (
            f"Teacher {self.id}: {self.name}"
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
        """ Create a new table to persist the attributes of Teacher instances in the database. """
        sql = """
            CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """ Drop the table used to persist the attributes of Teacher instances in the database. """
        sql = """
            DROP TABLE IF EXISTS teachers
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Save the teacher to the database. """

        sql = """
            INSERT INTO teachers (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """ Update the name of the teacher in the database. """

        sql = """
            UPDATE teachers
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        """ Delete the teacher from the database. """

        sql = """
            DELETE FROM teachers
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def create(cls, name):
        """ Create a new teacher instance and save it to the database. """

        teacher = cls(name)
        teacher.save()
        return teacher
    
    @classmethod
    def instance_from_db(cls, row):
        """ Return a teacher instance from the database. """

        teacher = cls.all.get(row[0])
        if teacher:
            teacher.name = row[1]
        else:
            teacher = cls(row[1])
            teacher.id = row[0]
            cls.all[teacher.id] = teacher
        return teacher
    
    @classmethod
    def get_all(cls):
        """ Return all the teachers in the database. """

        sql = """
            SELECT * 
            FROM teachers
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """ Return the teacher with the given id. """

        sql = """
            SELECT * 
            FROM teachers 
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()

        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """ Return the teacher with the given name. """

        sql = """
            SELECT *
            FROM teachers
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def get_classes(self):
        """ Return all the classes that the teacher has. """
        from models.class_name import Class_Name
        class_names = Class_Name.get_all()

        return [class_name for class_name in class_names if class_name.teacher_id == self.id]

    def get_students(self):
        """ Return all the students that the teacher has. """
        from models.student import Student
        from models.student_class_name import Student_Class_Name

        classes = self.get_classes()

        student_class_rows = []
        student_class_rows.extend(Student_Class_Name.find_by_class_name_id(class_.id) for class_ in classes)
        
        rows = []
        for student_class_row in student_class_rows:
            for row in student_class_row:
                rows.append(Student.find_by_id(row.student_id))

        students = set([Student.instance_from_db([row.id, row.name]) for row in rows])

        return students
    
    def get_reports(self):
        """ Return all the reports for the class. """
        from models.report import Report
        
        return Report.get_teacher_reports(self)