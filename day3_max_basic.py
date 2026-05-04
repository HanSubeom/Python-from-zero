max_value = None

while True:
    value = int(input("Enter a number (0 to quit): "))

    if value == 0:
        break

    if max_value is None:
        max_value = value
    elif value > max_value:
        max_value = value

if max_value is not None:
    print("Max:", max_value)
else:
    print("No numbers entered")
