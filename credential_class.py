from random import randint
import random

class Credentials:
    '''
    generates credials for users
    '''
    credentialList = []

    def __init__(self,account,username,password):
        '''
        creates instance variables for credentials

        Args:
             account: user account
             username: social medai name
             passsword: user password
        
        '''
        self.account = account
        self.username = username
        self.password = password

    def save_credential(self):
        '''
        function that saves credentials
        '''
        Credentials.credentialList.append(self)



    def delete_credential(self):
        '''
        deletes credential
        '''
        Credentials.credentialList.remove(self)

    @classmethod
    def credential_exist(cls,account):
         '''   
        method that checks if credentials exists from the credentialList
        Args:
             account:account to search if it exists
        Returns:
            Boolean:true or false depending if the credentials exists
        '''
        
         for searchAccount in cls.credentialList:
             if searchAccount.account == account:
                 return True




    @classmethod
    def find_credential_by_account(cls, account):
        '''
        method that takes in account and output accounts credential
        '''
        for searchAccount in cls.credentialList:
            if  searchAccount.account == account:
                return searchAccount


    @classmethod
    def display_credential(cls):
        '''
        display all the saved credentials in contact list
        '''
        return cls.credentialList

   
   
    def password_generator():
        lettersList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        '''
        converting lettersList strings to uppercase
        '''
        lettersListUpper = []
        for item in lettersList:
            letter = item.upper()
            lettersListUpper.append(letter)

        password_generated = []


        password_generated_sliced = ''
        for range in lettersList:
            range = randint(0, 100)
            if range%2 == 0:
                password_generated.append(random.choice(lettersList))
            elif range%5==0 or range%3 == 0:
                password_generated.append(random.choice(lettersListUpper))
            else:
                password_generated.append(str(range))

        password_generated_sliced = password_generated[0:8:1]
        random_password=(''.join(password_generated_sliced))
  
    
        print(f'your password is: {random_password}')


        return random_password


