def isPrime(x):
    """
    This function determines if the input parameter is prime or not. 
    This function does use the brute force method and I feel like this could be done a more beautiful way...
    """
    prime = True
    i = 2
    while i < x/2 and prime : # while the number is prime keep checking # We also only have to check up to 1/2 the number
        if x % i == 0:
            prime = False   #This exits the while loop if the number is found to not be prime
            # print(str(x) + " is divisible by " + str(i))
        i += 1
    return prime

    # Testing function isPrime()
# print(isPrime(13))

def findGreatestPrimeFactor(cap):
    '''
    This function find's the Greatest Prime Factor of cap
    
    '''
    factorPair = 0
    escape = True
    i = 3
    while escape and i < int(cap/2):
        # print(i)
        # If a factor is found
        if cap % i == 0:
            #Find the factor's pair
            factorPair = cap / i
            # If the factor pair is prime then we are done
            if isPrime(factorPair):
                return(factorPair)
            # Otherwise if the factor is prime it is the highest prime factor found so far
                # If no factorPairs are prime when checkin on the way up we will have kept up to date the largest prime factor found
            else:
                if isPrime(i):
                    answer = i  # We don't return here because there may be bigger numbers

            # Check if we have found all of the factors
            if i > factorPair:
                # If so then break from the loop
                escape = False
            # print( i, int(factorPair))

        # Only search odd numbers because even numbers can't be prime or factors
        i += 2

    return(answer)

# # Testing findGreatestPrimeFactor function
# print(findGreatestPrimeFactor(600851475143))

def isPalindromic(x):
    '''
    Checks if the number given in the parameter is palindromic or not.
    '''
    strNum = str(x)
    numDigits = len(strNum)
    checkNumDigits = int(numDigits / 2) # If there is an odd number the middle digit does not need to be checked
    firstHalf = strNum[0:checkNumDigits]
    secondHalf = strNum[-checkNumDigits:][::-1] # Get the last half and turn them around
    #Compare the frirst and second half
    if firstHalf == secondHalf:
        return True
    return False

print(isPalindromic(1234321))