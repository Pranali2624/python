# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour

import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp=time.strftime('%S')
print(timestamp)
if(int(timestamp)>=5 and int(timestamp)<12):
 print("Good morning")
elif(int(timestamp)>12 and int(timestamp)<16):
  print("Good afternppn")
elif(int(timestamp)>16 and int(timestamp)<20):
  print("Good Evening")
else:
  print("Good night  ")
  
 
