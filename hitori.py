import numpy as np
from queue import PriorityQueue, Queue, LifoQueue


class State:
    def __init__(self, board, dept=0, parent=None):
        self.board = board
        self.dept = dept
        self.parent = parent
        self.score = 0

    def is_goal(self):
        def is_uniqued(arr):
            unique_arr = np.unique(arr)
            return unique_arr[unique_arr != 0].shape == arr[arr != 0].shape

        goal_row = np.all(np.apply_along_axis(is_uniqued, 1, self.board))
        goal_col = np.all(np.apply_along_axis(is_uniqued, 0, self.board))
        return goal_row and goal_col

    def is_feasible(self, r, c):
        def is_not_shaded_adj(board, r, c):
            size = board.shape[0]
            return (r == size-1 or (r < size-1 and board[r+1, c] != 0)) and (r == 0 or (r > 0 and board[r-1, c] != 0)) \
                and (c == size-1 or (c < size-1 and board[r, c+1] != 0)) and (c == 0 or (c > 0 and board[r, c-1] != 0))

        def is_not_shaded_surround(board, r, c):
            size = board.shape[0]
            c1 = (r < size-2 and board[r+2, c] != 0) or (r == size-1) or (r < size-1 and (
                (c < size-1 and board[r+1, c+1] != 0) or (c > 0 and board[r+1, c-1] != 0)))
            c2 = (r > 1 and board[r-2, c] != 0) or (r == 0) or (r > 0 and (
                (c < size-1 and board[r-1, c+1] != 0) or (c > 0 and board[r-1, c-1] != 0)))
            c3 = (c < size-2 and board[r, c+2] != 0) or (c == size-1) or (c < size-1 and (
                (r < size-1 and board[r+1, c+1] != 0) or (r > 0 and board[r-1, c+1] != 0)))
            c4 = (c > 1 and board[r, c-2] != 0) or (c == 0) or (c > 0 and (
                (r < size-1 and board[r+1, c-1] != 0) or (r > 0 and board[r-1, c-1] != 0)))
            return c1 and c2 and c3 and c4

        def is_not_shaded_divide(board, r, c):
            def explore(board):
                size = board.shape[0]
                non_zero = np.nonzero(board)
                blacked_cell = size*size - len(non_zero[0])
                visited = np.full_like(board, True, dtype=bool)
                visited[non_zero] = False

                start = (non_zero[0][0], non_zero[1][0])
                st = [start]
                visited[start] = True
                num_of_connected_cell = 1
                while st:
                    current = st.pop()
                    if current[0] > 0 and not visited[current[0]-1, current[1]]:
                        st.append((current[0]-1, current[1]))
                        visited[st[-1]] = True
                        num_of_connected_cell += 1

                    if current[0] < size-1 and not visited[current[0]+1, current[1]]:
                        st.append((current[0]+1, current[1]))
                        visited[st[-1]] = True
                        num_of_connected_cell += 1

                    if current[1] > 0 and not visited[current[0], current[1]-1]:
                        st.append((current[0], current[1]-1))
                        visited[st[-1]] = True
                        num_of_connected_cell += 1

                    if current[1] < size-1 and not visited[current[0], current[1]+1]:
                        st.append((current[0], current[1]+1))
                        visited[st[-1]] = True
                        num_of_connected_cell += 1

                return num_of_connected_cell, blacked_cell

            size = board.shape[0]
            temp = board.copy()
            temp[r, c] = 0
            num_of_connected_cell, blacked_cell = explore(temp)
            return size*size == num_of_connected_cell+blacked_cell

        return is_not_shaded_adj(self.board, r, c) and is_not_shaded_surround(self.board, r, c) and is_not_shaded_divide(self.board, r, c)

    def __lt__(self, other):
        return self.score < other.score


def get_random_board(id=5):
    path = f'board/{id}.txt'
    return np.loadtxt(path, dtype=int)


class HitoriSolver:

    def __init__(self, board):
        self.initial_state = State(board=board)

    def expand(self, current):
        indexes = np.nonzero(current.board)
        successors = []
        for i in range(len(indexes[0])):
            if current.is_feasible(indexes[0][i], indexes[1][i]):
                temp = current.board.copy()
                temp[indexes[0][i], indexes[1][i]] = 0
                successors.append(
                    State(temp, dept=current.dept+1, parent=current))

        return successors

    def tracking(self, goal):
        current = goal.parent
        path = [goal.board]
        while current:
            path.append(current.board)
            current = current.parent

        path.reverse()
        return path

    def heuristic(self, state):
        def func(arr):
            arr = arr[arr != 0]
            count = np.bincount(arr)
            count = count[count > 1]
            count = count*(count-1)/2
            return np.sum(count)

        row_conflict = np.sum(np.apply_along_axis(func, 1, state.board))
        col_conflict = np.sum(np.apply_along_axis(func, 0, state.board))
        return row_conflict + col_conflict

    def solve(self, algorithm="dfs"):
        def DFS():
            st = LifoQueue()
            st.put(self.initial_state)
            while not st.empty():
                current = st.get()
                if current.is_goal():
                    return self.tracking(current)
                successors = self.expand(current)
                for succ in reversed(successors):
                    st.put(succ)

            raise Exception("Can not reach goal state.")

        def DFGS():
            st = LifoQueue()
            st.put(self.initial_state)
            explored = set()
            while not st.empty():
                current = st.get()
                if current.is_goal():
                    return self.tracking(current)
                successors = self.expand(current)
                for succ in reversed(successors):
                    encode_nparr = tuple(succ.board.reshape(-1))
                    if encode_nparr not in explored:
                        st.put(succ)
                        explored.add(encode_nparr)

            raise Exception("Can not reach goal state.")

        def BFS():
            q = Queue()
            q.put(self.initial_state)
            while not q.empty():
                current = q.get()
                if current.is_goal():
                    return self.tracking(current)
                successors = self.expand(current)
                for succ in successors:
                    q.put(succ)

            raise Exception("Can not reach goal state.")

        def BFGS():
            q = Queue()
            q.put(self.initial_state)
            explored = set()
            while not q.empty():
                current = q.get()
                if current.is_goal():
                    return self.tracking(current)
                successors = self.expand(current)
                for succ in successors:
                    encode_nparr = tuple(succ.board.reshape(-1))
                    if encode_nparr not in explored:
                        q.put(succ)
                        explored.add(encode_nparr)

            raise Exception("Can not reach goal state.")

        def BestFS(f):
            self.initial_state.score = f(self.initial_state)
            p = PriorityQueue()
            p.put(self.initial_state)
            explored = set()
            while not p.empty():
                current = p.get()
                if current.is_goal():
                    return self.tracking(current)
                successors = self.expand(current)
                for succ in successors:
                    encode_nparr = tuple(succ.board.reshape(-1))
                    if encode_nparr not in explored:
                        explored.add(encode_nparr)
                        succ.score = f(succ)
                        p.put(succ)

            raise Exception("Can not reach goal state.")

        if algorithm == "dfgs":
            return DFGS()
        elif algorithm == "a-star":
            return BestFS(f=lambda state: state.dept + self.heuristic(state))
        elif algorithm == "best-fs":
            return BestFS(f=self.heuristic)
        elif algorithm == "dfs":
            return DFS()
        elif algorithm == "bfs":
            return BFS()
        elif algorithm == "bfgs":
            return BFGS()
        else:
            raise ValueError("Algorithm must be 'dfs', 'best-fs' or 'a-star'.")
