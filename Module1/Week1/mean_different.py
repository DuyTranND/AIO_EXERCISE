def mean_different(y, y_hat, n, p):
    loss = (y**(1 / n) - y_hat**(1 / n))**p
    print(loss)


if __name__ == "__main__":
    mean_different(100, 99.5, 2, 1)
