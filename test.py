import curses

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)
    stdscr.clear()
    
    # Define window dimensions
    h, w = stdscr.getmaxyx()
    
    # Button positions
    button_positions = [
        (h // 2 - 2, w // 2 - 10),
        (h // 2 + 2, w // 2 - 10)
    ]
    
    # Create windows for buttons and input box
    buttons = [curses.newwin(3, 20, pos[0], pos[1]) for pos in button_positions]
    input_win = None
    
    # Button texts
    button_texts = ["Add Domain", "Another Action"]
    
    # Input box visibility flag
    input_visible = False
    
    # Current selected button
    current_button = 0
    
    def draw_buttons():
        for i, button_win in enumerate(buttons):
            button_win.clear()
            button_win.border()
            if i == current_button:
                button_win.addstr(1, 1, button_texts[i], curses.A_REVERSE)
            else:
                button_win.addstr(1, 1, button_texts[i])
            button_win.refresh()
    
    def draw_input_box():
        if input_visible:
            input_win.clear()
            input_win.border()
            input_win.addstr(1, 1, "Domain: ")
            input_win.refresh()
    
    draw_buttons()
    
    while True:
        key = stdscr.getch()
        
        if key == ord('q'):
            break
        
        elif key == curses.KEY_UP:
            current_button = (current_button - 1) % len(buttons)
        
        elif key == curses.KEY_DOWN:
            current_button = (current_button + 1) % len(buttons)
        
        elif key == ord('\n'):
            if current_button == 0 and not input_visible:
                # Show input box for "Add Domain"
                input_win = curses.newwin(3, 40, h // 2 + 5, w // 2 - 20)
                input_visible = True
            elif current_button == 0 and input_visible:
                # Hide input box
                input_win.clear()
                input_visible = False
                input_win = None
            # Handle other button actions here if necessary
            
            draw_input_box()
        
        draw_buttons()

curses.wrapper(main)
