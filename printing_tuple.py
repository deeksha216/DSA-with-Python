list = []
for x in range(4):
    num = int(input("Enter a number:"))
    list.append(num)

tuple = tuple(list)

for x in tuple:
    print(x)