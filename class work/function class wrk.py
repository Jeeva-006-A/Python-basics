# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

def isPrime(num):
    # Step 1: If the number is less than or equal to 1, it's not prime
    if num <= 1:
        return False

    # Step 2: Check divisibility from 2 up to num - 1
    for i in range(2, num):
        if num % i == 0:
            # If divisible by i, not a prime
            return False

    # Step 3: If loop completes, it's a prime number
    return True


# --- Main Program ---
n = int(input("Enter a number: "))

if isPrime(n):
    print("Prime number")
else:
    print("Not a prime number")

