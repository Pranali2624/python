# write the program using numbers function to find greatest of three numbers 
def numbers(a,b,c):
   if a>b and a>c: 
    print(a, "is greater")
   elif b>a and b>c:
    print(b,"is greter ")
   else:
    print(c, "is greater")

numbers(2,8,7)
  
  # Write a python program  using function to convert Celsius to lo fahrenheit

def celsfah(c):
  f=(c*9/5)+32
  print("the fahrenhite is",f)

celsfah(5)

# How do you prevent a python print() function to print ve new line at the end.
print("hello",end=" ")
print("world")

# Write a recursive function to calculate the sum of first n natural numbers
def sum(n):
  if n==1:
    return 1
  else:
    return n+sum(n-1)

print(sum(5))

# Write a python function to print first on lines of the following pattern
# *  *  *
# *  *
# *
# for n=3

def pattern(n):
  for i in range(n,0,-1):
    print("*"*i)

pattern(3)

# Write a python function which converts inches to cms
def inchtocm(inch):
  cm=inch*2.54
  print("the cm is",cm)

inchtocm(5)

# Write a python function to remove a given word from a list and stap it at the same time
def remove(list,word):
  list.remove(word)
  print(list)
list=["hello","world","python"]
remove(list,"world")

# Write a python function to print multiplication table of a given number

def table(n):
  for i in range(1,11):
    print(n,"X",i,"=",n*i)

table(5)

