
# for loop
for i in range(1,6):
    print(i)

for a in range(1,11):
    print("5 x", a,"=", 5*a)


fruits =["banana","apple","mango"]

for fruit in fruits:
    print(fruit)

# while loop

i=1
while i<=5:
    print(i)
    i=i+1

# break loop 

i=1 
for i in range(1,6):
    if i==3:
        break
    print(i)

# continue loop 
a=1
for a in range (1,7):
    if a==4:
        continue
    print(a)

# pass keyword
c=1
for c in range (1,4):
    if c==2:
        pass

print ("end of program")