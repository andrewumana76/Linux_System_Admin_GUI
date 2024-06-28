import curses

def main(stdscr):
    # Clear screen
    stdscr.clear()
    
    # Create a window and draw a box around it
    height, width = 10, 40
    start_y, start_x = 5, 5
    win = curses.newwin(height, width, start_y, start_x)
    win.box()
    
    # Add a string inside the box
    win.addstr(1, 1, "Hello, world!")
    
    # Refresh to update the screen
    win.refresh()
    stdscr.refresh()

    # Wait for a key press
    stdscr.getch()

curses.wrapper(main)
