letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1]
print(backwards)

print(letters[16:13:-1])

print(letters[4::-1])

print(letters[:-9:-1])

print(letters[-4:])

print(letters[:-5:-1])

print(letters[-1:])

print(letters[:1])

print(letters[0])

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"

print(data[::5])
print(data[0:-1:5])
print(data[:-1:5])
print(data[1:5])

days = "Mon, Tue, Wed"
print(days[0:-1:5])
