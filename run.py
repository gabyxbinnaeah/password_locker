#!/usr/bin/env python3.6
from user_class import User
from credential_class import Credentials

def create_user(first_name, last_name, email, password):
    '''
    creates new user
    '''

    new_user= User(first_name, last_name, email, password)

    return new_user

def saves_user(user):
    '''
    Function that saves user 
    '''
    user.save_user()

def generate_credentials(account,username,password):
    '''
    function to creates user Credentials
    '''

    new_credential= Credentials(account,username,password)

    return new_credential   

def saves_credentials(credentials):
    '''
    Saves credentials
    '''
    credentials.save_credential()

def delete_credentials(credential):
    '''
    function to delete credentials
    '''
    credential.delete_credential()

def find_credential(account):
    '''
    function that finds credential by account and returns Credentials
    '''
    return Credentials.find_by_account(account)


def main():
    print("Welcome to password locker online saftey store for your passwords with end-t-end encryption")
    
    short_code=input("Enter cu -create user account....:").upper()

if __name__ == "__main__":
    main()
