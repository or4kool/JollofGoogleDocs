import re
import hashlib
from User import Users

class Signup:
    def __init__(self, firstname = '', lastname ='', password = '', email ='', gender = '', birthday = '', phonenumber = '', location = ''):
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.email = email
        self.gender = gender
        self.birthday = birthday
        self.phonenumber = phonenumber
        self.location = location
        
    
    def collect_user_info(self):
        user_data = {}
        user_info = ['first name', 'last name', 'username', 'password', 'birthday', 'gender', 'phone number', 'email', 'location']
        for info_item in user_info:
            user_data[info_item] = input("Please enter your {}: ". format(info_item))
            if info_item == 'password':
                while not self.validate(user_data['password']):
                    user_data[info_item] = input("Please enter your {} again: ". format(info_item))
            elif info_item == 'email':
                while not re.match(r"[^@]+@[^@]+\.[^@]+", user_data[info_item]):
                    print("Make sure your email address is a valid email address.")                    
                    user_data[info_item] = input("Please enter your {} again: ". format(info_item))
                
        print(user_data)

        return user_data


    def validate(self, password):
        if len(password) < 8:
            print("Make sure your password is at lest 8 letters")
        elif re.search('[0-9]',password) is None:
            print("Make sure your password has a number in it")
        elif re.search('[A-Z]',password) is None: 
            print("Make sure your password has a Capital Letter in it")
        else:
            return True

class Login:
    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    def new_user(self, user):
        signin_credentials = {}
        signin_info = ['email', 'password']

        for user_data in signin_info:
            signin_credentials[signin_info] = input("please enter your {}: ".format(signin_info))
        result = user.authenticate(signin_credentials)

        while not result:
            for user_data in signin_info:
                print("Wrong email or password")
                signin_credentials[signin_info] = input("please enter your {}: ".format(signin_info))
            result = user.authenticate(signin_credentials)
            
        # call kab's module

userpass = Signup()
userpass.collect_user_info()
# userpass.validate()
