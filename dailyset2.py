x=int (input("enter value of x co-ordinate"))
y=int (input("enter value of x co-ordinate"))
if x==0 and y==0 :
  print("co-ordinates on the origin")
elif x>0 and y>0 :
  print("co-ordinates are in 1st Quadrant")
elif x<0 and y>0 :
    print("co-ordinates are in 2nd Quadrant") 
elif x<0 and y<0 :
    print("co-ordinates are in 3rd Quadrant")
elif x>0 and y<0 :
    print("co-ordinates are in 4th Quadrant")
