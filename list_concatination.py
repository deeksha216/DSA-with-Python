list1 = []
for x in range(4):
    num = int(input("Enter a number:"))
    list1.append(num)


list2 = []
for x in range(4):
    al = str(input("Enter a Alphabet:"))
    list2.append(al)
print(list1)
print(list2)

list = list1 + list2
print(list)