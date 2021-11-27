# Check whether the given number is armstrong or not.
"""
A number is said to be armstrong number if it's sum of n th power of each digit is equal to the number itself. Here n is called no of digits in the given number. Example Case: 371 = 3^3+7^3+1^3 = 371 

"""
def armstrong(num):
      sum = 0
      order = len(str(num))
      temp = num
      while temp >0:
            digit = temp % 10
            sum += digit ** order
            temp //=10
      if num == sum:
            print("armstrong")
      else:
            print("not armstrong")

num = int(input("enter the number: "))
print(armstrong(num))