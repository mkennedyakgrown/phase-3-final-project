# lib/text_edit_helpers.py

from models.__init__ import CONN, CURSOR

import npyscreen

class Text_Editor_Form(npyscreen.Form):

    all = {}

    def create(self):
        text = self.get_text()
        self.add(npyscreen.MultiLineEdit, name="Enter Text:", max_height=20, max_width=100, value=text, editable=True, scroll_exit=True, wrap=True, begin_entry_at=-1)
        save_button = self.add(npyscreen.ButtonPress, name="Save")
        save_button.when_pressed_function = self.on_save
        exit_button = self.add(npyscreen.ButtonPress, name="Exit")
        exit_button.when_pressed_function = self.on_exit
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
        type(self).all[1] = self.value
    
    def on_exit(self):
        self.on_save(0)
        self.exit_application()

    def exit_application(self):
        self.parentApp.NEXT_ACTIVE_FORM = None
        self.editing = False

class TextEditorApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", Text_Editor_Form, name="Text Editor")
    
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

if __name__ == "__main__":
    app = TextEditorApplication().run()