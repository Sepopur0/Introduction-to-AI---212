from hashi_funcs.boardstate import BoardState


def gx(board: BoardState):
    cost = 0

    for island in board.islands:
        for i in range(len(island.connect)):
            cost += island.connect[i]*(island.br_expect + board.islands[i].br_expect)

    return cost/2


def hx(board: BoardState):
    isl_count = len(board.islands)
    path_lengths = [0]
    visited = []
    for i in range(isl_count):
        stack = []
        if visited.count(i) != 0:
            continue
        stack.append(i)
        length = 0
        while len(stack) > 0:
            length += 1
            current = stack.pop()
            visited.append(current)
            for cn in range(len(board.islands)):
                if board.islands[current].connect[cn] > 0:
                    if visited.count(cn) == 0 and stack.count(cn) == 0:
                        stack.append(cn)
        path_lengths.append(length)

    heuristic = isl_count - max(path_lengths)
    return heuristic
