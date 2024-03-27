# lib/models/report.py

from models.__init__ import CONN, CURSOR

class Report:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, text, class_name_id, teacher_id, student_id, id=None):
        self.text = text
        self.class_name_id = class_name_id
        self.teacher_id = teacher_id
        self.student_id = student_id
        self.id = id

    def __repr__(self):
        return (
            f"""Report {self.id}: Class: {self.class_name_id} Teacher: {self.teacher_id} Student: {self.student_id}
        {self.text}"""
        )
    
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, text):
        if isinstance(text, str):
            self._text = text
        else:
            raise ValueError(
                "Text must be a string."
            )
    
    @property
    def class_name_id(self):
        return self._class_name_id
    
    @class_name_id.setter
    def class_name_id(self, class_name_id):
        from models.class_name import Class_Name
        if isinstance(class_name_id, int) and Class_Name.find_by_id(class_name_id):
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
        from models.teacher import Teacher
        if isinstance(teacher_id, int) and Teacher.find_by_id(teacher_id):
            self._teacher_id = teacher_id
        else:
            raise ValueError(
                "Teacher not found."
            )
        
    @property
    def student_id(self):
        return self._student_id
    
    @student_id.setter
    def student_id(self, student_id):
        from models.student import Student
        if isinstance(student_id, int) and Student.find_by_id(student_id):
            self._student_id = student_id
        else:
            raise ValueError(
                "Student not found."
            )
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Report instances in the database. """
        sql = """
            CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            class_name_id INTEGER NOT NULL,
            teacher_id INTEGER NOT NULL,
            student_id INTEGER NOT NULL
        );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table used to persist the attributes of Report instances in the database. """
        sql = """
            DROP TABLE IF EXISTS reports
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Save the report to the database. """

        sql = """
            INSERT INTO reports (text, class_name_id, teacher_id, student_id)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.text, self.class_name_id, self.teacher_id, self.student_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """ Update the report in the database. """

        sql = """
            UPDATE reports
            SET text = ?, class_name_id = ?, teacher_id = ?, student_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.text, self.class_name_id, self.teacher_id, self.student_id, self.id))
        CONN.commit()

    def delete(self):
        """ Delete the report from the database. """

        sql = """
            DELETE FROM reports
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None
    
    @classmethod
    def create(cls, text, class_name_id, teacher_id, student_id):
        """ Create a new report instance and save it to the database. """
        
        report = cls(text, class_name_id, teacher_id, student_id)
        report.save()
        return report
    
    @classmethod
    def instance_from_db(cls, row):
        """ Return a report instance from the database. """
        
        report = cls.all.get(row[0])
        if report:
            report.text = row[1]
            report.class_name_id = row[2]
            report.teacher_id = row[3]
            report.student_id = row[4]
        else:
            report = cls(row[1], row[2], row[3], row[4])
            report.id = row[0]
            cls.all[report.id] = report
        return report
    
    @classmethod
    def get_all(cls):
        """ Return all the reports in the database. """
        
        sql = """
            SELECT *
            FROM reports
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """ Return the report with the given id. """
        
        sql = """
            SELECT *
            FROM reports
            WHERE id = ?
        """
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()

        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_ids(cls, class_name_id, teacher_id, student_id):
        """ Return the report with the given class_name_id, teacher_id, and student_id. """
        
        sql = """
            SELECT *
            FROM reports
            WHERE class_name_id = ? AND teacher_id = ? AND student_id = ?
        """
        CURSOR.execute(sql, (class_name_id, teacher_id, student_id))
        row = CURSOR.fetchone()

        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def get_class_reports(cls, class_name_id):
        """ Return all the reports for the given class_name_id. """
        
        sql = """
            SELECT *
            FROM reports
            WHERE class_name_id = ?
        """
        CURSOR.execute(sql, (class_name_id,))
        rows = CURSOR.fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def get_teacher_reports(cls, teacher_id):
        """ Return all the reports for the given teacher_id. """
        
        sql = """
            SELECT *
            FROM reports
            WHERE teacher_id = ?
        """
        CURSOR.execute(sql, (teacher_id,))
        rows = CURSOR.fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def get_student_reports(cls, student_id):
        """ Return all the reports for the given student_id. """
        
        sql = """
            SELECT *
            FROM reports
            WHERE student_id = ?
        """
        CURSOR.execute(sql, (student_id,))
        rows = CURSOR.fetchall()

        return [cls.instance_from_db(row) for row in rows]