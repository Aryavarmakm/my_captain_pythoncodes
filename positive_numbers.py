List1=[]
n=int(input("Enter the size of the list"))
for i in range(n):
  e=int(input("Enter element of the list"))
  List1.append(e)
  print ("Positive numbers in",list1,"are: ")
for i in List1:
  if i>=0:
    print(i,end=" ")
 
 
 
 OUTPUT
 Enter the size of the list 5 
 Enter element of the list 12
 Enter element of the list -7
 Enter element of the list 5
 Enter element of the list 64
 Enter element of the list -14
 Positive numbers in [12,-7,5,64,-14] are: 
 12 5 64 
