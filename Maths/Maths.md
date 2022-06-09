##Observations

###Bit Manipulation
* 1 OR any number will set that bit.
* 0 AND any number will reset that bit.
* 1 XOR any number gives you it's compliment.
* XOR with same number gives 0.
* Left shift (<<) A number B times gives A*(2^B).
* Right shift (>>) A number B times gives A//(2^B)

###Sieve of Eratosthenes
* For every prime number, we will drop its multiples. After repeating this step till the square root, only the prime numbers will be left behind.
* Time complexity:  N * log (log N)
* Space complexity:  O(N)

###Newton's Square Root
* Formula:  root = (X + N / X) / 2 where X is our guess. We will update the guessed number at each step as X = root.

###Euclidean GCD & LCM
* GCD(A,B) is the largest number dividing both A and B.
* LCM(A,B) is the smallest number divisible by both A and B.
* LCM(A,B) * GCD(A,B) = A * B
