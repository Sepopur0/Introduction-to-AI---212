from hitori import HitoriSolver, get_random_board
import time
from memory_profiler import memory_usage


def hitori_profiler(algorithm, board_id):
    board = get_random_board(board_id)
    hit = HitoriSolver(board)
    res = []
    time_used = 0

    def solver(algorithm):
        nonlocal res, time_used
        start = time.time()
        res = hit.solve(algorithm)
        time_used = time.time() - start

    mem_used = memory_usage((solver, (algorithm,)), max_usage=True)

    return res, time_used, mem_used
