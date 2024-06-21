import curses
import time

#Initialize colors
def init_colors(stdscr):
    
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)

    #Background color
    stdscr.bkgd(curses.color_pair(1))


#Create menu box
def create_menu_box(stdscr):

    #Calculating max X and Y length
    height, width = stdscr.getmaxyx()
 
    box_height = 6
    box_width = 40
    y = (curses.LINES - box_height) // 2
    x = (curses.COLS - box_width) // 2

    #Draw box
    box_win = curses.newwin(box_height, box_width, y, x)
    box_win.bkgd(' ', curses.color_pair(3))
    box_win.box()
    box_win.refresh()
    stdscr.refresh()

    #Text-based interface
    stdscr.addstr(y + 1, x + 1, "Welcome to my Configurator", curses.color_pair(1) | curses.A_BOLD)
    stdscr.addstr(y + 3, x + 1, "1. Create User")
    stdscr.addstr(y + 4, x + 1, "2. Modify User")
    stdscr.addstr(y + 5, x + 1, "3. Delete User")
    stdscr.addstr(y + 6, x + 1, "4. Quit")

    stdscr.refresh()


def setup_interface(stdscr):

    #Clear screen
    stdscr.clear()

    #Initialize screen colors
    init_colors(stdscr)

    #Drawing menu
    create_menu_box(stdscr)
   
    #Refresh screen
    stdscr.refresh()



def handle_connect(stdscr, value):    
    
    if value == 1 :
        #create user screen
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
        
        input_win = curses.newwin(1, (curses.COLS -len(prompts[i]) - 1) // 4 , prompts_y[i], prompts_x[i] + (len(prompts[i])))
        input_windows.append(input_win)
    
    return input_windows



def create_button(stdscr,button_prompt,button_y,button_x):

    height, width = stdscr.getmaxyx()
    stdscr.addstr(height // 2, (width - len(button_prompt)) // 2, button_prompt)
    stdscr.refresh()


#def run_create_user_script(username, password, confirm):



def create_user(stdscr):

    #clear screen  
    stdscr.clear()

    #Calculating max X and Y length
    height, width = stdscr.getmaxyx()
 
    box_height = 6
    box_width = 40
    y = (curses.LINES - box_height) // 2
    x = (curses.COLS - box_width) // 2
    box_win = curses.newwin(box_height, box_width, y, x)

    #Draw box
    box_win.bkgd(curses.color_pair(3))
    box_win.box()
    box_win.refresh()
   
    stdscr.refresh()
    
    #Variable prompts
    username_prompt="Enter Username  : "
    username_y=0 + y
    username_x=0 + x

    password_prompt="Enter Password  : "
    password_y=1 + y
    password_x=0 + x

    confirm_prompt ="Confirm Password: " 
    confirm_y=2 + y
    confirm_x=0 + x

    prompts = [username_prompt, password_prompt, confirm_prompt]
    prompts_y = [username_y, password_y, confirm_y]
    prompts_x = [username_x, password_x, confirm_x]

    refresh = 0
    current_field=0
    bool_var = True


    while bool_var == True:

        input_windows = create_input_windows(stdscr,prompts,prompts_y,prompts_x)


        for i in range (len(prompts)):
            stdscr.addstr(prompts_y[i], prompts_x[i], prompts[i], curses.A_BOLD)
            stdscr.refresh()


        curses.echo()

        username_input = input_windows[0].getstr().decode('utf-8')
        password_input = input_windows[1].getstr().decode('utf-8')
        confirm_input = input_windows[2].getstr().decode('utf-8')


        #put logic here for determining what to do with the inputs
        #if username_input != "" and password_input != "" and confirm_input !="" and password_input == confirm_input :
            #bool_var = False
            #stdscr.clear()

def main(stdscr):
    
    setup_interface(stdscr)

    #Wait for Input
    while True:
        key = stdscr.getch()
        if key == ord('1'):
            handle_connect(stdscr, 1)
        elif key == ord('2'):
            handle_disconnect(stdscr, 2)
        elif key == ord('3'):
            break



if __name__ == "__main__":
    curses.wrapper(main)
