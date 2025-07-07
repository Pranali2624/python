#sperating alphabets ,nnubers and special chareters form string 
str=input("enter a aplhanumeric with special char string")
alpha=""
num=""
spec=""
for i in str:
    if i.isalpha():
        alpha += i+""
    elif i.isnumeric():
        num += i+""
    elif i=="":
        continue
    else:
        spec += i+""
print("alphabets are:",alpha)
print("numbers in string are:",num)
print("special char in string is:",spec)
