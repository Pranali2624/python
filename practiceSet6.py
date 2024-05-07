# write the program using numbers function to find greatest of three numbers 
def numbers(a,b,c):
   if a>b and a>c: 
    print(a, "is greater")
   elif b>a and b>c:
    print(b,"is greter ")
   else:
    print(c, "is greater")

numbers(2,5,7)
  
  # Write a python program  using function to convert Celsius to lo fahrenheit

def celsfah(c):
  f=(c*9/5)+32
  print("the fahrenhite is",f)

celsfah(5)

# How do you prevent a python print() function to print ve new line at the end.
print("hello",end=" ")
print("world")
