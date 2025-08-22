name=input("enter u name: ")
password=input("enter u password: ")

name.lower()
name=name.split()
name="-".join(name)

print("the user name is : "+name+"\nthe user password length : "+str(len(password)))

print("Is the password length is greater than or equal to 8? "+str(len(password)>=8))
print("Is the username is \"admin\"? "+str(name=="admin"))
print("Is the password is\"1234\"? "+str(password=="1234"))
print("Is it a default account? "+str((name=="admin")&(password=="1234")))

print(F"welcome {name}!, your password length is: {len(password)} ")
