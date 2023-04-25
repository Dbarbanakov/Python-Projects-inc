import PySimpleGUI as sg
import os


def health_bar(name,max,colors):
    return sg.ProgressBar(
        max,
        orientation="h",
        key=f"-HEALTH-{name}-",
        bar_color=colors,
        expand_y=True,
        visible=False,
        size=(21),
    )


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
                " ",
                key=options[i],
                image_source=f"{os.path.dirname(__file__)}/images/{options[i]}.png",
            )
        )
    return buttons


def generate_frame_with_buttons(options):
    return [[sg.Frame(" ----- ", [generate_options(options)], title_location="s")]]


def frame_layout_stars(number=5):
    frame = []
    for i in range(number):
        frame.append(
            sg.Image(
                f"{os.path.dirname(__file__)}/images/star.png",
                key=f"star{i+1}",
                visible=False,
            )
        )
    frame.append(sg.B("Rate me",key='-RATE-', visible=False))
    return frame


def frame_layout_stars_radio(radios=5):
    frame = []
    for i in range(radios):
        frame.append(sg.Radio(f"{i+1}", "-RADIO-STARS-",enable_events=True))
    return frame
