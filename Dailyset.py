x="pranali waghmare"
print(type(x))
length = len (x)
countv = 0
countc = 0
print(length)
for y in x:
    if y== "a" or y== "i" or y== "e" or y== "o" or y== "u":
        print("vowel are =",y)
        countv += 1
       
    elif y.isalpha() :
        print("const are=",y)
        countc +=1
    
print("total count vowels",countv)
print("total count of const", countc)
