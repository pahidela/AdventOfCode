def get_stacks():	
	with open("input.txt", "r") as f:
		lines = f.readlines()

	# Getting the total number of stacks
	for index, line in enumerate(lines):
		if "move" in line.replace("\n", ""):
			total_stacks = len(lines[index-2].split())
			move_index = index
			break
	
	# Creating the stacks
	stacks = {}
	stacks_positions = [1, 5]
	for i in range(total_stacks):
		stacks[str(i+1)] = []
	for i in range(2, total_stacks):
		stacks_positions.append(stacks_positions[i-1]+4)

	# Updating the stacks data
	for index, line in enumerate(lines):
		if "[" not in line:
			break
		for index, position in enumerate(stacks_positions):
			if line[position].isalpha():
				stacks[str(index+1)].append(line[position])
	
	# Reversing the stacks
	for stack in stacks.keys():
		stacks[stack].reverse()
 			
	return move_index, stacks

def get_stack_element(stacks, fr):
	crate = stacks[fr][len(stacks[fr])-1]
	del(stacks[fr][len(stacks[fr])-1])
	return crate, stacks

def move_crates(amount, fr, to, stacks):
	for i in range(amount):
		crate = stacks[fr][len(stacks[fr])-1]
		del(stacks[fr][len(stacks[fr])-1])
		stacks[to].append(crate)	
	return stacks

def move_crates_v2(amount, fr, to, stacks):
	stack = stacks[fr]
	crates = stack[len(stack)-amount:len(stack)]
	stacks[to].extend(crates)
	delete_index = len(stack)-amount
	for j in range(amount):
		del(stacks[fr][delete_index])
	return stacks

def iterate_instructions(move_index, stacks, part_one):
	with open("input.txt", "r") as f:
		lines = f.readlines()
	for i in range(move_index, len(lines)):
		line = lines[i].replace("\n", "")
		amount = int(line.split(" ")[1])
		from_stack = line.split(" ")[3]	
		to_stack = line.split(" ")[5]
		if part_one:
			stacks = move_crates(amount, from_stack, to_stack, stacks) 
		else:
			stacks = move_crates_v2(amount, from_stack, to_stack, stacks)
	return stacks

def get_stacks_tops(stacks):
	tops = ""
	for stack in stacks.keys():
		stack_list = stacks[stack]
		tops += stack_list[len(stack_list)-1]
	return tops

move_index, stacks = get_stacks()
stacks = iterate_instructions(move_index, stacks, True)
print(get_stacks_tops(stacks))

move_index, stacks = get_stacks()
stacks = iterate_instructions(move_index, stacks, False)
print(get_stacks_tops(stacks))
