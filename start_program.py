import curses
from functions_boxes import create_menu_box
from functions_buttons import create_buttons
from functions_buttons import draw_buttons
from functions_colors import init_colors
from functions_string_input import draw_input_boxes
from functions_string_input import clear_input_box
from functions_string_input import handle_input

def init_curses():
    curses.curs_set(0)

def main(stdscr):
    # Initialize curses
    init_curses()
    stdscr.clear()
    stdscr.refresh()
    
    # Define window dimensions
    h, w = stdscr.getmaxyx()
    
    # Button positions
    button_positions = [
        (h // 2 - 4, w // 2 - 10),
        (h // 2, w // 2 - 10)
    ]
    
    # Button texts
    button_texts = ["Add Domain", "Another Action"]
    
    # Input box states
    input_states = [False, False]
    input_values = ["", ""]
    
    # Current selected button
    current_button = 0
    
    # Create and draw buttons
    buttons = create_buttons(stdscr, button_positions, button_texts)
    
    while True:
        key = stdscr.getch()

        dimensions = create_menu_box(stdscr, 15,30)
        
        if key == ord('q'):
            break
        
        elif key == curses.KEY_UP:
            current_button = (current_button - 1) % len(buttons)
        
        elif key == curses.KEY_DOWN:
            current_button = (current_button + 1) % len(buttons)
        
        elif key == ord('\n'):
            if input_states[current_button]:
                # If the input box is already open, close it
                input_states[current_button] = False
                clear_input_box(button_positions, current_button)
                curses.curs_set(0)
            else:
                # Open the input box for the selected button
                input_states[current_button] = True
                handle_input(stdscr, button_positions, input_states, input_values, button_texts, current_button)
            
            draw_buttons(buttons, button_texts, current_button)
            draw_input_boxes(button_positions, input_states, input_values, button_texts)

        draw_buttons(buttons, button_texts, current_button)

curses.wrapper(main)