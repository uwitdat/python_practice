# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

term = 50
count = 0
number1 = 0
number2 = 1

while count < term:
    # some math here
    print(f'term: {count} / number: {number1} ')
    number = number1 + number2
    number1 = number2
    number2 = number
    count += 1
    if count == 50:
        break
