# Helper functions for the events


def toggle_element_visibility(boolean, window, *keys):
    for key in keys:
        window[key].update(visible=boolean)


def get_number_of_stars(values):
    for k, v in values.items():
        if v == True:
            return k + 1


def change_button_color(element, color1, color2):
    if element.get_text() in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        element.update(button_color=color1)
    else:
        element.update(button_color=color2)
