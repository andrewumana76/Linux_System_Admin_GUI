import curses

#Initialize colors
def init_colors(stdscr):
    
    curses.start_color()
    curses.use_default_colors()

    #Blue  
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    
    #Gray
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    
    #Create new color: 
    #curses.init_pair(3, , )

    #Background color
    stdscr.bkgd(curses.color_pair(1))
