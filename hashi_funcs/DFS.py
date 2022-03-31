from hashi_funcs.tree import Tree
from hashi_funcs.boardstate import BoardState
from copy import deepcopy

visited = 0


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
