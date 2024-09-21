from user import User

def add_user(users):
    name = input("Enter the name of the user: ")
    users.append(User(name))
    
def view_user_details(users):
    user_id = get_valid_user_id(users)
    find_user_index = user_index(users, user_id)
    if find_user_index is None:
        print("User not found.")
        return False
    print(f"Name: {users[find_user_index].name}")
    print(f"ID: {users[find_user_index].id}")
    print("Borrowed Books:")
    for book in users[find_user_index].borrowed_books:
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"Genre: {book.genre}")
        print(f"Publication Date: {book.publication_date}")
    print()

def display_users(users):
    for user in users:
        print(f"Name: {user.name}")
        print(f"ID: {user.id}")
        print()
        
def user_index(users, user_id):
    #Return the index of the user, or None if the user is not found
    for index, user in enumerate(users):
        if user.id == user_id:
            return index
    return None

def get_valid_user_id():
    while True:
        user_id = input("Enter the ID of the user: ")
        if user_id.isdigit():
            return int(user_id)
        print("Invalid user ID. Please try again.")