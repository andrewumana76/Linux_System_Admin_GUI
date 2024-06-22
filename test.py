import curses

def main(stdscr):
    stdscr.clear()
    curses.curs_set(1)  # Show cursor

    # Window dimensions
    height, width = stdscr.getmaxyx()

    # Create input windows
    input_win1 = curses.newwin(1, 20, 2, 2)
    input_win2 = curses.newwin(1, 20, 4, 2)

    # Draw labels
    input_win1.addstr(0, 0, "Input 1: ")
    input_win2.addstr(0, 0, "Input 2: ")

    # Refresh windows
    input_win1.refresh()
    input_win2.refresh()

    # Initialize variables
    current_field = 1  # Start with first input field

    while True:
        key = stdscr.getch()

        if key == curses.ascii.TAB:
            # Handle Tab key press
            if current_field == 1:
                # Move focus to input_win2
                input_win1.move(0, 9)  # Move cursor to end of input_win1
                current_field = 2
            elif current_field == 2:
                # Move focus back to input_win1
                input_win2.move(0, 9)  # Move cursor to end of input_win2
                current_field = 1

        elif key == curses.ascii.NL:  # Enter key to exit
            break

        # Handle input for each window
        if current_field == 1:
            input_win1.refresh()
            input_str1 = input_win1.getstr().decode('utf-8')
        elif current_field == 2:
            input_win2.refresh()
            input_str2 = input_win2.getstr().decode('utf-8')

    curses.endwin()

if __name__ == "__main__":
    curses.wrapper(main)
