import curses
from create_main_screen import create_main_screen_interface
from create_main_screen import setup_interface
from functions_boxes import create_menu_box
from functions_buttons import create_buttons
from functions_buttons import draw_buttons
from functions_colors import init_colors
from functions_string_input import draw_input_boxes
from functions_string_input import clear_input_box
from functions_string_input import handle_input

def init_curses():
    curses.curs_set(0)

def main(stdscr):
    # Initialize curses
    init_curses()
    stdscr.clear()
    stdscr.refresh()
    
    create_main_screen_interface(stdscr)

curses.wrapper(main)
