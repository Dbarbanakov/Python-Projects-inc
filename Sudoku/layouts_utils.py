import PySimpleGUI as sg


def generate_button(i, j, text=" "):
    return sg.B(
        text,
        size=(4, 2),
        key=(i, j),
        pad=(0, 0),
        border_width=2,
        font=("Helvetica", 10, "bold"),
        auto_size_button=False,
    )


def generate_options(options):
    buttons = []
    for i in range(len(options)):
        buttons.append(
            sg.B(
                f"{options[i]}",
                size=(4, 2),
                pad=(0, 0),
                border_width=2,
                font=("Helvetica", 10, "bold"),
                auto_size_button=False,
            )
        )
    return buttons


def generate_frame_with_buttons(options):
    return [[sg.Frame("FRAME1", [generate_options(options)], title_location="s")]]
