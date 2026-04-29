number = int(input("Enter a number: "))

if number % 2 == 0:
	print("Even")
else:
	print("Odd")

total = 0
count = 0

while True:
	value = int(input("Enter a number (0 to quit): "))

	if value == 0:
		break

	total += value
	count += 1

if count > 0:
	print("Total:", total)
	print("Average:", total / count)
else:
	print("No input")
