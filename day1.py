with open("input.txt", "r") as f:
	lines = f.readlines()

calorie_dict = {}
actual_calories = 0
i = 1
for line in lines:
	if line != "\n":
		actual_calories += int(line)
	else:
		calorie_dict[i] = actual_calories
		i += 1
		actual_calories = 0

def get_top_calories(calorie_dict: dict, number: int):
	total = 0
	for i in range(number):
		m = 0
		for position, value in calorie_dict.items(): 
			if value > m:
				m = value
				m_pos = position
		total += m
		print(m)
		calorie_dict.pop(m_pos)
	print(f"The total calories for the top {number} elves is {total}")
	
# get_top_calories(calorie_dict, 1)
get_top_calories(calorie_dict, 3)

