class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def info(self):
        rented_books = sorted(self.books)
        return ", ".join(rented_books)

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user_if_not_registered(self, user: User):
        for user_record in self.user_records:
            if user_record.user_id == user.user_id:
                return

        self.user_records.append(user)
        self.rented_books[user.username] = {}


    def get_user(self, user_id: int):
        for user in self.user_records:
            if user.user_id == user_id:
                return user
        return None

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if author in self.books_available:
            if book_name in self.books_available[author]:
                self.books_available[author].remove(book_name)
                if user.username not in self.rented_books:
                    self.rented_books[user.username] = {}
                self.rented_books[user.username].update({book_name: days_to_return})
                user.books.append(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"
            else:
                for username, data in self.rented_books.items():
                    for book, days in data.items():
                        if book == book_name:
                            return f'The book "{book_name}" is already rented and will be available in {days} days!'
        else:
            return f'No books found for the author {author}!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            self.rented_books[user.username].pop(book_name)
            self.books_available[author].append(book_name)
            user.books.remove(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"


class Registration:
    def __init__(self):
        pass

    def add_user(self, user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)
            return f"Successfully registered user - {user}!"

        return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
            return f"Successfully removed user - {user}!"

        return f"We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        user = library.get_user(user_id)
        if user is not None:
            if user.username != new_username:
                user.username = new_username
                if user.username in library.rented_books:
                    library.rented_books[new_username] = library.rented_books.pop(user.username)
                return f"Username successfully changed to: {new_username} for user id: {user_id}"
            else:
                return "Please check again the provided username - it should be different than the username used so far!"
        else:
            return f"There is no user with id = {user_id}!"


user = User(12, 'Peter')
library = Library()
registration = Registration()
registration.add_user(user, library)
print(registration.add_user(user, library))
registration.remove_user(user, library)
print(registration.remove_user(user, library))
registration.add_user(user, library)
print(registration.change_username(2, 'Igor', library))
print(registration.change_username(12, 'Peter', library))
print(registration.change_username(12, 'George', library))

[print(f'{user_record.user_id}, {user_record.username}, {user_record.books}') for user_record in library.user_records]

library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
                                                'The Prisoner of Azkaban',
                                                'The Goblet of Fire',
                                                'The Order of the Phoenix',
                                                'The Half-Blood Prince',
                                                'The Deathly Hallows']})
library.get_book('J.K.Rowling', 'The Deathly Hallows', 17, user)
print(library.books_available)
print(library.rented_books)
print(user.books)
print(library.get_book('J.K.Rowling', 'The Deathly Hallows', 10, user))
print(library.return_book('J.K.Rowling', 'The Cursed Child', user))
library.return_book('J.K.Rowling', 'The Deathly Hallows', user)
print(library.books_available)
print(library.rented_books)
print(user.books)
