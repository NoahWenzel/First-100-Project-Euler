'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

# Just try counting down and check if the numbers are palindromic

# Check if number is palindromic function
def isPalindromic(x):
    strNum = str(x)
    numDigits = len(strNum)
    checkNumDigits = int(numDigits / 2) # If there is an odd number the middle digit does not need to be checked
    firstHalf = strNum[0:checkNumDigits]
    secondHalf = strNum[-checkNumDigits:][::-1] # Get the last half and turn them around
    #Compare the frirst and second half
    if firstHalf == secondHalf:
        return True
    return False

# print(isPalindromic(1234321))


# print(999 * 999)

# First check all of the 6 digit numbers

# print(100000 / 999)
    # This means to do this the smaller number has to be greater than 100 (999 * 100) is the lower bound

x = 99
y = 99

# Start here and then work y all the way down to 100 before decrementing x and we'll see how long this takes.......

def testFunction():     # This is in a function so I can use for loops but easily break when I found the answer 
    for i in range(x, 9, -1):
        for j in range(y, 9, -1): # I know this lower bound could be higher but we'll find the answer before then
            # print(i, j)
            if isPalindromic(i*j):
                print(i, j, i*j)
                return

# testFunction()



# The above doesn't work because it's not multiplying the biggest two numbers but rather the biggest number that comes up first
# So let's try it a different way and see if we can find all of the palindromic numbers and then see if their largest common factors
    # are both 3 digits.


def test(cap):
    highestPairFound = [0, 0, 0]
    print('Factors of ' + str(cap))
    for factor in range(2, cap): # The factor starts at 2 and goes up to the provided number
        if cap % factor == 0:   # If the number truely is a factor enter this if statement
            factorPair = int(cap / factor)   # Find the Factor Pair
            if factor > factorPair: #Escape and return the highest factor pair that has 3 digits
                return highestPairFound
            print(factor, int(factorPair))
            # print(len(str(factor)), len(str(factorPair)))
            #Test them to see if they are 3 digits
            if len(str(factor)) == 3 and len(str(factorPair)) == 3:
                # We have found the next best canidate
                highestPairFound[0] = factor
                highestPairFound[1] = factorPair
                highestPairFound[2] = factor * factorPair


                #the above function finds all of the factor pairs and then returns the highest factors if it is 3 digits for both factors
# print(test(111*111))

def testFunction():
    for i in range((999*999), 0, -1):
        if isPalindromic(i):
            #Find largest factors and check if they are both 3 digits
            possibleSolution = test(i)
            if possibleSolution != [0, 0, 0]:
                return(possibleSolution)
print(testFunction())

'''
Congratulations, the answer you gave to problem 4 is correct.

The public tables currently show that this problem has been solved by 489651 members.
'''