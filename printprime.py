# Print all prime numbers from 1 to 100
"""
A num is said to be prime num if it's greater than 1 divisible by only itself and by 1 without remainders. 
Ex: 2,3,5,7,11,13 etc
"""

def primrprint():
      for Number in range (1, 101):
            count = 0
            for i in range(2, (Number//2 + 1)):
                  if(Number % i == 0):
                        count = count + 1
                        break

            if (count == 0 and Number != 1):
                  print(" %d" %Number, end = '  ')

primrprint()