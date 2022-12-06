with open("input.txt", "r") as f:
    line = f.read()

def get_marker(line, number):
    for i in range(number-1, len(line)):
        letters = set()
        for j in range(i-number+1, i+1):
            letters.add(line[j])
        if len(letters) == number:
            marker = i+1
            break
    return marker

print(get_marker(line, 4))
print(get_marker(line, 14))
