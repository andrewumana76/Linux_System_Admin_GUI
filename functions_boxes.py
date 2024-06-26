import curses

#Create menu box
def create_menu_box(stdscr, box_height, box_width):

    #Calculating max X and Y length
    height, width = stdscr.getmaxyx()

    #Setting X and Y locations based on box height/width
    y = (curses.LINES - box_height) // 2
    x = (curses.COLS - box_width) // 2

    #Draw box
    box_win = curses.newwin(box_height, box_width, y, x)
    box_win.bkgd(' ', curses.color_pair(2))
    box_win.box()
    box_win.refresh()
    stdscr.refresh()

    #Return dimensions of box so we can determine where to place text
    dimensions = [y , x]

    return dimensions
