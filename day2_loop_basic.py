total = 0
count = 0

while True:
	value = int(input("Enter a number (0 to quit): "))

	if value == 0:
		break

	total += value
	count += 1

print("Total", total)
print("count", count)
