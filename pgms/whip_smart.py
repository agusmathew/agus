accountDB = {}
accountList = []
Ad_DB = {}

class Account:
	def __init__(self,name,email,password):
		self.name = name
		self.email = email
		self.password = password
	def post_an_ad(self):
		req = raw_input("enter your requirement:")
		if self.name in Ad_DB:
			Ad_DB[self.name].append(req)
		else:
			Ad_DB[self.name] = [req]
	def my_ads(self):
		for ad in Ad_DB[self.name]:
			print ad,'\n'
class TutorAccount(Account):
	def view_ad(self):
		print Ad_DB.values()




def createAccount():
	name = raw_input("Enter your name: ")
	email = raw_input("Enter your email: ")
	
	while True:	
		password = raw_input("Enter your pasword: ")
		confirm_password = raw_input("Re-enter your pasword: ")
		if password == confirm_password:
			typeofaccount = input("1.Student\n2.Tutor")
			if typeofaccount == 1:

				accountObject = Account(name,email,password)
				accountDB[name]=[accountObject]
				print "account created successfully"
				break
			elif typeofaccount == 2:
				accountObject = TutorAccount(name,email,password)
				accountDB[name]=[accountObject]
				print "tutor account created successfully"
				break
		else:
			print "password mismatch"

while True:
	home = input("1.Create Account\n2.Student Login\n3.Tutor Login\n4.Post an Ad")
	if home == 1:
		createAccount()
	if home == 2:
		name = raw_input("Enter your name: ")
		if name in accountDB.keys():
			password_check = raw_input("Enter your pasword: ")
			if password_check == accountDB[name][0].password:
				print "logged in successfully"
				while True:
					do = input("1.Post an ad\n2.My Ads\n3.back")
					if do == 1:
						accountDB[name][0].post_an_ad()
					elif do == 2:
						accountDB[name][0].my_ads()
					elif do == 3:
						break

			else:
				print "no pw"
		else:
			print "no"