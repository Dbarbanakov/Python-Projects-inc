from time import time
from os import path
from datetime import date


# Time

start_time = time()


def get_time():
    """Returns time passed since the start of the game."""
    return int(time() - start_time)


def get_chronometer():
    """Returns time in a 0:00 format as minutes to seconds."""
    current_time = get_time()
    return "{:0d}:{:02d}".format(current_time // 60, current_time % 60)


# Time

# Scores

scores_file = f"{path.dirname(__file__)}/files/high_scores.txt"


def read_score():
    """Reads the file, returning a list of each line."""
    with open(scores_file, "r") as scores:
        return scores.readlines()


def append_score(score, user):
    """Adds a new line at the end of the file."""
    score_line = f"{0} {user}({get_time()}) {score} {date.today()}\n"
    with open(scores_file, "a") as scores:
        scores.write(score_line)


def format_score():
    """Takes the score file as a list of lines, returns sorted list by points."""
    scores_list = read_score()

    # key: value - points: line w/o number
    box = {int(line.split()[2].strip()): line[1:] for line in scores_list}

    # sorts by key till 10th element, if there is 11th, it cuts it
    box_sorted = {key: box[key] for key in sorted(box, reverse=True)[:10]}

    # returns sorted list of lines with concatenated number in front of each line
    return [
        f"{count} {value}" for count, value in enumerate(box_sorted.values(), start=1)
    ]


def write_score():
    """Writes the formatted score to the file, overwriting the old one."""
    scores_list = format_score()

    with open(scores_file, "w") as scores:
        scores.writelines(scores_list)


# Scores
