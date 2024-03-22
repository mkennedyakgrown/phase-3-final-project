# lib/text_edit_helpers.py

from models.__init__ import CONN, CURSOR

import npyscreen

class Text_Editor_Form(npyscreen.Form):

    def create(self):
        text = self.get_text()
        self.add(npyscreen.MultiLineEdit, name="Enter Text:", max_height=20, max_width=100, value=text, editable=True, scroll_exit=True, wrap=True, begin_entry_at=-1)
        save_button = self.add(npyscreen.ButtonPress, name="Save")
        save_button.when_pressed_function = self.on_save
        exit_button = self.add(npyscreen.ButtonPress, name="Save and Exit")
        exit_button.when_pressed_function = self.on_exit
        cancel_button = self.add(npyscreen.ButtonPress, name="Cancel")
        cancel_button.when_pressed_function = self.on_cancel
        self.add_handlers({"^S": self.on_save})
        self.add_handlers({"^Q": self.on_exit})

    def get_text(self):
        sql = """
            SELECT text
            FROM text_data
            WHERE id = 1
        """
        text = CURSOR.execute(sql).fetchone()
        return text[0]

    def on_save(self, key=0):
        self.set_value(self.get_widget(0).value)
        TextEditorApplication.update_text(self.value)

    def on_cancel(self, key=0):
        sql = """
            SELECT text
            FROM text_data
            WHERE id = 2
        """
        text = CURSOR.execute(sql).fetchone()
        sql = """
            UPDATE text_data
            SET text = ?
            WHERE id = 1
        """
        CURSOR.execute(sql, (text[0],))
        CONN.commit()
        self.editing = False
        self.parentApp.setNextForm(None)
    
    def on_exit(self):
        self.on_save(0)
        self.exit_application()

    def exit_application(self):
        self.editing = False
        self.parentApp.setNextForm(None)

class TextEditorApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addFormClass("MAIN", Text_Editor_Form, name="Text Editor")
        self.setNextForm("MAIN")

    def restart(self):
        self.setNextForm("MAIN")

    def initialize_text(text):
        sql = """
            DROP TABLE IF EXISTS text_data;
        """
        CURSOR.execute(sql)
        CONN.commit()
        sql = """
            CREATE TABLE text_data (
                id INTEGER PRIMARY KEY,
                text TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        sql = """
            INSERT INTO text_data (text)
            VALUES ('')
        """
        CURSOR.execute(sql)
        CONN.commit()
        sql = """
            INSERT INTO text_data (text)
            VALUES (?)
        """
        CURSOR.execute(sql, (text,))
        CONN.commit()
    
    def update_text(text):
        sql = """
            UPDATE text_data
            SET text = ?
            WHERE id = 1
        """
        CURSOR.execute(sql, (text,))
        CONN.commit()

    def get_text():
        sql = """
            SELECT text
            FROM text_data
            WHERE id = 1
        """
        text = CURSOR.execute(sql).fetchone()
        return text[0]