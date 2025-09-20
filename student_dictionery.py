dict = {}

new_Entries =int(input("Enter the number of new entries: "))

for i in range(new_Entries):
    name = input("Enter the name of the student: ")
    roll_no = int(input("Enter the roll number of the student: "))
    dict[name]=roll_no

print(dict)



