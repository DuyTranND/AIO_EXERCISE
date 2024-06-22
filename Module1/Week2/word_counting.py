# Word Counting
def word_count(file_path):
    f = open(file_path)
    f = f.read()
    lis = f.lower().split()
    unit = set([str(elem) for elem in lis])
    dic = {}
    for i in unit:
        lis.count(i)
        dic[i] = lis.count(i)
    return dic


file_path = "F:\AIO\AIO_Homework\Module1\Week2\Exercise\P1_data.txt"

if __name__ == "__main__":
    print(word_count(file_path))
