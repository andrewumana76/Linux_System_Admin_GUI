import curses
from screen_create_user import create_user_screen_interface

def handle_connect(stdscr, value):    
    
    if value == 1 :
        #create_user(stdscr)
        create_user_screen_interface(stdscr)
    #if value == 2 :
        #modify user screen
    #if value == 3 :
        #delete user screen
    #if value == 4 :
        #quit screen
        
    stdscr.refresh()

def handle_disconnect(stdscr):
    stdscr.addstr(6, 0, "Disconnecting...", curses.A_BOLD)
    stdscr.refresh()
