with open("input.txt", "r") as f:
	 data = f.readlines()


overlapping = 0
for pair in data:
	first, second = pair.split(",")[0], pair.split(",")[1]

	first_first = int(first.split("-")[0])
	first_second = int(first.split("-")[1])
	second_first = int(second.split("-")[0])
	second_second = int(second.split("-")[1])

	if first_first >= second_first and first_second <=second_second:
		overlapping += 1
	elif second_first >= first_first and second_second <= first_second:
		overlapping += 1
print(overlapping)


overlapping = 0
for pair in data:
	first, second = pair.split(",")[0], pair.split(",")[1]
	
	first_first = int(first.split("-")[0])
	first_second = int(first.split("-")[1])
	second_first = int(second.split("-")[0])
	second_second = int(second.split("-")[1])

	
	if first_first <= second_first and first_second >= second_first:
		overlapping += 1

	elif second_first <= first_first and second_second >= first_first:
		overlapping += 1

print(overlapping)
