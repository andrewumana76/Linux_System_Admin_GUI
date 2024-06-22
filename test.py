import curses

def main(stdscr):
    curses.curs_set(0)  # Hide cursor

    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Default colors
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Custom color pair

    # Get screen dimensions
    height, width = stdscr.getmaxyx()

    # Create a new window for drawing
    win_height = 10
    win_width = 40
    win_y = (height - win_height) // 2
    win_x = (width - win_width) // 2
    win = curses.newwin(win_height, win_width, win_y, win_x)

    # Set background color to gray
    win.bkgd(' ', curses.color_pair(2))  # Use color pair 2 (black on white)

    # Draw a box with gray background
    win.box()

    # Refresh the window to show changes
    win.refresh()

    # Wait for user input
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
