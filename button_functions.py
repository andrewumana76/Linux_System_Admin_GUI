import curses

def create_buttons(stdscr, button_positions, button_texts):
    buttons = [curses.newwin(3, 20, pos[0], pos[1]) for pos in button_positions]
    draw_buttons(buttons, button_texts, 0)
    return buttons

def draw_buttons(buttons, button_texts, current_button):
    for i, button_win in enumerate(buttons):
        button_win.clear()
        button_win.border()
        if i == current_button:
            button_win.addstr(1, 1, button_texts[i], curses.A_REVERSE)
        else:
            button_win.addstr(1, 1, button_texts[i])
        button_win.refresh()
