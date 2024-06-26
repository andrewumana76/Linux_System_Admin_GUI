import curses
from create_main_screen import setup_interface
from functions_boxes import create_menu_box
from functions_buttons import create_buttons
from functions_buttons import draw_buttons
from functions_colors import init_colors
from functions_string_input import draw_button_input_boxes
from functions_string_input import clear_input_box
from functions_string_input import create_input_windows
from functions_string_input import handle_input

def create_user_screen_interface(stdscr):

    #clear screen  
    stdscr.clear()

    #Variable prompts
    username_prompt="Enter Username  : "
    #username_y=0 + y
    #username_x=0 + x

    password_prompt="Enter Password  : "
    #password_y=1 + y
    #password_x=0 + x

    confirm_prompt ="Confirm Password: " 
    #confirm_y=2 + y
    #confirm_x=0 + x

    prompts = [username_prompt, password_prompt, confirm_prompt]
    #prompts_y = [username_y, password_y, confirm_y]
    #prompts_x = [username_x, password_x, confirm_x]

    initial_run = 0
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

        username_input = input_windows[0].getstr().decode('utf-8')
        password_input = input_windows[1].getstr().decode('utf-8')
        confirm_input = input_windows[2].getstr().decode('utf-8')


        #put logic here for determining what to do with the inputs
        #if username_input != "" and password_input != "" and confirm_input !="" and password_input == confirm_input :
            #bool_var = False
            #stdscr.clear()
