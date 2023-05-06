from os import path
from datetime import date

high_scores = f"{path.dirname(__file__)}/files/high_scores.txt"


def get_score(time, hp):
    score = int((hp**2 + 100) / (time - time // 5) * 1000)
    return score


def append_score(score, user):
    formatted_score = f"{user} {score} {date.today()}\n"
    with open(high_scores, "a") as scores:
        scores.write(formatted_score)


def read_score():
    with open(high_scores, "r") as scores:
        return scores.readlines()


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
