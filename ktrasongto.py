import math

n = int(input("Nhập một số: "))

if n < 2:
    print(f"{n} is NOT PRIME number!")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False

    if is_prime:
        print(f"{n} is PRIME number!")
    else:
        print(f"{n} is NOT PRIME number!")
