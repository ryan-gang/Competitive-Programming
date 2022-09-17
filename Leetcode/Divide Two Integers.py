DIVD = dividend = 7
DIVS = divisor = 3
quotient = 0

while dividend >= divisor:
    dividend -= divisor
    quotient += 1

print(quotient == (DIVD // DIVS))
print(quotient)
