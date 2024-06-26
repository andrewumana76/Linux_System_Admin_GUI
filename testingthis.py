import curses

def main(stdscr):
    curses.curs_set(1)  # Show cursor
    
    stdscr.clear()
    stdscr.refresh()
    
    stdscr.addstr(5, 10, "Enter text (Press Enter to submit):")
    stdscr.refresh()

    # Define positions for input boxes
    input_box_start_y = 7
    input_box_start_x = 10
    input_box_width = 40
    input_box_height = 3

    # Initialize input values
    input_values = ["", "", ""]
    
    # Current input box index
    current_input = 0

    # Function to draw input boxes
    def draw_input_boxes():
        for i, value in enumerate(input_values):
            stdscr.addstr(input_box_start_y + i * (input_box_height + 1), input_box_start_x, value.ljust(input_box_width), curses.A_UNDERLINE)

    # Function to handle keyboard input
    def handle_input(key):
        nonlocal current_input
        
        if key == 10:  # Enter key
            stdscr.addstr(input_box_start_y + len(input_values) * (input_box_height + 1), input_box_start_x, f"Input submitted: {input_values[current_input]}", curses.A_BOLD)
            input_values[current_input] = ""
        elif key == curses.KEY_BACKSPACE:
            if input_values[current_input]:
                input_values[current_input] = input_values[current_input][:-1]
        elif key >= 32 and key <= 126:  # Accept printable ASCII characters
            input_values[current_input] += chr(key)
        elif key == curses.KEY_LEFT:
            if stdscr.getyx()[1] > input_box_start_x:
                stdscr.move(stdscr.getyx()[0], stdscr.getyx()[1] - 1)
        elif key == curses.KEY_RIGHT:
            if stdscr.getyx()[1] < input_box_start_x + input_box_width:
                stdscr.move(stdscr.getyx()[0], stdscr.getyx()[1] + 1)
        elif key == curses.KEY_UP:
            current_input = (current_input - 1) % len(input_values)
            stdscr.move(input_box_start_y + current_input * (input_box_height + 1), input_box_start_x + len(input_values[current_input]))
        elif key == curses.KEY_DOWN:
            current_input = (current_input + 1) % len(input_values)
            stdscr.move(input_box_start_y + current_input * (input_box_height + 1), input_box_start_x + len(input_values[current_input]))

    while True:
        key = stdscr.getch()

        if key == ord('q'):
            break
        
        handle_input(key)
        stdscr.clear()
        stdscr.addstr(5, 10, "Enter text (Press Enter to submit):")
        draw_input_boxes()
        stdscr.refresh()

curses.wrapper(main)
