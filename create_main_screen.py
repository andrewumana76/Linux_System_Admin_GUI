import curses
from functions_colors import init_colors
from functions_boxes import create_menu_box
from functions_connect import handle_connect
from function_connect import handle_disconnect

def setup_interface(stdscr):

    #Clear screen
    stdscr.clear()

    #Initialize screen colors
    init_colors(stdscr)
   
    #Refresh screen
    stdscr.refresh()

def create_main_screen_interface(stdscr):

    setup_interface(stdscr)
  
    #Wait for Input
    while True:
        #Creates initial menu box
        dimensions = create_menu_box(stdscr,10,30)
        y = dimensions[0]
        x = dimensions[1]

        #Create initial box
        stdscr.addstr(y + 1, x + 2, "Welcome to my Configurator", curses.color_pair(2))
        stdscr.addstr(y + 3, x + 2, "1. Create User", curses.color_pair(2))
        stdscr.addstr(y + 4, x + 2, "2. Modify User", curses.color_pair(2))
        stdscr.addstr(y + 5, x + 2, "3. Delete User", curses.color_pair(2))
        stdscr.addstr(y + 6, x + 2, "Q. Quit", curses.color_pair(2))

        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('1'):
            handle_connect(stdscr, 1)
        elif key == ord('2'):
            handle_disconnect(stdscr, 2)
        elif key == ord('3'):
            break
