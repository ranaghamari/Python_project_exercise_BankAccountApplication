import sqlite3
from tkinter import Tk, Entry, Label, Button
from person import User, Account

login_window = Tk()
login_window.title("Login")

with sqlite3.connect("BankApplication.db") as connection:
        cursor = connection.cursor()
        data = cursor.execute("""
        SELECT user_name,
               password
        FROM Users;""").fetchall()
print(data)

user_label = Label(login_window, text="Username")
user_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

user_entry = Entry(login_window, width=20)
user_entry.grid(row=0, column=1, pady=10, padx=(0,10), sticky="e", columnspan=2)

password_label = Label(login_window, text="Password")
password_label.grid(row=1, column=0, pady=10, padx=10, sticky="w")

password_entry = Entry(login_window, width=20)
password_entry.grid(row=1, column=1, pady=10, padx=(0,10), sticky="e", columnspan=2)

def identification():
    user_input = user_entry.get()
    password_input = int(password_entry.get())
    res_input = (user_input, password_input)
    my_res = data
    if res_input in my_res:
        main_window = Tk()
        main_window.title("Bank Application (Users page)")

        def show_user_form(id=None, username="", password="", user_firstname="", user_lastname="", user_deleted=""):
            newuser_window = Tk()
            if id:
                newuser_window.title("Update User")

            else:
                newuser_window.title("Create User")

            newusername_label = Label(newuser_window, text="Username")
            newusername_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

            newusername_entry = Entry(newuser_window, width=20)
            newusername_entry.insert(0, username)
            newusername_entry.grid(row=0, column=1, pady=10, padx=10, sticky="w", columnspan=2)

            newpassword_label = Label(newuser_window, text="Password")
            newpassword_label.grid(row=1, column=0, pady=10, padx=10, sticky="w")

            newpassword_entry = Entry(newuser_window, width=20)
            newpassword_entry.insert(0, password)
            newpassword_entry.grid(row=1, column=1, pady=10, padx=10, sticky="w", columnspan=2)

            newfirstname_label = Label(newuser_window, text="First name")
            newfirstname_label.grid(row=2, column=0, pady=10, padx=10, sticky="w")

            newfirstname_entry = Entry(newuser_window, width=20)
            newfirstname_entry.insert(0, user_firstname)
            newfirstname_entry.grid(row=2, column=1, pady=10, padx=10, sticky="w", columnspan=2)

            newlastname_label = Label(newuser_window, text="Last name")
            newlastname_label.grid(row=3, column=0, pady=10, padx=10, sticky="w")

            newlastname_entry = Entry(newuser_window, width=20)
            newlastname_entry.insert(0, user_lastname)
            newlastname_entry.grid(row=3, column=1, pady=10, padx=10, sticky="w", columnspan=2)

            newdeleted_label = Label(newuser_window, text="Deletion")
            newdeleted_label.grid(row=4, column=0, pady=10, padx=10, sticky="w")

            newdeleted_entry = Entry(newuser_window, width=10)
            newdeleted_entry.insert(0, user_deleted)
            newdeleted_entry.grid(row=4, column=1, pady=10, padx=10, sticky="w", columnspan=2)

            def submit():
                username = newusername_entry.get()
                password = int(newpassword_entry.get())
                firstname = newfirstname_entry.get()
                lastname = newlastname_entry.get()
                deleted = newdeleted_entry.get()

                if id:
                    update_user(id, username, password, firstname, lastname, deleted)
                else:
                    insert_user(username, password, firstname, lastname, deleted)

                newuser_window.destroy()
                create_table_body()

            def insert_user(username, password, firstname, lastname, deleted):
                with sqlite3.connect("BankApplication.db") as connection:
                    cursor = connection.cursor()
                    cursor.execute(f"""
                    INSERT INTO Users (
                                user_name,
                                password,
                                user_first_name,
                                user_last_name,
                                user_deleted
                          )
                          VALUES (
                              '{username}',
                               {password},
                              '{firstname}',
                              '{lastname}',
                              '{deleted}'
                          );""")
                    connection.commit()

            def update_user(id, username, password, firstname, lastname, deleted):
                with sqlite3.connect("BankApplication.db") as connection:
                    cursor = connection.cursor()
                    cursor.execute(f"""
                    UPDATE Users
                    SET    user_name = '{username}',
                           password = {password},
                           user_first_name = '{firstname}',
                           user_last_name = '{lastname}',
                           user_deleted = '{deleted}'
                    WHERE user_id = {id}""")
                    connection.commit()

            newuser_submit_button = Button(newuser_window, text="Submit", command=submit)
            newuser_submit_button.grid(row=4, column=2, pady=10, padx=10, sticky="e")

            newuser_window.mainloop()

        new_user_button = Button(main_window, text="New User", command=show_user_form)
        new_user_button.grid(row=0, column=1, pady=10, padx=0, sticky="w")

        def create_table_header():
            row_label = Label(main_window, text="NO")
            row_label.grid(row=1, column=0, sticky="w")

            username_label = Label(main_window, text="Username")
            username_label.grid(row=1, column=1, sticky="w")

            password_label = Label(main_window, text="Password")
            password_label.grid(row=1, column=2, sticky="w")

            userfirstname_label = Label(main_window, text="First name")
            userfirstname_label.grid(row=1, column=3, sticky="w")

            userlastname_label = Label(main_window, text="Last name")
            userlastname_label.grid(row=1, column=4, sticky="w")

            userdeletion_label = Label(main_window, text="Deleted")
            userdeletion_label.grid(row=1, column=5, sticky="w")

        create_table_header()

        def load_users_data():
            users_list = []
            with sqlite3.connect("BankApplication.db") as connection:
                cursor = connection.cursor()
                data = cursor.execute("""
        SELECT user_id,
               user_name,
               password,
               user_first_name,
               user_last_name,
               user_deleted
        FROM Users;""").fetchall()

                for item in data:
                    users_item = User(item[0], item[1], item[2], item[3], item[4], item[5])
                    users_list.append(users_item)

                return users_list

        entry_list = []

        def create_table_body():
            for entry in entry_list:
                entry.destroy()

            entry_list.clear()

            users_list = load_users_data()

            row_number = 1
            for users_item in users_list:
                row_entry = Entry(main_window, width=5)
                row_entry.insert(0, row_number)
                row_entry.grid(row=row_number + 1, column=0)
                row_entry.config(state="readonly")
                entry_list.append(row_entry)

                username_entry = Entry(main_window, width=10)
                username_entry.insert(0, users_item.username)
                username_entry.grid(row=row_number + 1, column=1)
                username_entry.config(state="readonly")
                entry_list.append(username_entry)

                password_entry = Entry(main_window, width=10)
                password_entry.insert(0, users_item.password)
                password_entry.grid(row=row_number + 1, column=2)
                password_entry.config(state="readonly")
                entry_list.append(password_entry)

                firstname_entry = Entry(main_window, width=10)
                firstname_entry.insert(0, users_item.firstname)
                firstname_entry.grid(row=row_number + 1, column=3)
                firstname_entry.config(state="readonly")
                entry_list.append(firstname_entry)

                lastname_entry = Entry(main_window, width=10)
                lastname_entry.insert(0, users_item.lastname)
                lastname_entry.grid(row=row_number + 1, column=4)
                lastname_entry.config(state="readonly")
                entry_list.append(lastname_entry)

                deleted_entry = Entry(main_window, width=10)
                deleted_entry.insert(0, users_item.deleted)
                deleted_entry.grid(row=row_number + 1, column=5)
                deleted_entry.config(state="readonly")
                entry_list.append(deleted_entry)

                update_button = Button(main_window, text="Update",
                                       command=lambda id=users_item.id,
                                                      username=users_item.username,
                                                      password=users_item.password,
                                                      firstname=users_item.firstname,
                                                      lastname=users_item.lastname,
                                                      deleted=users_item.deleted:
                                       show_user_form(id, username, password, firstname, lastname, deleted))
                update_button.grid(row=row_number + 1, column=6)

                row_number += 1

        create_table_body()

        def show_accounts():
            accounts_window = Tk()
            accounts_window.title("Accounts")

            def create_account_table_header():
                row_label = Label(accounts_window, text="NO")
                row_label.grid(row=1, column=0, sticky="w")

                accountfirstname_label = Label(accounts_window, text="First name")
                accountfirstname_label.grid(row=1, column=1, sticky="w")

                accountlastname_label = Label(accounts_window, text="Last name")
                accountlastname_label.grid(row=1, column=2, sticky="w")

                deposit_label = Label(accounts_window, text="Deposit")
                deposit_label.grid(row=1, column=3, sticky="w")

                activation_label = Label(accounts_window, text="Activation")
                activation_label.grid(row=1, column=4, sticky="w")

                deletion_label = Label(accounts_window, text="Deleted")
                deletion_label.grid(row=1, column=5, sticky="w")

            create_account_table_header()

            def load_accounts_data():
                accounts_list = []
                with sqlite3.connect("BankApplication.db") as connection:
                    cursor = connection.cursor()
                    data = cursor.execute("""
            SELECT account_id,
                   account_first_name,
                   account_last_name,
                   deposit,
                   activation,
                   deleted
            FROM   Accounts;""").fetchall()

                    for account_item in data:
                        accounts_item = Account(account_item[0], account_item[1], account_item[2], account_item[3],
                                                account_item[4], account_item[5])
                        accounts_list.append(accounts_item)

                return accounts_list

            account_entry_list = []

            def create_account_table_body():
                for account_entry in account_entry_list:
                    account_entry.destroy()

                account_entry_list.clear()

                accounts_list = load_accounts_data()

                def create_new_acount(id=None, firstname="", lastname="", deposit="", activation="", deleted=""):
                    newaccount_window = Tk()
                    newaccount_window.title("Create new account")

                    newaccount_firstname_label = Label(newaccount_window, text="First name")
                    newaccount_firstname_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

                    newaccount_firstname_entry = Entry(newaccount_window, width=15)
                    newaccount_firstname_entry.insert(0, firstname)
                    newaccount_firstname_entry.grid(row=0, column=1, pady=10, padx=10, sticky="w", columnspan=2)

                    newaccount_lastname_label = Label(newaccount_window, text="Last name")
                    newaccount_lastname_label.grid(row=1, column=0, pady=10, padx=10, sticky="w")

                    newaccount_lastname_entry = Entry(newaccount_window, width=15)
                    newaccount_lastname_entry.insert(0, lastname)
                    newaccount_lastname_entry.grid(row=1, column=1, pady=10, padx=10, sticky="w", columnspan=2)

                    newaccount_deposit_label = Label(newaccount_window, text="Deposit")
                    newaccount_deposit_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

                    newaccount_deposit_entry = Entry(newaccount_window, width=10)
                    newaccount_deposit_entry.insert(0, deposit)
                    newaccount_deposit_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

                    newactivation_label = Label(newaccount_window, text="Activation[Y/N]")
                    newactivation_label.grid(row=3, column=0, pady=10, padx=10, sticky="w")

                    newactivation_entry = Entry(newaccount_window, width=10)
                    newactivation_entry.insert(0, activation)
                    newactivation_entry.grid(row=3, column=1, pady=10, padx=10)

                    newdeletion_label = Label(newaccount_window, text="Deleted[Y/N]")
                    newdeletion_label.grid(row=4, column=0, pady=10, padx=10, sticky="w")

                    newdeletion_entry = Entry(newaccount_window, width=10)
                    newdeletion_entry.insert(0, deleted)
                    newdeletion_entry.grid(row=4, column=1, pady=10, padx=10)

                    def submit_new_account():
                        newaccount_firstname = newaccount_firstname_entry.get()
                        newaccount_lastname = newaccount_lastname_entry.get()
                        newacoount_deposit = int(newaccount_deposit_entry.get())
                        newaccount_activation = newactivation_entry.get()
                        newaccount_deletion = newdeletion_entry.get()

                        if id:
                            update_account(id, newaccount_firstname, newaccount_lastname, newacoount_deposit,
                                           newaccount_activation, newaccount_deletion)
                        else:
                            insert_account(newaccount_firstname, newaccount_lastname, newacoount_deposit,
                                           newaccount_activation, newaccount_deletion)

                        newaccount_window.destroy()
                        create_account_table_body()

                    def insert_account(newaccount_firstname, newaccount_lastname, newacoount_deposit,
                                       newaccount_activation, newaccount_deletion):
                        with sqlite3.connect("BankApplication.db") as connection:
                            cursor = connection.cursor()
                            cursor.execute(f"""
                            INSERT INTO Accounts (
                                 account_first_name,
                                 account_last_name,
                                 deposit,
                                 activation,
                                 deleted
                             )
                             VALUES (
                                 '{newaccount_firstname}',
                                 '{newaccount_lastname}',
                                 {newacoount_deposit},
                                 '{newaccount_activation}',
                                 '{newaccount_deletion}'
                             );""")
                            connection.commit()

                    def update_account(id, newaccount_firstname, newaccount_lastname, newaccount_deposit,
                                       newaccount_activation, newaccount_deletion):
                        with sqlite3.connect("BankApplication.db") as connection:
                            cursor = connection.cursor()
                            cursor.execute(f"""
                            UPDATE Accounts
                            SET   account_first_name = '{newaccount_firstname}',
                                  account_last_name = '{newaccount_lastname}',
                                  deposit = '{newaccount_deposit}',
                                  activation = '{newaccount_activation}',
                                  deleted = '{newaccount_deletion}'
                            WHERE account_id = {id}""")

                    newaccount_submit_button = Button(newaccount_window, text="Submit", command=submit_new_account)
                    newaccount_submit_button.grid(row=5, column=2, pady=10, padx=10, sticky="e")

                new_account_button = Button(accounts_window, text="New Account", command=create_new_acount)
                new_account_button.grid(row=0, column=0, pady=10, padx=10, sticky="e")

                account_row_number = 2
                for accounts_item in accounts_list:
                    account_row_entry = Entry(accounts_window, width=20)
                    account_row_entry.insert(0, account_row_number - 1)
                    account_row_entry.grid(row=account_row_number + 1, column=0)
                    account_row_entry.config(state="readonly")
                    account_entry_list.append(account_row_entry)

                    account_firstname_entry = Entry(accounts_window, width=10)
                    account_firstname_entry.insert(0, accounts_item.firstname)
                    account_firstname_entry.grid(row=account_row_number + 1, column=1)
                    account_firstname_entry.config(state="readonly")
                    account_entry_list.append(account_firstname_entry)

                    account_lastname_entry = Entry(accounts_window, width=10)
                    account_lastname_entry.insert(0, accounts_item.lastname)
                    account_lastname_entry.grid(row=account_row_number + 1, column=2)
                    account_lastname_entry.config(state="readonly")
                    account_entry_list.append(account_lastname_entry)

                    account_deposit_entry = Entry(accounts_window, width=10)
                    account_deposit_entry.insert(0, accounts_item.deposit)
                    account_deposit_entry.grid(row=account_row_number + 1, column=3)
                    account_deposit_entry.config(state="readonly")
                    account_entry_list.append(account_deposit_entry)

                    account_activation_entry = Entry(accounts_window, width=10)
                    account_activation_entry.insert(0, accounts_item.activation)
                    account_activation_entry.grid(row=account_row_number + 1, column=4)
                    account_activation_entry.config(state="readonly")
                    account_entry_list.append(account_activation_entry)

                    account_deletaion_entry = Entry(accounts_window, width=10)
                    account_deletaion_entry.insert(0, accounts_item.deleted)
                    account_deletaion_entry.grid(row=account_row_number + 1, column=5)
                    account_deletaion_entry.config(state="readonly")
                    account_entry_list.append(account_deletaion_entry)

                    account_update_button = Button(accounts_window, text="Update",
                                                   command=lambda id=accounts_item.id,
                                                                  firstname=accounts_item.firstname,
                                                                  lastname=accounts_item.lastname,
                                                                  deposit=accounts_item.deposit,
                                                                  activation=accounts_item.activation,
                                                                  deleted=accounts_item.deleted:
                                                   create_new_acount(id, firstname, lastname, deposit, activation,
                                                                     deleted))
                    account_update_button.grid(row=account_row_number + 1, column=6)

                    account_row_number += 1

            create_account_table_body()

            accounts_window.mainloop()

        show_accounts_button = Button(main_window, text="Show accounts", command=show_accounts)
        show_accounts_button.grid(row=0, column=2, pady=10, padx=0, sticky="w")

        main_window.mainloop()

    else:
        res_label = Label(login_window, text="wrong")
        res_label.grid(row=2, column=1, pady=10, padx=10)

    return res_label

login_button = Button(login_window, text="Login", command=identification)
login_button.grid(row=2, column=2, pady=10, padx=(0,20), sticky="e")





login_window.mainloop()

