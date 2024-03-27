#lib/curses_text_editor.py

import curses

from models.__init__ import CONN, CURSOR

def main(stdscr):
    # Initialize variables
    buffer = []  # List to store text lines
    stored_text = get_text()
    if stored_text is not None:
        buffer = load_buffer(stored_text)
    else:
        buffer.append("")
    row = 0
    col = 0
    directions = """Ctrl+A to Save and Quit
    Ctrl+B to Cancel"""



    # Main loop
    while True:
        # Clear screen
        stdscr.erase()

        # Display text buffer
        for i, line in enumerate(buffer):
            stdscr.addstr(i, 1, line)

        # Display buttons
        stdscr.addstr(len(buffer) + 1, 1, directions)

        # Move cursor
        stdscr.move(row, col)

        # Get user input
        key = stdscr.getch()

        # Handle key presses
        if key == curses.KEY_UP and row > 0:
            row -= 1
            if len(buffer[row]) < len(buffer[row + 1]):
                col = len(buffer[row])
        elif key == curses.KEY_DOWN and row < len(buffer) - 1:
            row += 1
            if len(buffer[row]) < len(buffer[row - 1]):
                col = len(buffer[row])
        elif key == curses.KEY_LEFT and col > 0:
            col -= 1
        elif key == curses.KEY_RIGHT and col < len(buffer[row]) if buffer else 0:
            col += 1
        elif key in range(32, 127):  # Handle printable characters
            if len(buffer[row]) < curses.COLS - 1:
                buffer[row] = buffer[row][:col] + chr(key) + buffer[row][col:]
                col += 1
        elif key == curses.KEY_BACKSPACE or key == 127 and col > 0:
            buffer[row] = buffer[row][:col-1] + buffer[row][col:]
            col -= 1
        elif key == 10:  # Enter key - create new line
            buffer.insert(row + 1, "")
            row += 1
            col = 0
        elif key == 1:  # Save and quit on Ctrl+A
            break
        elif key == 2:  # Cancel on Ctrl+B
            on_cancel()
            break

        # Refresh screen
        stdscr.refresh()

        save_text = "\n".join(buffer)

        sql = """
            UPDATE text_data
            SET text = ?
            WHERE id = 1"""

        CURSOR.execute(sql, (save_text,))
        CONN.commit()

def on_cancel():
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

def get_text():
    sql = """
        SELECT text
        FROM text_data
        WHERE id = 1
    """
    text = CURSOR.execute(sql).fetchone()
    return text[0]

def load_buffer(text):
    sql = """
        SELECT text
        FROM text_data
        WHERE id = 2
    """
    text = CURSOR.execute(sql).fetchone()[0]
    return text.split("\n")

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

def enter_text_editor():
    curses.wrapper(main)