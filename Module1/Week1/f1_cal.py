# Calculating F1-Score
import random
import math


def cal_f1(tp, fp, fn):
    # Check input == int
    if not isinstance(tp, int):
        print('tp must be int')
        return
    if not isinstance(fp, int):
        print('fp must be int')
        return
    if not isinstance(fn, int):
        print('fn must be int')
        return

    # Check input != 0
    if tp <= 0 or fp <= 0 or fn <= 0:
        print('tp and fp and fn must be greater than zero')
        return

    # Precision, Recall and F1-score
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * precision * recall / (precision + recall)

    # Print results
    print(f'precision is {precision}')
    print(f'recall is {recall}')
    print(f'f1-score is {f1_score}')


if __name__ == "__main__":
    cal_f1(2, 1, 4)
