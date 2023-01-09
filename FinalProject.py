class Client:
    def __init__(self, name, id_no):
        self.name = name
        self.id_no = id_no


class Librarian:
    def __init__(self, name, id_no):
        self.name = name
        self.id_no = id_no


class Book:
    def __init__(self, title, author, isbn, status):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status


class BorrowOrder:
    def __init__(self, book, client, order_id):
        self.book = book
        self.client = client
        self.order_id = order_id


clients = []
librarians = []
books = []
orders = []


user_type = input("Are you a client or librarian? Enter 'client' or 'librarian': ")
if user_type == "client":
        name = input("Enter your name: ")
        id_no = input("Enter your ID number: ")
        new_client = Client(name, id_no)
        clients.append(new_client)
        user_type = input("Are you a client or librarian? Enter 'client' or 'librarian': ")

        if user_type == "librarian":
          name = input("Enter your name: ")
          id_no = input("Enter your ID number: ")
          new_librarian = Librarian(name, id_no)
          librarians.append(new_librarian)

        while len(books) < 3:
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            status = input("Enter the status of the book ('active' or 'inactive'): ")
            new_book = Book(title, author, isbn, status)
            books.append(new_book)

        print("\nAll books:")
        for book in books:
            print(f"Title: {book.title} | Author: {book.author} | ISBN: {book.isbn} | Status: {book.status}")

        borrow_book = input("\nWhich book do you want to borrow? Enter the title: ")

        for book in books:
            if book.title == borrow_book:
                if book.status == "active":
                    id_no = input("Enter your ID number: ")
                    client_exists = False
                    for client in clients:
                        if client.id_no == id_no:
                            client_exists = True
                            selected_client = client
                            break

                    if client_exists:
                        order_id = len(orders) + 1
                        new_order = BorrowOrder(book, client, order_id)
                        orders.append(new_order)
                        print(f"Borrow order created: Order ID = {order_id} | Book = {book.title} | Client = {client.name}")
                    else:
                        print("Client does not exist in the system. Borrow order not created.")


#                    to search for orders
search_id = input("Enter the order ID to search for: ")
order_found = False
for order in orders:
    if orders == search_id:
        order_found = True
        print(f"Order found: Order ID = {order.order_id} | Book = {order.book.title} | Client = {order.client.name}")
        break

if not order_found:
    print("Order not found.")


print("All orders:")
for order in orders:
    print(f"Order ID = {order.order_id} | Book = {order.book.title} | Client = {order.client.name}")
