from hitori import HitoriSolver, get_random_board
import os
import time
import psutil


def get_mem():
    a = psutil.Process(os.getpid())
    return a.memory_info().rss


def hitori_profiler(type, id):
    board = get_random_board(id)
    hit = HitoriSolver(board)
    mem_start = get_mem()
    start = time.time()
    result = hit.solve(algorithm=type)
    runtime = time.time()-start
    mem_end = get_mem()
    memused = (mem_end-mem_start)
    return [result, runtime, memused]
