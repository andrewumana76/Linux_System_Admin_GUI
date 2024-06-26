import curses
from string_input_functions import draw_input_boxes
from string_input_functions import clear_input_box
from string_input_functions import handle_input

def init_curses():
    curses.curs_set(0)

def create_buttons(stdscr, button_positions, button_texts):
    buttons = [curses.newwin(3, 20, pos[0], pos[1]) for pos in button_positions]
    draw_buttons(buttons, button_texts, 0)
    return buttons

def draw_buttons(buttons, button_texts, current_button):
    for i, button_win in enumerate(buttons):
        button_win.clear()
        button_win.border()
        if i == current_button:
            button_win.addstr(1, 1, button_texts[i], curses.A_REVERSE)
        else:
            button_win.addstr(1, 1, button_texts[i])
        button_win.refresh()

#def draw_input_boxes(button_positions, input_states, input_values, button_texts):
#    for i, state in enumerate(input_states):
#        if state:
#            input_win = curses.newwin(3, 40, button_positions[i][0] + 3, button_positions[i][1] - 10)
#            input_win.clear()
#            input_win.border()
#            input_win.addstr(1, 1, f"{button_texts[i]}: {input_values[i]}")
#            input_win.refresh()
#
#def clear_input_box(button_positions, i):
#    if i >= 0:
#        input_win = curses.newwin(3, 40, button_positions[i][0] + 3, button_positions[i][1] - 10)
#        input_win.clear()
#        input_win.refresh()
#
#def handle_input(stdscr, button_positions, input_states, input_values, button_texts, current_button):
#    curses.curs_set(1)
#    input_win = curses.newwin(3, 40, button_positions[current_button][0] + 3, button_positions[current_button][1] - 10)
#    input_win.clear()
#    input_win.border()
#    curses.echo()
#    input_win.addstr(1, 1, f"{button_texts[current_button]}: ")
#    input_win.refresh()
#    input_values[current_button] = input_win.getstr(1, len(button_texts[current_button]) + 2, 30).decode('utf-8')
#    curses.noecho()
#    input_states[current_button] = False
#    curses.curs_set(0)
#    clear_input_box(button_positions, current_button)

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
