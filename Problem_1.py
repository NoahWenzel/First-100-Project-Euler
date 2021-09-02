"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Note: Does this include 1000 or not?
"""

# Find multiples below x

x = 1000

totalSum = 0 # Start this off as 0

for i in range(x):
    if i % 3 == 0:
        print(i)
        totalSum += i
    elif i % 5 == 0:
        print(i)
        totalSum += i

print("Final Sum")
print(totalSum)


# 966752