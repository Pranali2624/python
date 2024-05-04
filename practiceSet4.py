# Write a program to find greatest of four numbers entered by the user
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the therid number:"))
d=int(input("Enter the fourth number:"))
if a>b and a>c and a>d:
  print("The gretest number is",a)
elif b>a and b>c and b>d:
  print("the gretest number is",b)
elif c>a and c>b and c>d:
  print("The gretest number is ",c)
else:
  print("The gretest number is ",d)

# Write a brogram to find out whether a student is pass or fail, if it requires total 40% and at least 33%, in each subject to pass. Assume pass Subjects and take marks as an input from the user.

a=int(input("Enter the marks of the first   subject:"))
b=int(input("Enter the marks of the second subject:"))
c=int(input("Enter the marks of the therid subject:"))
d=int(input("Enter the marks of the fourth subject:"))
if a>33 and b>33 and c>33 and d>33 and a+b+c+d>120:
  print("you are pass")
else:
  print("you are fail")
  
# A spam comment is definded as a teat Containsing following Reywords: "make a lot of money" "buy now", "Subscribe this, "click this". Write a program to detect these spams.


a=input("Enter the text:")
if "make a lot of money" in a or "buy now" in a or "subscribe this" in a or "click this" in a :
  print("This is a spams")
else:
  print("this is not a spam, you are safe")

# Write a program to find whether a given username Contains less than 10 characters or not.

a=input("Enter  your username:")
if len(a)<10:
  print("your username is less then 10 characters")
else:
  print("your username is more then 10 characters")

# Write a program which finde out whether a given name is present in a list or not.
str=("pranali","apurva","aniket")
a=input("Enter your name")
if a in str:
  print("your name is present in a list")
else:
  print("your name is not present in a list")


# Write a program to calculate the grade of a Student from Scheme: his marks from the following
# 90-100 → Ex
# 80-90 →A
# 70-80 → B
# 60-70 →C
# 50-60 - D
# 40-50 - F

a=int(input("Enter your marks:"))
if a>90 and a<100:
  print("your grade is excellence")
elif a>80 and a<90:
  print("your garde is A")
elif a>70 and a<80:
  print("your garde is B")
elif a>60 and a<70:
  print("your grade is C")
elif a>50 and a<60:
  print("your grade is D")
else:
  print("your grade is F")

# Write a program to find out whether a given post is talking about "Harry" or not.

a=input("enter a post:")
if "harry" in a:
  print("this post is talking about harry")
else:
  print("this post is not takling about harry")

