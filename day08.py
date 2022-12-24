def read_grid(filename: str):
    grid = []
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            row = [int(number) for number in line]
            grid.append(row)
    return grid

def check_visible(grid, y, x):
    if x == 0 or y == 0 or x == len(grid[0])-1 or y == len(grid)-1:
        return 1

    # Horizontal check
    hlist1, hlist2 = grid[x][0:y], grid[x][y+1:len(grid)]
    if max(hlist1) < grid[x][y] or max(hlist2) < grid[x][y]:
        return 1

    # Vertical check
    vlist1, vlist2 = [], []
    for index, row in enumerate(grid):
        if index != x:
            if index < x:
                vlist1.append(row[y])
            else:
                vlist2.append(row[y])
    if max(vlist1) < grid[x][y] or max(vlist2) < grid[x][y]:
        return 1
    return 0
    
def get_highest(grid, y, x):
    if x == 0 or y == 0 or x == len(grid[0])-1 or y == len(grid)-1:
        return 0
    score = 1

    k = y-1
    points = 0
    while k >= 0:
        points += 1
        if grid[x][k] >= grid[x][y]:
            break
        k -= 1
    score *= points

    k = y+1
    points = 0
    while k < len(grid):
        points += 1
        if grid[x][k] >= grid[x][y]:
            break
        k += 1
    score *= points
    
    i = x-1
    points = 0
    while i >= 0:
        points += 1
        if grid[i][y] >= grid[x][y]:
            break
        i -= 1
    score *= points

    i = x+1
    points = 0
    while i < len(grid[x]):
        points += 1
        if grid[i][y] >= grid[x][y]:
            break
        i += 1
    score *= points
    return score


def main():
    grid = read_grid("input.txt")
    visible = 0
    score = 1
    for j, row in enumerate(grid):
        for i, elem in enumerate(row):
            visible += check_visible(grid, i, j)
            new_score = get_highest(grid, i, j)
            if new_score > score:
                score = new_score

    print(visible)
    print(score)

if __name__ == "__main__":
    main()
