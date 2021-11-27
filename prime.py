# Check whetehr the num is prime or not
"""
A num is said to be prime num if it's greater than 1 divisible by only itself and by 1 without remainders. 
Ex: 2,3,5,7,11,13 etc
"""

def prime(num):
      if num > 1:
            for i in range(2, num):
                  if (num % i) == 0:
                        print(num, "is not a prime num")
                        break
            else:
                  print(num, "is a prime num")
            
      else:
            print(num, "is not a prime num")

num = int(input("enter the num : "))
print(prime(num))