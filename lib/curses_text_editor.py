#lib/curses_text_editor.py

import curses

from models.__init__ import CONN, CURSOR

def main(stdscr):
  # Initialize variables
  buffer = []  # List to store text lines
  buffer.append("")
  row = 0
  col = 0
  directions = """Ctrl+A to Save and Quit
  Ctrl+B to Cancel"""

  # Load a file (optional)
  # ... (code to open and read file into buffer)

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
      print("Ctrl+A")
    elif key == 2:  # Save and quit on Ctrl+B
      print("Ctrl+B")
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

curses.wrapper(main)