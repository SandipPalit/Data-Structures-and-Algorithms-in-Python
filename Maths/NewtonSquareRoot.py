def NewtonSquareRoot(number,allowedError):
    """
    Initially we will assume that that number is itself its square root, i.e, 'X'.
    Then we will iterate and find root=(X+(number/X))/2.
    If error is less than 'allowedError' then break, else update 'X' as root
    """
    X=number
    while True:
        root=(X+(number/X))/2
        if abs(root-X)<=allowedError:
            break
        else:
            X=root
    return root


print(NewtonSquareRoot(11,0.01))