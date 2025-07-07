# deleting vowels form string and print remaining string
str = input("enter a string")
for i in  str:
  if i=="a" or i=="e" or i =="i" or i=="o" or i=="u":
   continue
  elif i.isalpha():
      print(i)
