"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

#How to check if a number is prime

# # could do it brute force and count up to the number but I feel like there's a better way....
# def isPrime(x):
#     prime = True # Unless otherwise proven false
#     for i in range(2, x):
#         if x % i == 0:
#             prime = False
#             # print("Not Prime! " + str(i))
#     return prime

# # Testing function
# print(isPrime(13))

    # Now for the rest of the problem
largestPrimeFactor = 0

cap = 600851475143

# for i in range(2, cap):
#     if cap % i == 0:    # If you find a factor
#         if isPrime(i):      #Check if it's prime
#             largestPrimeFactor = i # If it is then it is the largest prime factor found so far

# print("The Largest prime factor of " + str(cap) + " is " + str(largestPrimeFactor))

# Above code takes somewhere on the order of 10^22 calculations so I was right the functions need to be optomized

# I am now optomizing the function isPrime to exit once it confirms it is not prime and I am also going to count down instead of up
    # Because the goal is the LARGEST prime factor

def isPrime(x):
    prime = True
    i = 2
    while i < x/2 and prime : # while the number is prime keep checking # We also only have to check up to 1/2 the number
        if x % i == 0:
            prime = False   #This exits the while loop if the number is found to not be prime
            print(str(x) + " is divisible by " + str(i))
        i += 1
    return prime


# # Making a while loop to count backwards from the cap checking for largest factor and then checking if it is prime
# i = int(cap/2)
# print(i)
# largestPrimeFactorNotFound = True
# while i > 0 and largestPrimeFactorNotFound:
#     if cap % i == 0:    # Is it a factor
#         print(str(i) + ' is a factor')
#         if isPrime(i):      # If I is a factor then check if it's prime
#             largestPrimeFactorNotFound = False  # If it's prime then we found it!
#             largestPrimeFactor = i
#             print(str(i) + ' is prime')
#     # else:
#     #     print(str(i) + ' is not prime')
#     i -= 2
# print("Largest prime factor of " + str(cap) + ' is ' + str(largestPrimeFactor))










# Start from the bottom and find the factor's pair and see if the pair is prime!


cap = 600851475143
factorPair = 0
smallestFactorFound = cap
escape = True

# # 13195 prime factors are 5, 7, 13 and 29.
# print('Factors of ' + str(cap))
# for i in range(2, cap):
#     if cap % i == 0:
#         factorPair = cap / i
#         print(i, int(factorPair))
#         if smallestFactorFound > i:
#             escape = False
#         # if isPrime(i):
#         #     # print(True)



i = 3
while escape and i < int(cap/2):
    # print(i)
    # If a factor is found
    if cap % i == 0:
        #Find the factor's pair
        factorPair = cap / i
        # If the factor pair is prime then we are done
        if isPrime(factorPair):
            answer = factorPair
        # Otherwise if the factor is prime it is the highest prime factor found so far
            # If no factorPairs are prime when checkin on the way up we will have kept up to date the largest prime factor found
        else:
            if isPrime(i):
                answer = i

        # Check if we have found all of the factors
        if i > factorPair:
            # If so then break from the loop
            escape = False
        print( i, int(factorPair))

    # Only search odd numbers because even numbers can't be prime or factors
    i += 2

print()
print(answer)


# Congratulations, the answer you gave to problem 3 is correct.

# The public tables currently show that this problem has been solved by 553622 members.

# You have earned 1 new award:

# Baby Steps: Solve three problems