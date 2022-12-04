with open("input.txt", "r") as f:
	 data = f.readlines()

def get_sections_string(sections):
	
	array = list(range(int(sections.split("-")[0]), int(sections.split("-")[1])+1))
	string = " ".join([str(number) for number in array])
	return string

overlapping = 0
for pair in data:
	first, second = pair.split(",")[0], pair.split(",")[1]

	first = get_sections_string(first)
	second = get_sections_string(second)
	
	if first in second or second in first:
		print(pair)
		overlapping += 1	
print(overlapping)
