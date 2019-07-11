# Put your "check_celebrity" function below this line
def check_celebrity(some_grid):
    celebrity = False
    for i in range(len(some_grid)):
        total = 0
        total_2 = 0
        for j in range(len(some_grid[i])):
            if some_grid[i][j] == 0 and i != j:
                total += 1
            if some_grid[j][i] == 1 and i != j:
                total_2 += 1
        if total == len(some_grid[i]) - 1 and total_2 == len(some_grid) - 1:
            print("Celebrity at number", i)
            celebrity = True
    if not celebrity:
        print("No celebrity found")


# The code will test your function

print("Test 1, Should show #2 is a celebrity.")
grid = [[1, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [1, 0, 1, 1]]

check_celebrity(grid)

print("Test 2, Should show no one is a celebrity.")
grid = [[1, 1, 1, 0, 1],
        [0, 1, 1, 0, 1],
        [0, 0, 1, 0, 0],
        [1, 0, 0, 1, 1],
        [1, 0, 0, 1, 1]]

check_celebrity(grid)

print("Test 3, Should show #2 is a celebrity.")
grid = [[1, 1, 1, 0, 1],
        [0, 1, 1, 0, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1]]
check_celebrity(grid)

print("Test 4, Should show no one is a celebrity.")
grid = [[1, 1, 1, 0, 1],
        [0, 1, 1, 0, 1],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1]]

check_celebrity(grid)

print("TEST 5")
grid = [[1, 1, 1, 0, 1, 1, 1],
        [0, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 1, 1],
        [0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1, 1, 1]]

check_celebrity(grid)
