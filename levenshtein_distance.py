# Levenshtein distance
def levenshtein_distance(source, target):
    matrix = [[0 for _ in range(len(target) + 1)]
              for _ in range(len(source) + 1)]

    for i in range(len(source) + 1):
        matrix[i][0] = i
    for j in range(len(target) + 1):
        matrix[0][j] = j

    for i in range(1, len(source) + 1):
        for j in range(1, len(target) + 1):
            if source[i - 1] == target[j - 1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + cost)

    return matrix[len(source)][len(target)]


source = "kitten"
target = "sitting"

if __name__ == '__main__':
    print(levenshtein_distance(source, target))
