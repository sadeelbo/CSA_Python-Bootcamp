arr=["apple","grape","melon","banana","cherry"]
print(arr)
print("the first fruit is: "+arr[0])
print("the last fruit is: "+arr[-1])
arr[1]="mango"
print(arr)
arr.insert(2,"Watermelon")

cheack=input("enter fruit u want to find: ")
cheack=cheack.strip().lower()
print(cheack+"\'s number is : "+str(arr.count(cheack)))   # بضل يطلع عندي صفر لما اكتب العنصر التاني ف الليست مش عارفة ليه 

arr.sort()
print(arr)



