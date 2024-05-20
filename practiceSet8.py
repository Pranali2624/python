# Write a program to create a dictionary of Hindi words with values as their english translation 

hindi_to_english = {'बिली':'cat ','कुता':'dog','पंछि':'bird'}
print(hindi_to_english.items())

# Write a program to input eight numbers from the user and display all the uaique numbers (ones)
a=set()
for i in range (8):
  n=int(input("Enter a number:" ))
  a.add(n)
print(a)
