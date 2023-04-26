import os
from datetime import date

high_scores = f"{os.path.dirname(__file__)}/files/high_scores.txt"


def print_file():
    with open(high_scores, "r") as scores:
        for line in scores.readlines():
            print(line)


def get_score(time, hp):
    score = int((hp**2 + 100) / (time - time // 5) * 1000)
    return score


def write_score(score, user):
    formatted_score = f"{user} {score} {date.today()}\n"
    with open(high_scores, "a") as scores:
        scores.write(formatted_score)


def read_score():
    with open(high_scores, "r") as scores:
        return scores.readlines()


def format_score():
    scores_unsorted = {}

    with open(high_scores, "r") as scores:
        for line in scores.readlines():
            key = int(line.split()[1].strip())
            scores_unsorted[key] = line

    keys_list = list(scores_unsorted.keys())
    keys_list.sort(reverse=True)

    scores_sorted = {key: scores_unsorted[key] for key in keys_list[:10]}

    with open(high_scores, "w") as scores:
        scores.writelines(list(scores_sorted.values()))
