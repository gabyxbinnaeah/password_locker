import unittest
from credential_classes import Credentials
from user_class import User

class TestClass(unittest.TestCase):
    '''
    define test cases for user and credentials behavior
    '''

    def setUp(self):
        '''
        set up a method to run before each test cases
        '''
        self.new_user=("Caleb","oginga","caleb@ms.com","new21oginga")


    def user_creation(self):
        '''
        method that checks if function creates user 
        '''
        self.assertEual(self.new_user.fname,"Caleb")
        self.assertEual(self.new_user.lname,"oginga")
        self.assertEual(self.new_user.email_address,"caleb@ms.com")
        self.assertEual(self.new_user.password,"new21oginga")