import unittest
from credential_class import Credentials
from user_class import User

class TestClass(unittest.TestCase):
    '''
    define test cases for user and credentials behavior
    '''

    def setUp(self):
        '''
        set up a method to run before each test cases
        '''
        self.new_user= User("caleb","oginga","caleb@ms.com","new21oginga")
        self.new_credential= Credentials( 'facebook','gabyxbinnaeh','flavian')


    def tearDown(self):
        '''
        clears the counter after evry test cases
        '''
        Credentials.credentialList=[]


    def test_user_creation(self):
        '''
        method that checks if function creates user 
        '''
        self.assertEqual(self.new_user.first_name,"caleb")
        self.assertEqual(self.new_user.last_name,"oginga")
        self.assertEqual(self.new_user.email_address,"caleb@ms.com")
        self.assertEqual(self.new_user.password,"new21oginga")

    def  test_save_user(self):
         '''
         test if method saves user
         '''
         self.new_user.save_user()
         self.assertEqual(len(User.userList),1)

    def  test_credential_creation(self):
        '''
        checks if method creates credential
        '''

        # self.new_credential= Credentials( 'facebook','gabyxbinnaeh','flavian')

        self.assertEqual(self.new_credential.account,'facebook')
        self.assertEqual(self.new_credential.username,'gabyxbinnaeh')
        self.assertEqual(self.new_credential.password,'flavian')


    def test_save_credentials(self):
        '''
        method that checks for save credentials i
        '''
        self.new_credential= Credentials( 'facebook','gabyxbinnaeh','flavian')


        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credentialList),1)
    


    def test_save_multiple_credentials(self):
        '''
        Checks if user can save multiple credentials 
        '''
        self.new_credential.save_credential()
        test_credential=Credentials('linkedin','gabu','gabu23')
        test_credential.save_credential()

        self.assertEqual(len(Credentials.credentialList),2)
    def test_delete_credentials(self):
        '''
        checks if the delete function deletes the Credentials
        '''
        self.new_credential.save_credential()
        test_credential=Credentials('linkedin','gabu','gabu23')
        test_credential.delete_credential()

        self.assertEqual(len(Credentials.credentialList),1)

        

       

   

if __name__ == "__main__":
    unittest.main()