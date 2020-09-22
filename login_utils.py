import pickle


class Users:
    def __init__(self, file_name):
        self.file = file_name
        self.users = []

    def add_user(self, username, password):
        self.users.append(Account(username, password))

    def remove_user(self, username):
        self.users.remove(self._get_user(username))

    def change_password(self, username, new_password):
        self._get_user(username).change_password(new_password)

    def is_user_valid(self, username, password):
        if self.is_user(username):
            return self._get_user(username).password == password
        return False

    def is_user(self, username):
        if self._get_user(username) == "not found":
            return False
        return True

    def store(self):
        file = open(self.file, "wb")
        pickle.dump(self, file)

    def _get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return "not found"


class Account:
    def __init__(self, username, password):
        self.username, self.password = username, password

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def change_password(self, new_password):
        self.password = new_password
