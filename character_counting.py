# Character Counting
def main():
    character_statistic = {}

    word = 'members'

    for char in word:
        if char in character_statistic:
            character_statistic[char] += 1
        else:
            character_statistic[char] = 1

    print(character_statistic)


if __name__ == "__main__":
    main()
