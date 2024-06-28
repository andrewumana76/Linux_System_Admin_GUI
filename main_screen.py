import curses
import time

#Initialize colors
def init_colors(stdscr):
    
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)
    #curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_GREY)

    #Background color
    stdscr.bkgd(curses.color_pair(1))


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


def setup_interface(stdscr):

    #Clear screen
    stdscr.clear()

    #Initialize screen colors
    init_colors(stdscr)

    #Drawing menu
    #create_menu_box(stdscr)
   
    #Refresh screen
    stdscr.refresh()



def handle_connect(stdscr, value):    
    
    if value == 1 :
        create_user(stdscr)
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



def create_input_windows(stdscr,prompts,prompts_y, prompts_x):

    input_windows= []
    
    #Creates an input window for each box
    for i in range (len(prompts)) :
        
        #input_win = curses.newwin(1, (curses.COLS -len(prompts[i]) - 1) // 4 , prompts_y[i], prompts_x[i] + (len(prompts[i])))
        input_win = curses.newwin(1, 20 , prompts_y[i], prompts_x[i] + (len(prompts[i])))
        input_windows.append(input_win)
    
    return input_windows


def create_user(stdscr):

    #clear screen  
    stdscr.clear()

    #Variable prompts
    username_prompt="Enter Username  : "
    password_prompt="Enter Password  : "
    confirm_prompt ="Confirm Password: " 
    prompts = [username_prompt, password_prompt, confirm_prompt]

    current_field=0
    bool_var = True


    while bool_var == True:

        dimensions = create_menu_box(stdscr,10,70)
        y = dimensions[0]
        x = dimensions[1]
        
            
        username_y = 3 + y
        username_x = 3 + x

        password_y = 5 + y
        password_x = 3 + x

        confirm_y = 7 + y
        confirm_x = 3 + x

        prompts_y = [username_y, password_y, confirm_y]
        prompts_x = [username_x, password_x, confirm_x]


        input_windows = create_input_windows(stdscr,prompts,prompts_y,prompts_x)

        dimensions = create_menu_box(stdscr,10,70)

        for i in range (len(prompts)):
            stdscr.addstr(prompts_y[i], prompts_x[i], prompts[i], curses.color_pair(2))
            stdscr.refresh()


        curses.echo()

        #username_input = input_windows[0].getstr().decode('utf-8')
        #password_input = input_windows[1].getstr().decode('utf-8')
        #confirm_input = input_windows[2].getstr().decode('utf-8')


        
            



def main(stdscr):
    
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



if __name__ == "__main__":
    curses.wrapper(main)
