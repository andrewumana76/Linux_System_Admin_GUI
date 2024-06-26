import curses

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)
    stdscr.clear()
    
    # Define window dimensions
    h, w = stdscr.getmaxyx()
    button_win = curses.newwin(3, 20, h // 2 - 1, w // 2 - 10)
    input_win = None
    
    # Button text
    button_text = "Add Domain"
    
    # Input box visibility flag
    input_visible = False
    
    def draw_button():
        button_win.clear()
        button_win.border()
        button_win.addstr(1, 1, button_text)
        button_win.refresh()
    
    def draw_input_box():
        if input_visible:
            input_win.clear()
            input_win.border()
            input_win.addstr(1, 1, "Domain: ")
            input_win.refresh()
    
    draw_button()
    
    while True:
        key = stdscr.getch()
        
        if key == ord('q'):
            break
        
        elif key == ord('\n'):  # Enter key
            if not input_visible:
                # Show input box
                input_win = curses.newwin(3, 40, h // 2 + 2, w // 2 - 20)
                input_visible = True
            else:
                # Hide input box
                input_win.clear()
                input_visible = False
                input_win = None
            
            draw_input_box()
        
        draw_button()

curses.wrapper(main)
