# Getting Max Over Kernel
def main():
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    sub_list = []
    result_list = []

    for element in num_list:
        sub_list.append(element)

        if len(sub_list) == k:
            print(sub_list)
            result_list.append(max(sub_list))
            del sub_list[0]

    print("Result:", result_list)


if __name__ == "__main__":
    main()
