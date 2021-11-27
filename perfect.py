# check whether the given number is perfect or not 
"""
In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.

"""
def perfect(num):
      sum=0
      for i in range(1,(num//2)+1):
            remainder = num % i
            if remainder == 0:
                  sum = sum + i
      if sum == num:
            print("given no. is perfect number")
      else:
            print("given no. is not a perfect number") 

num = int(input("enter the number : "))
print(perfect(num))