from time import time
from os import path
from datetime import date


hp_sudoku = 81
hp_player = 10

# Time

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


# Time

# Scores

high_scores = f"{path.dirname(__file__)}/files/high_scores.txt"


def get_score(time, hp):
    score = int((hp**2 + 100) / (time - time // 5) * 1000)
    return score


def read_score():
    with open(high_scores, "r") as scores:
        return scores.readlines()


def append_score(score, user):
    formatted_score = f"{user} {score} {date.today()}\n"
    with open(high_scores, "a") as scores:
        scores.write(formatted_score)


def format_score():
    scores = read_score()

    scores_unsorted = {int(line.split()[1].strip()): line for line in scores}

    keys_list = list(scores_unsorted.keys())
    keys_list.sort(reverse=True)

    return {key: scores_unsorted[key] for key in keys_list[:10]}


def write_score():
    score = format_score()
    with open(high_scores, "w") as scores:
        scores.writelines(list(score.values()))


# Scores


def toggle_element_visibility(boolean, window, *keys):
    for key in keys:
        window[key].update(visible=boolean)


def change_button_color(element, color1="black", color2="white"):
    element.update(
        button_color=(
            color1 if element.get_text() in [x for x in range(1, 10)] else color2
        )
    )


