

def toggle_panel_visibility(boolean, window, *keys):
    for key in keys:
        window[key].update(visible=boolean)


def get_stars(values):
    for k, v in values.items():
        if v == True:
            return k + 1
