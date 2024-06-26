import curses

def main(stdscr):
    curses.curs_set(1)  # Show cursor
    
    stdscr.clear()
    stdscr.refresh()
    
    stdscr.addstr(5, 10, "Enter text (Press Enter to submit):")
    stdscr.refresh()

    # Define input box dimensions and position
    input_box_start_y = 7
    input_box_start_x = 10
    input_box_width = 40

    # Initialize input value
    input_value = ""
    
    # Function to draw the input box
    def draw_input_box():
        stdscr.addstr(input_box_start_y, input_box_start_x, input_value.ljust(input_box_width), curses.A_UNDERLINE)
    
    # Function to handle keyboard input
    def handle_input(key):
        nonlocal input_value
        
        if key == 10:  # Enter key
            stdscr.addstr(input_box_start_y + 2, input_box_start_x, f"Input submitted: {input_value}", curses.A_BOLD)
            input_value = ""
        elif key == curses.KEY_BACKSPACE:
            if input_value:
                input_value = input_value[:-1]
        elif key >= 32 and key <= 126:  # Accept printable ASCII characters
            input_value += chr(key)

    while True:
        key = stdscr.getch()

        if key == ord('q'):
            break
        
        handle_input(key)
        stdscr.clear()
        stdscr.addstr(5, 10, "Enter text (Press Enter to submit):")
        draw_input_box()
        stdscr.refresh()

curses.wrapper(main)
