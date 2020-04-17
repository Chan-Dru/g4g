def SieveOfEratosthenes(n):
    prime = [True]*n
    p = 2
    while(p*p < n):
        if prime[p]:
            for i in range(p*p,n,p):
                prime[i] = False
        p += 1

    prime_number = [i for i in range(2,n) if prime[i] ]
    return prime_number

    

if __name__ == "__main__":
    n = 50
    prime = SieveOfEratosthenes(n)
    print("Prime numbers in the range {} is {}".format(n,prime))