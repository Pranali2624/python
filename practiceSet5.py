# Write a program to print multiplication table of a user input number using for loop
i=int(input("enatera number want to print table:"))
for a in range(1,11):
  print(i,"X",a,"=",i*a)
  
  # Write a program to greet all the person names Stored in list l1 and which starts with S
  # l₁ = [" Harry", "Saham", "Sachin", "Rabul"]

l1 = [" Harry", "Saham", "Sachin", "Rabul"]
for l1 in l1:
  if l1.startswith("S"):
    print("Hello " + l1)

# Write a program to print multiplication table of a user input number using for while loop
i=int(input("enter a number want to print a table"))
a=1
while a<=10:
  print(i,"X",a,"=",i*a)
  a=a+1


# Write a program to find whether a given number prime or not
i=int(input("enter a number"))
if i>1:
  for a in range(2,i):
    if i%a==0:
      print(i,"is a prime number")
      break
# # Write a program to find the sum of first n natural numbers using while loop.
i=int(input("enter a number"))
a=1
sum=0
while a<=i:
 sum=sum+a
 a=a+1
print(sum)

# # Write a program to calculate the factorial of A given number using for loop.
i=int(input("enter a number"))
a=1
fact=1
while a<=i:
  fact=fact*a
  a=a+1
print(fact)

# Write a program to print the following star pattern using for loop       
#                *
#                * *
#                * * *

i=0
while i<=3:
  print(i*"*")
  i=i+1

# Write a program n to print multiplication using for loop in reversed order
i=int(input("enter a number"))
for a in range(10,0,-1):
  print(i,"X",a,"=",(i*a))
  
