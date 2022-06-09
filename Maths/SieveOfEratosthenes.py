def SieveOfEratosthenes(rangeNum):
    """
    Initially we will take a boolean array and assume that all the numbers from 1 to 'rangeNum' is prime.
    Then we will iterate till sqrt('rangeNum') and check whether that number is prime or not.
    If prime, then we will mark all its multiples as non-primes on the boolean array.
    """
    isPrime=[True]*(rangeNum+1)
    i=2
    while i*i <= rangeNum:
        if isPrime[i]:  # prime number
            for j in range(2*i,rangeNum+1,i):
                isPrime[j]=False
        i+=1
    primeNumbers=[]
    for i in range(2,len(isPrime)):
        if isPrime[i]:
            primeNumbers.append(i)
    return primeNumbers


print(SieveOfEratosthenes(100))