        # 01234567890123
parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])
print(parrot[-5])
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])


print(parrot[0:6])

print(parrot[:6] + parrot[6:])

print(parrot[-4:12])

print(parrot[0:6:2])

number = "9,223;372:036 854,775;807"

seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])



