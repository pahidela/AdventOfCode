with open("input.txt", "r") as f:
    data = f.readlines()

def get_points(char: str):
    alphabet_points = {letter: pos+1 for pos, letter in enumerate("abcdefghijklmnopqrstuvwxyz")} 
    case_points = 0 if char in alphabet_points else 26
    return alphabet_points[char.lower()]+case_points

total_points = 0
for line in data:
    line = line.replace("\n", "")

    first = line[0:int(len(line)/2)]
    second = line[int(len(line)/2):len(line)]
    
    for letter in first:
        if letter in second:
           total_points += get_points(letter) 
           break
print(total_points)

total_points = 0
i = 0
while i < len(data):

    first = data[i].replace("\n", "")
    second = data[i+1].replace("\n", "")
    third = data[i+2].replace("\n", "")
    for letter in first:
        if letter in second and letter in third:
            total_points += get_points(letter)
            break
    i += 3
print(total_points)
