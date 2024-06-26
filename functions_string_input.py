import curses
from functions_colors import init_colors


def handle_input(stdscr, key, current_button, inputs_, input_positions, write):
    
    if write == 1:
        inputs_[current_button] = inputs_[current_button] + chr(key)
    
    if current_button == 0:
        stdscr.addstr(input_positions[0][0], input_positions[0][1], inputs_[current_button], curses.color_pair(2))
        stdscr.addstr(input_positions[1][0], input_positions[1][1], inputs_[1], curses.color_pair(2))
        stdscr.addstr(input_positions[2][0], input_positions[2][1], inputs_[2], curses.color_pair(2))
        stdscr.move(input_positions[0][0], input_positions[0][1] + len (inputs_[current_button]))
        
    elif current_button == 1:
        stdscr.addstr(input_positions[0][0], input_positions[0][1], inputs_[0], curses.color_pair(2))
        stdscr.addstr(input_positions[1][0], input_positions[1][1], inputs_[current_button], curses.color_pair(2))
        stdscr.addstr(input_positions[2][0], input_positions[2][1], inputs_[2], curses.color_pair(2))
        stdscr.move(input_positions[1][0], input_positions[1][1] + len (inputs_[current_button]))
            
    elif current_button == 2:
        stdscr.addstr(input_positions[0][0], input_positions[0][1], inputs_[0], curses.color_pair(2))
        stdscr.addstr(input_positions[1][0], input_positions[1][1], inputs_[1], curses.color_pair(2))
        stdscr.addstr(input_positions[2][0], input_positions[2][1], inputs_[current_button], curses.color_pair(2))
        stdscr.move(input_positions[2][0], input_positions[2][1] + len (inputs_[current_button]))
    
    stdscr.refresh()


def draw_button_input_boxes(button_positions, input_states, input_values, button_texts):
    for i, state in enumerate(input_states):
        if state:
            input_win = curses.newwin(3, 40, button_positions[i][0] + 3, button_positions[i][1] - 10)
            input_win.clear()
            input_win.border()
            input_win.addstr(1, 1, f"{button_texts[i]}: {input_values[i]}")
            input_win.refresh()

def clear_input_box(button_positions, i):
    if i >= 0:
        input_win = curses.newwin(3, 40, button_positions[i][0] + 3, button_positions[i][1] - 10)
        input_win.clear()
        input_win.refresh()


def create_input_windows(stdscr,prompts,prompts_y, prompts_x):

    init_colors(stdscr)
    input_windows= []
    
    #Creates an input window for each box
    for i in range (len(prompts)) :
        
        #input_win = curses.newwin(1, (curses.COLS -len(prompts[i]) - 1) // 4 , prompts_y[i], prompts_x[i] + (len(prompts[i])))
        input_win = curses.newwin(1, 20 , prompts_y[i], prompts_x[i] + (len(prompts[i])))
        input_win.bkgd(curses.color_pair(1))
        input_windows.append(input_win)
    
    return input_windows
