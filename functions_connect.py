import curses

def handle_connect(stdscr, value):    
    
    if value == 1 :
        #create_user(stdscr)
        stdscr.addstr(6, 0, "1 is pressed...", curses.A_BOLD)
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
