from hitori import HitoriSolver, get_random_board
from board_n_tree_hashi import load_map
from hashi import dfs, a_star
import time
from memory_profiler import memory_usage


def hitori_profiler(algorithm, board_id):
    board = get_random_board(board_id)
    hit = HitoriSolver(board)
    res = []
    time_used = 0

    def hitori_solver(algorithm):
        nonlocal res, time_used
        start = time.time()
        res = hit.solve(algorithm)
        time_used = time.time() - start
    mem_used = memory_usage((hitori_solver, (algorithm,)), max_usage=True)
    return res, time_used, mem_used


def hashi_profiler(type, id):
    time_used = 0
    res = []
    test = load_map(f"board_hashi/{id}.txt")

    def hashi_solver(test):
        nonlocal res, time_used
        node = []
        start = time.time()
        if type == "dfs":
            node, i, j = dfs(test)
        else:
            node, i, j = a_star(test)
        time_used = time.time() - start
        res = node.path()
    mem_used = memory_usage((hashi_solver, (test,)), max_usage=True)
    return res, time_used, mem_used
