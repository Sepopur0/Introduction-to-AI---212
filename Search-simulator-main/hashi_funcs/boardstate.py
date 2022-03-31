class BoardState:
    def __init__(self, board_matrix=None):
        if board_matrix is None:
            board_matrix = [[]]
        self.board = board_matrix
        self.islands = []
        self.solved = False
        self.objective_function = 0

    def evaluate(self):
        # All islands are full
        for isl in self.islands:
            if isl.br_expect != isl.br_cur:
                self.solved = False
                return False
        # All islands are connected
        visited = []
        stack = [0]
        while len(stack) > 0:
            current = stack.pop()
            visited.append(current)
            for con in range(len(self.islands)):
                if self.islands[current].connect[con] > 0:
                    if visited.count(con) == 0 and stack.count(con) == 0:
                        stack.append(con)

        if len(visited) == len(self.islands):
            self.solved = True
            return True

        self.solved = False
        return False

    def add_isl(self, x: int, y: int, br: int):
        new_isl = BoardState.Island(x, y, br)
        for _ in self.islands:
            new_isl.connect.append(0)
        self.islands.append(new_isl)
        for isl in self.islands:
            isl.connect.append(0)

    def generate_isl(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] > 0:
                    self.add_isl(i, j, self.board[i][j])

    def add_bridge(self, isl1: int, isl2: int):
        # Invalid ID
        if isl1 < 0 or isl2 < 0 or isl1 > len(self.islands) or isl2 > len(self.islands) or isl1 == isl2:
            return False
        # Full
        if self.islands[isl1].br_expect == self.islands[isl1].br_cur or\
                self.islands[isl2].br_expect == self.islands[isl2].br_cur:
            return False
        # Connected twice
        if self.islands[isl1].connect[isl2] == 2:
            return False
        # Not same x y
        if self.islands[isl1].x != self.islands[isl2].x and self.islands[isl1].y != self.islands[isl2].y:
            return False
        # Blocked
        if self.islands[isl1].connect[isl2] != 1:
            if self.islands[isl1].x == self.islands[isl2].x:
                x = self.islands[isl1].x
                for y in range(self.islands[isl1].y + 1, self.islands[isl2].y):
                    if self.board[x][y] > 0:
                        return False
            elif self.islands[isl1].y == self.islands[isl2].y:
                y = self.islands[isl1].y
                for x in range(self.islands[isl1].x + 1, self.islands[isl2].x):
                    if self.board[x][y] > 0:
                        return False
        # Adding
        self.islands[isl1].connect[isl2] += 1
        self.islands[isl2].connect[isl1] += 1
        self.islands[isl1].br_cur += 1
        self.islands[isl2].br_cur += 1
        # Placing bridge
        br = 0
        con = self.islands[isl1].connect[isl2]
        if self.islands[isl1].x == self.islands[isl2].x:
            x = self.islands[isl1].x
            if con == 1:
                br = 21
            if con == 2:
                br = 22
            for y in range(self.islands[isl1].y + 1, self.islands[isl2].y):
                self.board[x][y] = br
        elif self.islands[isl1].y == self.islands[isl2].y:
            y = self.islands[isl1].y
            if con == 1:
                br = 11
            if con == 2:
                br = 12
            for x in range(self.islands[isl1].x + 1, self.islands[isl2].x):
                self.board[x][y] = br
        return True

    class Island:
        def __init__(self, x: int, y: int, br: int):
            self.x = x
            self.y = y
            self.br_expect = br
            self.br_cur = 0
            self.connect = []


def load_map(file_name):

    with open(file_name, 'r') as file:
        return [list(map(int, row.strip('\n').split(' '))) for row in file]
