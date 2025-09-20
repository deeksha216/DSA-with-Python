import time

n1 = int(input("Enter first value of n: "))
n2 = int(input("Enter second value of n: "))
n3 = int(input("Enter third value of n: "))

for n in [n1, n2, n3]:
    start = time.time()

    total = 0
    for i in range(n):
        total += i  

    end = time.time()

    print(f"Time taken for n = {n} is {end - start:.6f} seconds")
