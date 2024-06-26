import curses

def draw_input_boxes(button_positions, input_states, input_values, button_texts):
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

def handle_input(stdscr, button_positions, input_states, input_values, button_texts, current_button):
    curses.curs_set(1)
    input_win = curses.newwin(3, 40, button_positions[current_button][0] + 3, button_positions[current_button][1] - 10)
    input_win.clear()
    input_win.border()
    curses.echo()
    input_win.addstr(1, 1, f"{button_texts[current_button]}: ")
    input_win.refresh()
    input_values[current_button] = input_win.getstr(1, len(button_texts[current_button]) + 2, 30).decode('utf-8')
    curses.noecho()
    input_states[current_button] = False
    curses.curs_set(0)
    clear_input_box(button_positions, current_button)