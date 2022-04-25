import unittest
# import pyperclip
from user_credentials import User, Credential

# Test class that defines test cases for the user class behaviours.
class TestUser(unittest.TestCase):
	
		# Args: unittest.TestCase: helps in creating test cases
	
	# Function to create a user account before each test
	def setUp(self):
		
		self.new_user = User('Abishag','Maitha','pendomaitha')

	# Test to if check the initialization/creation of user instances is properly done
	def test__init__(self):
	
		self.assertEqual(self.new_user.first_name,'Abishag')
		self.assertEqual(self.new_user.last_name,'Maitha')
		self.assertEqual(self.new_user.password,'pendomaitha')

	def test_save_user(self):
		
		self.new_user.save_user()
		self.assertEqual(len(User.users_list),1)

# Test class that defines test cases for the credentials class behaviours.
class TestCredentials(unittest.TestCase):
	
	# Args: unittest.TestCase: helps in creating test cases
	
	def test_check_user(self):
		
		self.new_user = User('Abishag','Maitha','pendomaitha')
		self.new_user.save_user()
		user2 = User('Tz','Maitha','pendomaitha')
		user2.save_user()

		for user in User.users_list:
			if user.first_name == user2.first_name and user.password == user2.password:
				current_user = user.first_name
		return current_user

		self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))

	# Function to create an account's credentials before each test
	def setUp(self):
		
		self.new_credential = Credential('Pendo','Instagram','pendo_maitha','pendomaitha')

	# Test to if check the initialization/creation of credential instances is properly done
	def test__init__(self):
		
		self.assertEqual(self.new_credential.user_name,'Pendo')
		self.assertEqual(self.new_credential.site_name,'Instagram')
		self.assertEqual(self.new_credential.account_name,'pendo_maitha')
		self.assertEqual(self.new_credential.password,'pendomaitha')

	def test_save_credentials(self):
		
		self.new_credential.save_credentials()
		twitter = Credential('Abishag','Twitter','abishag_pendo','pendomaitha')
		twitter.save_credentials()
		self.assertEqual(len(Credential.credentials_list),2)

	# Function to clear the credentials list after every test
	def tearDown(self):
		
		Credential.credentials_list = []
		User.users_list = []

	# Test to check if the display_credentials method, displays the correct credentials.
	def test_display_credentials(self):
		
		self.new_credential.save_credentials()
		twitter = Credential('Abishag','Twitter','abishag_pendo','pendomaitha')
		twitter.save_credentials()
		instagram = Credential('Pendo','Instagram','pendo_maitha','pendomaitha')
		instagram.save_credentials()
		self.assertEqual(len(Credential.display_credentials(twitter.user_name)),2)

	def test_find_by_site_name(self):
		'''
		Test to check if the find_by_site_name method returns the correct credential
		'''
		self.new_credential.save_credentials()
		twitter = Credential('Abishag','Twitter','abishag_pendo','pendomaitha')
		twitter.save_credentials()
		credential_exists = Credential.find_by_site_name('Twitter')
		self.assertEqual(credential_exists,twitter)

	# def test_copy_credential(self):
		
		# Test to check if the copy a credential method copies the correct credential
		
		# self.new_credential.save_credentials()
		# twitter = Credential('Abishag','Twitter','abishag_pendo','pendomaitha')
		# twitter.save_credentials()
		# find_credential = None
		# for credential in Credential.user_credentials_list:
		# 		find_credential =Credential.find_by_site_name(credential.site_name)
		# 		return pyperclip.copy(find_credential.password)
		# Credential.copy_credential(self.new_credential.site_name)
		# self.assertEqual('pendomaitha',pyperclip.paste())
		# print(pyperclip.paste())

if __name__ == '__main__':
	unittest.main(verbosity=2)