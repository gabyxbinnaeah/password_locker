class User:
    '''
    generates a new instance of a user 
    '''
    userList=[]

    def __init__(self,fname,lname,email_address,password):
        '''
        initialize properties
        '''
        self.first_name = fname
        self.last_name = lname
        self.email_address = email_address
        self.password = password

    
