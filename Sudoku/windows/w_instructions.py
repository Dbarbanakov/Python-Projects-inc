import PySimpleGUI as sg
import os

instructions = f"{os.path.dirname(__file__)}/../files/instructions.txt"

layout_instructions = [
    [sg.MLine(key="-ML1-" + sg.WRITE_ONLY_KEY, size=(40, 8))],
    [sg.Button("Go"), sg.Button("Exit")],
]

window_instructions = sg.Window("Window Title", layout_instructions)



# while True:
#     event, values = window_instructions.read()
#     if event in (sg.WIN_CLOSED, "Exit"):
#         break
#     if event == "Go":
#         with open(instructions, "r") as lines:
#             for line in lines.readlines():
#                 window_instructions["-ML1-" + sg.WRITE_ONLY_KEY].print(
#                     line.strip(), text_color="red"
#                 )


