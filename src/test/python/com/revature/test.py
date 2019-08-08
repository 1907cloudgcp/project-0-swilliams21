#!/usr/bin/env python3
import src.main.python.com.revature.service.business as business
import random
'''
This is your main testing script, this should call several other testing scripts on its own
'''
def main():
	# print('TO-DO')
	print("Test Cases")

	# open
	b = business.business(runbool=False)

	#create a test user
	username = randomInput()
	password = randomInput()
	print("Username: " + username)
	print("Password: " + password)
	b.querry_register(username, password)

	# test 01
	# check failed login
	# it thows an error when login fails so this is using a try catch block to detect the error
	a = "no crash"
	assert a == "no crash"
	try:
		#note input is 21 characters and all test cases up to this point are 20 characters or 5. It is almost impossible for a user with 21 characters to exist
		b.querry_login("aaaaaaaaaaaaaaaaaaaaaaaaaa", "a")
	except:
		a = "crash"
	assert a == "crash"
	assert a != "no crash"

	# test 02
	# check login
	b.querry_login(username, password)
	assert b.user == username
	# assert b.user == "fred"
	assert b.user != "fred"

	# test 03
	# failed withdraw
	# assumption: login successful
	# assumption: user exists
	# assumption: account is 0$
	b.querry_deposite(100)
	assert b.money == 100
	b.querry_withdraw(200)
	# money assumably should be the same because of failed login
	assert b.money == 100

	# test 04
	# successful withdraw
	# note: I was too lazy to instantiate a another user
	# assumption: test 03 should have money set to 100
	b.querry_withdraw(50)
	assert b.money == 50
	b.querry_withdraw(50)
	assert b.money == 0

	# test 05
	# duplicate user registration
	a = "no crash"
	assert a == "no crash"
	try:
		b.querry_register(username, password)
	except:
		a = "crash"
	assert a == "crash"
	assert a != "no crash"

def randomInput():
	a = ""
	l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	for i in range(20):
		a = a + str(random.choice(l))
	return a

if __name__ == '__main__':
	main()