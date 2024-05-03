# write a python program to display a user enterd name followed by good afternoon using input() function
a = input("Enter your name:")
print("Good afternoon ,", a)

# Write a program to fill in a letter template given below with name and date.

# letter = """Dear </NAME/>,
# You are selected!
# </ DATEID/>"""

name="pranali"
date="22/12/2022"
print(""""Dear """, name ,
"""you are selected!""" ,date )

# write a program to detect double spaces in a string 
str="     hii there     "
print(str.find("  "))

# repalce the double spaces with single spaces
str="     hii there     "
print(str.replace("   "," "))

# white a program to format the folowing letter using escape sequence characters.
# letter = "Dear Harry, This Python Course is nice. Thanks!"

letter="Dear Harry ,\n This Python Course is nice. \nThanks! "
print(letter)
      
