from user_class import User
from credential_class import Credential

def create_user(first_name, last_name, email, password):
    '''
    creates new user
    '''

    new_user= User(first_name, last_name, email, password)

    return new_user
    
