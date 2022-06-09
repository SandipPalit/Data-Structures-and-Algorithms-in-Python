def GCD(A,B):
    """
    GCD(A,B) is the largest number dividing both A and B.
    """
    if A==0:
        return B
    return GCD(B%A,A)


def LCM(A,B):
    """
    LCM(A,B) is the smallest number divisible by both A and B.
    """
    return (A*B)//GCD(A,B)

num1=9
num2=18
print("GCD:  ",GCD(num1,num2),"  LCM:  ",LCM(num1,num2))