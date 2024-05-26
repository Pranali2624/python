# Write a program to store seven fruits in a list entered by the user
fruits=[input("Enter fruit 1:"),input("Enter fruit 2:"),input("Enter fruit 3:"),input("Enter fruit 4:"),input("Enter fruit 5:"),input("Enter fruit 6:"),
input("Enter fruit 7:")]
print(fruits)

# Write a program to accept marks of 6 students and display them in a sorted manner
marks=[int(input("Enter marks of student 1:")),int(input("Enter marks of student 2:")),int(input("Enter marks of student 3:")),int(input("Enter marks of student 4:")),int(input("Enter marks of student 5:")),int(input("Enter marks of student 6:"))]
marks.sort()
print(marks)


# Check that a tuple cannot be changed in python
tup=(1,2,3,4,5,6)
tup[0]=0
print(tup)

# Wrik a program to sum a list with 4 numbers.
list=[1,2,3,4]
print(sum(list))

# Write a program to count the number of zeres in the following tuple:

a = (7,0,8,0,0,9)
print(a.count(0))
