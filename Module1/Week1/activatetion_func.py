import math


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def activate_function():
    x = input("Input x: ")
    if not is_number(x):
        print('x must be a number')
        return

    x = float(x)
    activation_function = input(
        "Input activation function (sigmoid|relu|elu): ").lower()

    if activation_function == 'sigmoid':
        result = 1 / (1 + math.exp(-x))
        print(f'sigmoid: f({x}) = {result}')
    elif activation_function == 'relu':
        result = max(0, x)
        print(f'relu: f({x}) = {result}')
    elif activation_function == 'elu':
        alpha = 0.01
        result = x if x > 0 else alpha * (math.exp(x) - 1)
        print(f'elu: f({x}) = {result}')
    else:
        print(f'{activation_function} is not supported')


if __name__ == "__main__":
    activate_function()
