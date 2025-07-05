# single cot string
name='pranali'
print(name)

# double cot string
lastname="waghmare"
print(lastname)

# triple cot
middelname='''bharat'''
print(middelname)

# indexing
print(name[0])
print(name[2])
print(name[-4]) #negative index -4 is also mean -4+(length of string(7)) =3
print(name[4])

#  string slicing 

a= " hello world "
print(a[0:11])

# string method

print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.replace("world","python"))
print(a.split())

# string formatting

tamplet="hey {} you are great, take your {}$ back"

a="pranali"
a1="10000"
print(tamplet.format(a,a1))

# f string
print(f"hey {a} you are great, take your {a1}$ back")




