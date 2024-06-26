import curses
#from create_main_screen import setup_interface
from functions_boxes import create_menu_box
from functions_buttons import create_buttons
from functions_buttons import draw_buttons
from functions_colors import init_colors
from functions_string_input import draw_button_input_boxes
from functions_string_input import clear_input_box
from functions_string_input import create_input_windows
from functions_string_input import handle_input


#def handle_input2(key):
#    nonlocal input_value
#
#    if key == 10 or key == 9:
#        current_position += 1
        


def create_user_screen_interface(stdscr):

    #clear screen  
    stdscr.clear()

    #Variable prompts
    username_prompt="Enter Username  : "
    password_prompt="Enter Password  : "
    confirm_prompt ="Confirm Password: "
    empty_string = ""
    prompts = [username_prompt, password_prompt, confirm_prompt,empty_string,empty_string,empty_string]

    initial_run = 0
    current_field=0
    bool_var = True
    deviation = 2


    #Button Variables
    h, w = stdscr.getmaxyx()
    button_y = [h-5, h-5]
    button_x = [5, w-25]

    button_positions = [
            (button_y[0], button_x[0]),
            (button_y[1], button_x[1])
    ]

    button_texts = ["Previous","Next"]
    
    input_states = [True,True]
    input_values = ["",""]

    current_button=0

    buttons = create_buttons(stdscr, button_positions, button_texts)

    stdscr.refresh()
    
    while bool_var == True:

        dimensions = create_menu_box(stdscr,10,70)
        y = dimensions[0]
        x = dimensions[1]
             
        
        username_y = 3 + y
        username_x = 3 + x

        username_input_y = username_y
        username_input_x = username_x + deviation

        password_y = 5 + y
        password_x = 3 + x

        password_input_y = password_y
        password_input_x = password_x + deviation

        confirm_y = 7 + y
        confirm_x = 3 + x

        confirm_input_y = confirm_y
        confirm_input_x = confirm_x + deviation

        prompts_y = [username_y, password_y, confirm_y, username_input_y, password_input_y, confirm_input_y]
        prompts_x = [username_x, password_x, confirm_x, username_input_x, username_input_x, confirm_input_x]


        input_windows = create_input_windows(stdscr,prompts,prompts_y,prompts_x)
        dimensions = create_menu_box(stdscr,10,70)


        buttons = create_buttons(stdscr, button_positions, button_texts)
        
        user_boxes = [ input_windows[0], input_windows[1], input_windows[2], buttons[0], buttons[0] ]

        input_positions = [ 
                (prompts_y[3], prompts_x[3]),
                (prompts_y[4], prompts_x[4]),
                (prompts_y[5], prompts_x[5]),
                (button_y[0], button_x[0]),
                (button_y[1], button_x[1]),
        ]


        stdscr.addstr(prompts_y[0], prompts_x[0], prompts[0], curses.color_pair(2))
        stdscr.addstr(prompts_y[1], prompts_x[1], prompts[1], curses.color_pair(2))
        stdscr.addstr(prompts_y[2], prompts_x[2], prompts[2], curses.color_pair(2))
        stdscr.refresh()


        curses.echo()

        #username_input = input_windows[0].getstr().decode('utf-8')
        #password_input = input_windows[1].getstr().decode('utf-8')
        #confirm_input = input_windows[2].getstr().decode('utf-8')


        key = stdscr.getch()

        
        


        #if key == 9:
        #    current_button = (current_button + 1) % len(input_positions)
        #    curses.curs_set(1)
        #    stdscr.addstr(1, 40, "Here.........", curses.color_pair(2))
        #    stdscr.move(input_positions[current_button][0], input_positions[current_button][1])
        #    stdscr.refresh()

        #put logic here for determining what to do with the inputs
        #if username_input != "" and password_input != "" and confirm_input !="" and password_input == confirm_input :
            #bool_var = False
            #stdscr.clear()
