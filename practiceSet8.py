# Write a program to create a dictionary of Hindi words with values as their english translation 

hindi_to_english = {'बिली':'cat ','कुता':'dog','पंछि':'bird'}
print(hindi_to_english.items())

# Write a program to input eight numbers from the user and display all the uaique numbers (ones)
a=set()
for i in range (8):
  n=int(input("Enter a number:" ))
  a.add(n)
print(a)


# Can we have a set with 18 (int) and "18(str) as a values in it?
a ={18,"18"}
print(a)

# What will be the length of following set 5.
S= set ()
S.add(20)
S.add(20.0)
S.add("20") 
# # => Length of & after these operation?
print(len(S))

# what is the type of S
S={}
print(type(S))

# Can you change the values inside a is contained in set S list which

S= {8, 7, 12, "Harry", " [1,2]"}
print(S)
