import csv


class Users:
    """User class:
    creates new users,
    remove users,
    login users,
    Authenticate users"""
    count = 0

    def __init__(self):
        pass

    # create new user
    def create_user(self, user_info):
        self.write_to_file(user_info)

    # Write user data into csv file
    @classmethod
    def write_to_file(cls, file, new='a'):
        with open("user_data.csv", new) as write_user:
            file_header = ['first name', 'last name', 'username', 'password', 'birthday', 'gender', 'phone number', 'email', 'location']
            writer = csv.DictWriter(write_user, fieldnames=file_header)
            if cls.count < 1:
                writer.writeheader()
                cls.count += 1
            writer.writerow(file)

    # Read user data from csv file
    @staticmethod
    def read_from_file():
        with open("user_data.csv") as read_user:
            reader = csv.DictReader(read_user)
            user_data = [data for data in reader]
            return user_data

    # Remove single user through their email
    def remove_user(self, email):
        single_user = self.search_user(email)
        if single_user is not False:
            all_users = self.read_from_file()
            for key, user_data in enumerate(all_users):
                if email in user_data['email']:
                    all_users.pop(key)
                # clear the csv file
                open('user_data.csv', 'w').close()
            for num in range(len(all_users)):
                self.write_to_file(all_users[num])
            return True
        else:
            return "{} does not exist".format(email)

    # search for single user using their email
    def search_user(self, email):
        all_users = self.read_from_file()
        for user_data in all_users:
            if email in user_data['email']:
                return user_data
        else:
            return False

    # Check if user is still logged in via session key
    def check_user_login(self, session_key, email):
        the_user = self.search_user(email)
        if the_user:
            if session_key in the_user:
                return True
            else:
                return False

    # Verify if password and email is correct
    def authenticate_user(self, email, password):
        the_user = self.search_user(email)
        if the_user is not False:
            if email == the_user['email'] and password == the_user['password']:
                return True
            else:
                return False
        else:
            return "{} does not exist".format(email)

