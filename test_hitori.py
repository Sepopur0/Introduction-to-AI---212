from sys import implementation
import numpy as np
from hitori import HitoriSolver, get_random_board
import time
import timeit

def check(id=5):
    a = get_random_board(id)
    hit = HitoriSolver(a)
    start=time.time()
    dfgs = hit.solve(algorithm='dfgs')  
    print("DFS:",time.time()-start)
    a_star = hit.solve(algorithm='a-star')
    bestfs = hit.solve(algorithm='best-fs')
    
def profiler(id=5):
    setup = """
import numpy as np
from hitori import HitoriSolver, get_random_board
a = get_random_board({id})
hit = HitoriSolver(a)
""".format(id=id)
    dfgs = "hit.solve(algorithm='dfgs')"
    a_star = "hit.solve(algorithm='a-star')"
    bestfs = "hit.solve(algorithm='best-fs')"

    print("DFGS:", timeit.timeit(dfgs, setup=setup, number=1))
    print("Best-FS:", timeit.timeit(bestfs, setup=setup, number=1))
    print("A*:", timeit.timeit(a_star, setup=setup, number=1))



if __name__ == '__main__':
    # a = get_random_board()
    # a = np.loadtxt("board/18.txt", dtype=int)
    # hit = HitoriSolver(a)
    # print(*hit.solve(algorithm='best-fs'), sep='\n\n')

#     setup = """
# import numpy as np
# from hitori import HitoriSolver, get_random_board
# a = np.loadtxt("board/5x5/9.txt",dtype=int)
# hit = HitoriSolver(a)
# """
#     dfgs = "hit.solve(algorithm='dfgs')"
#     print(timeit.timeit(dfgs, setup=setup, number=1), sep='\n\n')
    profiler()
