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


def  credentials_display():
    '''
    function that returns all credentials saved
    '''
    return Credentials.display_credential()

def password_generated():
    '''
    function that generates random password
    '''
    return Credentials.password_generator()


def main():
    print("Welcome to password locker online saftey store for your passwords with end-t-end encryption")
    
    short_code=input("Enter ca  to create user account....:").upper()

    while short_code!='CA':
        print("invalid option")
        short_code=input("Enter cu  to create user account....:").upper()
        
    else:
        f_name=input("Enter your first name...:") 
        l_name=input("Enter your last name....:")
        email=input("Enter your email...:")
        password=input("Enter your password...:")

  
        saves_user(create_user(f_name, l_name, email, password))

        print('\n')
        print(f"Welcome {f_name} {l_name} , kindly proceed to create your credentials")
        print('\n')

        while True:
            short_code=input("use these short codes: cc -create credentials account, del -delete credentials, fc -find credentials, dc -display credential, gp-generates password...:=>").upper()
            if short_code=="CC":
                social_media_account=input("Enter your social media account name...: =>")
                social_media_username=input("Enter your social media username...:=>")
                social_media_password=input("Enter your social media password..:=>")
                

                saves_credentials(generate_credentials(social_media_account,social_media_username,social_media_password))

                print('\n')
                print(f"Your account =>: {social_media_account} of username =>: {social_media_username} credentials have been created and stored with end-to-end encryption")
                print('\n')

            elif short_code=="DC":

                if credentials_display():
                    print("Here is a list of your credentials")
                    print('\n')

                    for credential in credentials_display():
                         print(f"User account...:{credential.account} username...:{credential.username} and user password...:{credential.password}")
                         print('\n')

                else :
                    print("\n")
                    print("You dont have any store credential")
                    print('\n')

            



 




if __name__ == "__main__":
    main()
