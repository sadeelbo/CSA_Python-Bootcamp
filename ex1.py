
print("enter u name: ")
name=input()

print("enter u info: ")
info=input()

with open("info.txt","w")as f:
   f.write(name)
   f.write(info)

with open("info.txt","r")as f:
   print(f.read())
   print(f.read())




