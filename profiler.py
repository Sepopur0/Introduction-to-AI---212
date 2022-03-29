from hitori import HitoriSolver, get_random_board
import timeit
from memory_profiler import memory_usage


def hitori_profiler(algorithm, board_id):
    setup = f"""
from hitori import HitoriSolver, get_random_board
a = get_random_board(id={board_id})
hit = HitoriSolver(a)
"""
    stmt = f"hit.solve(algorithm='{algorithm}')"
    time_used = timeit.timeit(stmt, setup=setup, number=1)

    board = get_random_board(board_id)
    hit = HitoriSolver(board)
    mem_used = memory_usage((hit.solve, (algorithm,)), max_usage=True)

    return time_used, mem_used
