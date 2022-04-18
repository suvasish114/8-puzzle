'''
8-puzzle problem visualization using artificial intelligence (A* search)
author: @suvasish114 (https://suvasish114.github.io/)
'''
class Puzzle:
    '''contains puzzle board instance'''
    def __init__(self, board, goal, size):
        self.board = board  # board instance
        self.goal = goal    # goal board
        self.size = size   # board size in 1D
    
    def set_board(self, board):
        self.board = board
    
    @property
    def is_goal(self):
        return self.board == self.goal 
    
    @property
    def manhattan(self):
        '''calculate manhattan distance'''
        distance = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] != 0:
                    pos = 0
                    for k in range(self.size):
                        try:
                            pos = k*3 + self.goal[k].index(self.board[i][j])
                        except:
                            pass
                    distance += abs(i-int(pos/3)) + abs(j-int(pos%3))
        return distance

    def copy(self):
        '''copy board instance and return similar copy'''
        cpy = []
        for i in self.board:
            temp = []
            for j in i:
                temp.append(j)
            cpy.append(temp)
        return cpy
    
    def move(self, at, to):
        '''return a copy of board after performed move'''
        i,j = at 
        r,c = to 
        cpy = self.copy()
        cpy[i][j], cpy[r][c] = cpy[r][c], cpy[i][j]
        return cpy

    def action(self):
        '''return possible states'''
        moves = []
        for i in range(self.size):
            for j in range(self.size):
                directions = {  # directions w.r.t '0' (empty square)
                    'R': (i, j-1),
                    'L': (i, j+1),
                    'U': (i+1, j),
                    'D': (i-1, j)
                }
                for action,(r,c) in directions.items():
                    if r>=0 and c>=0 and r<self.size and c<self.size and self.board[i][j]==0:
                        move = self.move((i,j),(r,c))
                        moves.append(move)
        return moves


class Node:
    '''contains node properties'''
    def __init__(self, root, h=0, g=0):
        self.root = root    # board instance
        self.h = h  # heuristic cost
        self.g = g  # cost to reach present node
    
    def generate_child(self):
        self.g += 1
        childs = []
        for child in self.root.action():
            board = Puzzle(child, self.root.goal, self.root.size)
            node = Node(board, board.manhattan, self.g)
            childs.append(node)
        return childs   # [node...]
    
    @property
    def score(self):
        return self.g+self.h

    def set_root(self, root):
        self.root = root
    
class Solve:
    '''solver class'''
    def __init__(self, puzzle):
        self.node = Node(puzzle)

    def process(self):
        visited = []
        childs = self.node.generate_child()
        while self.node.root.is_goal == False:
            childs = self.node.generate_child()
            root = childs[0]
            for child in childs:
                if root.score > child.score and root.root.board not in visited:
                    root = child
            print('root:')
            for a in root.root.board:
                print(a)
            print(root.score)
            # print(visited)
            visited.append(root.root.board)
            self.node.set_root(root.root)
