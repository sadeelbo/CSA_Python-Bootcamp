
name=input("enter u name: ")

info=input("enter u info: ")

with open("info.txt","w")as f:
   f.write(info)

with open("info.txt","r")as f:
   print(name+"\'s info is: "+f.read())

