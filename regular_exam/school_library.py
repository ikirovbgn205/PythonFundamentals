shelf_of_books = input().split("&")

action = input().split(" | ")

while action[0] != "Done":

    if action[0] == "Add Book":
        book_name = action[1]
        if book_name not in shelf_of_books:
            shelf_of_books.insert(0, book_name)

    elif action[0] == "Take Book":
        book_name = action[1]
        if book_name in shelf_of_books:
            shelf_of_books.remove(book_name)

    elif action[0] == "Swap Books":
        first_book, second_book = action[1], action[2]
        if first_book in shelf_of_books and second_book in shelf_of_books:
            first_book_index = shelf_of_books.index(first_book)
            second_book_index = shelf_of_books.index(second_book)
            shelf_of_books[first_book_index], shelf_of_books[second_book_index] = shelf_of_books[second_book_index], shelf_of_books[first_book_index]

    elif action[0] == "Insert Book":
        book_name = action[1]
        if book_name not in shelf_of_books:
            shelf_of_books.append(book_name)

    elif action[0] == "Check Book":
        index = int(action[1])
        if index in range(len(shelf_of_books)):
            print(shelf_of_books[index])

    action = input().split(" | ")

print(", ".join(shelf_of_books))