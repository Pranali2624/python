# program in python for fiboacci serice 
def febo(num):
  if num == 0 or num == 1 :
    return num
  else:
    return febo(num-1) + febo(num-2)
print(febo(6))
