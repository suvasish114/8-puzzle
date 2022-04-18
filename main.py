from puzzle import *

def prompt(size, message):
    print(message)
    board = []
    for i in range(size):
        temp = input().split(" ")
        for j in range(len(temp)):
            temp[j] = int(temp[j])
        board.append(temp)
    return board

if __name__ == '__main__':
    size = int(input("Enter the puzzle size: "))
    start = prompt(size, "Enter the start puzzle:")
    goal = prompt(size, "Enter the goal puzzle:")
    puzzle = Puzzle(start, goal, size)
    solver = Solve(puzzle)
    solver.process()
