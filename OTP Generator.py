import random
generator=random.randint(000000,100000)
username=input("Username: ")
print("Hellow!", username)
print('Here is your OTP for login', generator)
password=input("Enter OTP to login: ")
if password==str(generator):
    print("Login Successful!")
else:
    print("Wrong OTP")