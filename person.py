class User:
    def __init__(self, id, username, password, user_firstname, user_lastname, user_deleted):
        self.id = id
        self.username = username
        self.password = password
        self.firstname = user_firstname
        self.lastname = user_lastname
        self.deleted = user_deleted


class Account:
    def __init__(self, id, account_firstname, account_lastname, deposit, activation, deleted):
        self.id = id
        self.firstname = account_firstname
        self.lastname = account_lastname
        self.deposit = deposit
        self.activation = activation
        self.deleted = deleted

class UserForLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

