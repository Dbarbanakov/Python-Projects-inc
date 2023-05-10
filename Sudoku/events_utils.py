from time import time
from os import path
from datetime import date


hp_sudoku = 81
hp_player = 10
consequences = 0

# Time

start_time = time()


def get_time():
    return int(time() - start_time)


def get_chronometer():
    current_time = get_time()
    return "{:0d}:{:02d}".format(current_time // 60, current_time % 60)


# Time

# Scores

high_scores_txt = f"{path.dirname(__file__)}/files/high_scores.txt"


def read_score():
    with open(high_scores_txt, "r") as scores:
        return scores.readlines()


def append_score(score, user):
    score_line = f"{0} {user}({get_time()}) {score} {date.today()}\n"
    with open(high_scores_txt, "a") as scores:
        scores.write(score_line)


def format_score():
    scores = read_score()

    scores_unsorted_dict = {int(line.split()[2].strip()): line for line in scores}

    keys_list = list(sorted(scores_unsorted_dict.keys(), reverse=True))

    scores_sorted_dict = {key: scores_unsorted_dict[key] for key in keys_list[:10]}
    scores_sorted_list = list(scores_sorted_dict.values())

    formatted_score = [
        (f"{x+1} " + scores_sorted_list[x][1:]) for x in range(len(scores_sorted_list))
    ]

    return formatted_score


def write_score():
    score_list = format_score()

    with open(high_scores_txt, "w") as scores:
        scores.writelines(score_list)


# Scores


def toggle_element_visibility(boolean, window, *elements):
    for element in elements:
        window[element].update(visible=boolean)


def change_button_color(element, color1="black", color2="white"):
    element.update(
        button_color=(color1 if element.get_text() in range(1, 10) else color2)
    )
