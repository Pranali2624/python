#list1=[10,20,30,40,50,60,70]
element=int (input("eneter elements for list"))
list1=[elements]

length= len(list1)

if length%2==0:
     print("invalid")
else:
     mis= int(length /2)
     last=length-1
     x=list1[0]

     list1[0]=list1[mis]
     list1[mis]=list1[last]
     list1[last]=x

     print(list1)
