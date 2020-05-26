a=0XFACE
print(type(a))

print(True+True)
print(False*False)

a= 10
b= 10
c= 10

print(id(a))
print(id(b))
print(id(c))

c=11

print(id(c))

#True, False, None
#if, elif, else
#and, or, Not, in
#while, for, break, continue, return, in, yield
#try, except, finally, raise, assert
# import, as, from, class, def, pass, global, nonlocal, lambda, del, with

a=12
print(bin(a))


a=0B1010
print(hex(a))

b= True


str1 = "vijay"
str2 = 'vijay'
str3= '''class is defined in "double" and 'single quotes' '''
print(str3)


str1 = "vikramviswanath"
print(str1[-4:])

a= 10+20j
b= 10+20j
print(id(a))
print(id(b))

l = [10,'durga',20,10,30]
print(type(l))
print(l[0])
print(l[-1])
print(l[1:4])

l=[]
print(type(l))
l.append(10)
l.append(20)
l.append(20)
l.append(10)
l.append(30)
print(l)
l.remove(10)
print(l)

l = (10,20,30,40,10,'durga')
print(type(l))
print(l)
print(l[0])
print(l[-1])

t = (10,)
print(type(t))

s = {10,20,30,'durga',10}
print(type(s))
print(s)
s.add(50)
s.remove(30)
print(s)

s= {}
print(type(s))


s = set()
print(type(s))
print(s)

s={10,20,30,40,'durga'}
s1=s
print(type(s))
print(s)
print(s1)
s.add(45)
print(s)
print(s1)


s = {10,20,30,40}
fs = frozenset(s)
print(type(fs))
print(fs)