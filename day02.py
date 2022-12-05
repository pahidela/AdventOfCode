with open("input.txt", "r") as f:
	data = f.readlines()

total_points = 0
total_points2 = 0
pd1 = {
	"A X": 4,
	"A Y": 8,
	"A Z": 3,
 	"B X": 1,
	"B Y": 5,
	"B Z": 9,
	"C X": 7,
	"C Y": 2,
	"C Z": 6,
}

pd2 = {
	"A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
	"C Z": 7,
}

for line in data:
	line = line.replace("\n", "")
	if not line:
		break
	total_points += pd1[line]
	total_points2 += pd2[line] 	
print(total_points, total_points2)
	
	
