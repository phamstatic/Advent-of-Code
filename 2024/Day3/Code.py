import re

fileName = "2024/Day3/Input.txt"
input = []

with open(fileName) as file:
    for line in file:
        input.append(line)

# mul\((\d+),\s*(\d+)\)
# mul\(: Matches the literal string "mul(".
# \d+: Matches one or more digits (for the first number).
# ,: Matches the comma between the numbers.
# \s*: Matches any whitespace between the comma and the second number (optional).
# \d+: Matches the second number.
# \): Matches the closing parenthesis.

def scanCorruptedMemory(input):
    validInput = []
    for i in range(0, len(input)):
        validInput.append(re.findall('mul\((\d+),\s*(\d+)\)', input[i]))

    inputProduct = 0
    for j in range(0, len(validInput)):
        for k in range(0, len(validInput[j])):
            # The regular expression returns an array of unordered pairs e.g.: ('373', '681')
            inputProduct += int(validInput[j][k][0]) * int(validInput[j][k][1])

    return inputProduct

scanCorruptedMemory(input)