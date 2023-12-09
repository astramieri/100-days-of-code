# check is a number is prime
def prime_checker(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is NOT a prime number")   

n = int(input("Check this number: "))

prime_checker(n)