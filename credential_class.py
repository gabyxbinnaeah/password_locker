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


