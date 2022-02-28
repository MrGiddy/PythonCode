# Special book categorization program,
# assigns each book a special code based on its title.

# This code creates file with some book titles in each line
file = open("books.txt", "w+")
file.write("Harry Potter\nThe Hunger Games\nPride and Prejudice\nGone with the Wind\nSome book\nAnother book")
file.close()

# This code creates a list with contents of each line as an element
with open("books.txt", "r") as file:
    raw_file_list = file.readlines()

    # removes "\n" from list elements
    file_list = []
    for i in raw_file_list:
        file_list.append(i.rstrip("\n"))

    # accesses each book title in file, and prints their special code
    n = 0
    while n < len(file_list):
        book_title = file_list[n]
        n += 1
        print(book_title[0] + str(len(book_title)))

    # alternative to while loop
    # for line in file_list:
    #     print(line[0] + str(len(line)))
