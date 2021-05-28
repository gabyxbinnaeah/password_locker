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
       
       

   

if __name__ == "__main__":
    unittest.main()