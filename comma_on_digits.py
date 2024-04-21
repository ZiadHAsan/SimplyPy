digits = input("enter number: ")

parts = []

while len(digits) > 0:
    parts.insert(0,digits[-3:])
    digits = digits[:-3]

print(",".join(parts))
