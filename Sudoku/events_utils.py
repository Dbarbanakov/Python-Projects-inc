from time import time
from os import path
from datetime import date


HP_BOARD = 81
HP_PLAYER = 10
COMBO = 0


# Time

start_time = time()


def get_time():
    return int(time() - start_time)


def get_chronometer():
    current_time = get_time()
    return "{:0d}:{:02d}".format(current_time // 60, current_time % 60)


# Time

# Scores

high_scores_file = f"{path.dirname(__file__)}/files/high_scores.txt"


def read_score():
    with open(high_scores_file, "r") as scores:
        return scores.readlines()


def append_score(score, user):
    score_line = f"{0} {user}({get_time()}) {score} {date.today()}\n"
    with open(high_scores_file, "a") as scores:
        scores.write(score_line)


def format_score():
    scores = read_score()

    box = {int(line.split()[2].strip()): line for line in scores}

    box_sorted = {key: box[key] for key in sorted(box, reverse=True)[:10]}

    formatted_score = [
        f"{x+1} {list(box_sorted.values())[x][1:]}" for x in range(len(box_sorted))
    ]

    return formatted_score


def write_score():
    score_list = format_score()

    with open(high_scores_file, "w") as scores:
        scores.writelines(score_list)


# Scores
