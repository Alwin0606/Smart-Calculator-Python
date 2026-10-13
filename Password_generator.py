import secrets
import string
lenth =int(input("enter password length:"))
if length <8:
  print("password must be at least 8 characters long.")
else:
  characters= string.ascii_letters + string.digits +"!@#$%&*"
  password= '',jion(secrets.choice(characters) for_in range(length))
  print("Your password is : ",password)
