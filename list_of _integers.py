list = []
for x in range(4):
    num = int(input("Enter a number:"))
    list.append(num)

print(f"First Elemrnt : {list[0]}")
print(f"Last element : {list[-1]}")

print("All Elements:")
for x in list:
    print(x)

print("Reverse Order: ")
print(list[::-1])