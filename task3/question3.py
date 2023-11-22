books = []
def help():
    print("Read these instruction:")
    print("add -> add a book to inventory")
    print("display -> display the current books in inventory")
    print("remove -> remove the book from the inventory")
    print("exit -> exit the program")

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")

    book = [title, author]

    if book  in books:
        print("Already in library")
    else:
        books.append(book)
        print("Book added.")

def remove_book():
    title = input("Enter the title of book to remove: ")

    for book in books:
        if book[0] == title:
            books.remove(book)
            print("Book removed successfully")
            break
        else:
            print("Book not found")

def display_book():
    if not books:
        print("There are no books")
    else:
        print("Current book is: ")
        for book in books:
            print(f"Title: {book[0]}, Author: {book[1]}")

while True:
    help()
    command = input("Enter a command: ").lower()

    if command == "add":
        add_book()
    elif command == "remove":
        remove_book()
    elif command == "display":
        display_book()
    elif command == "exit":
        confirm = input("Are you sure you want to exit? (yes/no): ").lower()
        if confirm == "yes":
            print("Exiting the program")
            break
    else:
        print("Invalid command.")