# Imports

# Jordan Hancock
# Solution to karan projects:
#   Fibonacci Sequence

# Calculates and prints fibonacci sequence to a certain number
def calculateFibonacciTo(number):
    values = [0, 1] # Starting values

    while len(values) < number:
        nextPos = len(values) # Use length of list to get nextPos

        #nextPos = sum of previous two values
        values.append(values[nextPos - 2] + values[nextPos - 1])

    return values

def main():
    number = int(raw_input("Calculate fib to? ")) # Get user input

    fibonacciSequence = calculateFibonacciTo(number) # Get output

    print fibonacciSequence

if __name__ == "__main__":
    main()
