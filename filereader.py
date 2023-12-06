def read_file(filename):
    sol = []
    with open("data.txt", "r") as fd:
        book_list = fd.readlines()
        for item in book_list:
            sol.append(item.split(", "))

    return sol


def calculate_average_price(books):
    s=0
    for i in books:
        s += int(i[0])
    avg = s/len(books)
    return avg

    




