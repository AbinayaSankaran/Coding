#fibonacci series iterative method 
"""
In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.
"""
"""
Iterative method : In computational mathematics, an iterative method is a mathematical procedure that uses an initial value to generate a sequence of improving approximate solutions for a class of problems, in which the n-th approximation is derived from the previous ones.
"""
def fibs(n):
    f = []
    a = 0
    b = 1
    if n == 0 or n == 1:
        print(n)
    else:
        f.append(a)
        f.append(b)
        while len(f) != n:
            temp = a + b
            f.append(temp)
            a = b
            b = temp

    print(f)

print(fibs(20))