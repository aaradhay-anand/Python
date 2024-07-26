from library import Library
from user import User

def main():
    global username
    is_user_in = False

    lib = Library()
    lib.add_book(1, "Harry Potter", "J.K. Rowling", "Fiction", "Harry Potter is a series of seven fantasy novels written by British author J. K. Rowling.")
    lib.add_book(2, "The Da Vinci Code", "Dan Brown", "Mystery", "The Da Vinci Code is a 2003 mystery thriller novel by Dan Brown.")

    user = User()

    print("Welcome to the library!")
    user_input = int(input("Enter 1 to Sign in\nEnter 2 to Sign up\n"))

    if user_input == 1:
        username = input("Enter your Username\n")
        password = input("Enter your Password\n")
        is_user_in = user.sign_in(username, password)
    elif user_input == 2:
        username = input("Enter your Username\n")
        password = input("Enter your Password\n")
        if user.sign_up(username, password):
            is_user_in = user.sign_in(username, password)
            print("You were auto signed in.")

    if is_user_in:
        while True:
            print("\nYou can:")
            print("1. Search for a book")
            print("2. Check out a book")
            print("3. Return a book")
            print("4. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                book_title = input("Enter the title of the book you want to search for:\n")
                book_info = lib.search_book(book_title)
                if book_info:
                    print(book_info)
                else:
                    print("Sorry, the book is not available in the library.")
            elif choice == 2:
                book_title = input("Enter the title of the book you want to check out:\n")
                success, message = lib.check_out_book(book_title, username)
                print(message)
            elif choice == 3:
                book_title = input("Enter the title of the book you want to return:\n")
                success, message = lib.return_book(book_title, username)
                print(message)
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")
    else:
        print("Sorry, you must sign in first.")

if __name__ == "__main__":
    main()
