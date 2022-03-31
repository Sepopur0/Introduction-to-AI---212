from hashi_funcs.tree import Tree
from hashi_funcs.boardstate import BoardState
from copy import deepcopy
from hashi_funcs import heuristic


def a_star(board):
    root_board = BoardState(board)
    root_board.generate_isl()
    root_board.evaluate()
    root_board.objective_function = 2 * heuristic.hx(root_board) - heuristic.gx(root_board)
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
                    board_next.objective_function = 2 * heuristic.hx(board_next) - heuristic.gx(board_next)
                    child = node_current.add_child(board_next)
                    to_visit.append(child)
                    board_next = deepcopy(node_current).content

    return final_node, moves_tree, node_visited
