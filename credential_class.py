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




