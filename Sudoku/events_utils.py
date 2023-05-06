from time import time

hp_sudoku = 81
hp_player = 0

start_time = int(round(time() * 100))


def get_time():
    return int(round(time() * 100)) - start_time


def get_timer():
    return get_time() / 100


def get_chronometer():
    current_time = get_time()
    return "{:0d}:{:02d}".format(
        (current_time // 100) // 60, (current_time // 100) % 60
    )


def toggle_element_visibility(boolean, window, *keys):
    for key in keys:
        window[key].update(visible=boolean)


def get_number_of_stars(values):
    for k, v in values.items():
        if v == True:
            return k + 1


def change_button_color(element, color1="purple", color2="purple"):
    element.update(
        button_color=(
            color1 if element.get_text() in [x for x in range(1, 10)] else color2
        )
    )
