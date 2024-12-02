fileName = "Day2/Input.txt"

input = []

with open(fileName) as file:
    for line in file:
        input.append([int(num) for num in line.split()])

def findSafeReports(input):
    # Give safeReports the size of the input array
    safeReports = len(input)
    for line in input:
        isIncreasing = False
        isChecked = False
        prevNumber = -1

        for curNumber in line:
            # If index is 0, there is no previous number so we set the prevNumber to the number and move on
            if (prevNumber == -1): 
                prevNumber = curNumber
                continue

            # Checks whether the array is ascending or descending
            if (isChecked == False):
                if (curNumber > prevNumber):
                    isIncreasing = True
                elif(curNumber < prevNumber):
                    isIncreasing = False
                isChecked = True
            
            # Calculate the difference between two indexes using max/min to prevent negative numbers
            levelDifference = max(curNumber, prevNumber) - min(curNumber, prevNumber)

            # If the difference fails a test case, subtract 1 from the overall safe reports count and break the loop
            if (levelDifference > 3 or levelDifference < 1) or ((curNumber > prevNumber and isIncreasing == False) or (curNumber < prevNumber and isIncreasing == True)):
                safeReports -= 1
                break
            
            prevNumber = curNumber
    return safeReports

findSafeReports(input)