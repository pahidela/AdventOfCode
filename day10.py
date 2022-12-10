with open("input.txt", "r") as f:
    data = f.readlines()


def draw_sprite(cycle, sprite_str, register):
    register_pixels = [register-1, register, register+1]
    print(f"cycle {cycle}: ", register, register_pixels)
    if cycle-1-40*sprite_str.count("\n") in register_pixels:
        sprite_str += "#"
    else:
        sprite_str += "."
    if len(sprite_str) in [40, 81, 122, 163, 204]:
        sprite_str += "\n"
    print(f"\n{sprite_str}\n")
    return sprite_str


def check_cycles(cycles, current_value, register):
    if (cycles - 20) % 40 == 0 or cycles == 20:
        current_value += cycles*register
    return current_value


current_value = 0
cycle = 1
register = 1
sprite_str = ""
for line in data:
    instruction = line.strip()
    command = instruction.split(" ")[0]
    if command == "addx":
        for times in range(1, 2+1):
            sprite_str = draw_sprite(cycle, sprite_str, register)
            cycle += 1
            if times == 2:
                register += int(instruction.split(" ")[1])
            current_value = check_cycles(cycle, current_value, register)
    else:
        sprite_str = draw_sprite(cycle, sprite_str, register)
        cycle += 1
        current_value = check_cycles(cycle, current_value, register)

print(current_value)


