def isPrime(number):

    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not prime
            return False # number is not a prime
        divisor += 1

    return True # number is prime

print(isPrime(6))

def main():
    count(0)
    N = 10000
    for number in range(2,N):
        if isPrime(number):
            count += 1
    print('There are' + str(count) + 'prime numbers between 1 and' + str(N))
    
    if isPrime(12):
        print('prime')
    else:
        print('not prime')
    main()
