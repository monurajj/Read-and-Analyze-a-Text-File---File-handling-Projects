def read_file(filename):
    sol = []
    with open("data.txt", "r") as fd:
        book_list = fd.readlines()
        for item in book_list:
            sol.append(item.strip().split(", "))

    return sol


def calculate_average_price(books):
    total_price = sum(float(book[1]) for book in books)
    avg_price = total_price / len(books)
    return avg_price

    




