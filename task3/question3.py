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
        print("\nAlready in library")
    else:
        books.append(book)
        print("\nBook added.\n")

def remove_book():
    title = input("\nEnter the title of book to remove: ")

    for book in books:
        if book[0] == title:
            books.remove(book)
            print("\nBook removed successfully")
            break
        else:
            print("\nBook not found")

def display_book():
    if not books:
        print("\nThere are no books")
    else:
        print("\nCurrent book is: ")
        for book in books:
            print(f"\nTitle: {book[0]} by Author: {book[1]}\n")

while True:
    help()
    command = input("\nEnter a command: ").lower()

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
        print("Invalid command.\n")