from user import User

def user_index(users, user_id):
    #Return the index of the user, or None if the user is not found
    for index, user in enumerate(users):
        if user.id == user_id:
            return index
    return None