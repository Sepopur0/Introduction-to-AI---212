from board_n_tree_hashi import BoardState,Tree
from copy import deepcopy

visited = 0

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

def a_star(board):
    root_board = BoardState(board)
    root_board.generate_isl()
    root_board.evaluate()
    root_board.objective_function = 2 * hx(root_board) - gx(root_board)
    isl_count = len(root_board.islands)

    moves_tree = Tree(root_board)

    to_visit = [moves_tree.root]
    node_visited = 0
    final_node = None

    while len(to_visit) > 0:
        to_visit.sort(key=lambda node: node.content.objective_function, reverse=True)
        node_current = to_visit.pop()
        node_visited += 1

        node_current.content.evaluate()
        if node_current.content.solved:
            final_node = node_current
            return final_node, moves_tree, node_visited

        board_next = deepcopy(node_current).content

        for i in range(isl_count):
            for j in range(i+1, isl_count):
                if board_next.add_bridge(i, j):
                    board_next.objective_function = 2 * hx(board_next) - gx(board_next)
                    child = node_current.add_child(board_next)
                    to_visit.append(child)
                    board_next = deepcopy(node_current).content

    return final_node, moves_tree, node_visited



def dfs(board):
    root_board = BoardState(board)
    root_board.generate_isl()
    root_board.evaluate()

    global visited
    visited = 0

    moves_tree = Tree(root_board)

    node_current = moves_tree.root
    final_board = dfs_help(node_current, moves_tree)

    return final_board, moves_tree, visited


def dfs_help(node: Tree.Node, tree: Tree, depth=0):
    """global visited,
    visited += 1"""
    depth += 1

    isl_count = len(node.content.islands)
    board_next = deepcopy(node).content

    for i in range(isl_count):
        for j in range(i+1, isl_count):
            if board_next.add_bridge(i, j):
                board_next.evaluate()
                if board_next.solved:
                    result = node.add_child(board_next)
                    return result
                node_next = node.add_child(board_next)
                result = dfs_help(node_next, tree, depth)
                if result is not None:
                    return result
                board_next = deepcopy(node).content
    return None
