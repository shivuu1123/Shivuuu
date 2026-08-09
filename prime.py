
x = int(input("Enter a number: "))

if x > 1:

    for i in range(2, int(x ** 0.5) + 1):
        if (x % i) == 0:
            print(f"{x} is not a prime number.")
            break
    else:
        print(f"{x} is a prime number.")
else:
    print(f"{x} is not a prime number.")
