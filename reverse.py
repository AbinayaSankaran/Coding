# write a function to get reverse of the number.
"""
sample i/p: 971
sample o/p : 179

"""

def reverse(num):
      rev = 0
      while num!=0:
            rev  = (rev*10)+num%10
            num = num//10
      return rev
num = int(input("enter the number : "))
print(reverse(num))
