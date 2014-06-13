# Imports

# Jordan Hancock
# Solution to karan projects:
#   Collatz Conjecture 

# Performs some task
def calculateCollatzConjecture(numberToConject):
    currentValue = numberToConject # Copy of number which can be modified
    numberOfOperations = 0 # Current number of operations performed

    while currentValue > 1: # Do until currentValue = 1
        if currentValue % 2 == 0: # If even
            currentValue = currentValue / 2 # Divide by 2
        else: # If odd
            currentValue = (currentValue * 3) + 1 # Multiply by 3 then add 1
        numberOfOperations = numberOfOperations + 1

    return numberOfOperations

def main():
    numberToConject = int(raw_input("Enter number to conject > "))
    if numberToConject > 1:
	    numberOfOperations = calculateCollatzConjecture(numberToConject)
    else:
        print "Number must be greater than 1."

    print numberOfOperations

if __name__ == "__main__":
    main()
