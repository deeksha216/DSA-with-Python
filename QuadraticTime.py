import time

def quadratic_time(n):
    print(f"\n0(n2) for n = {n}")
    start = time.time()
    for i in range(n):
        for j in range(n):
            pass
    end = time.time()
    print(f"Time taken: {end - start} seconds")

quadratic_time(200)
quadratic_time(400)
quadratic_time(800)
