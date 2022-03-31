from profiler import hashi_profiler

if __name__ == "__main__":

    with open('hashi_perf_stat.txt', 'w', encoding='utf-8') as f:
        for id in range(20):
            f.write(f"Board ID: {id}\n")
            dump, time_used, mem_used = hashi_profiler(
                algorithm="dfgs", board_id=id)
            f.write("DFS Time usage: {} s\n".format(time_used))
            f.write("DFS Memory usage: {} MiB\n".format(mem_used))
            dump, time_used, mem_used = hashi_profiler(
                algorithm="a-star", board_id=id)
            f.write("A* Time usage: {} s\n".format(time_used))
            f.write("A* Memory usage: {} MiB\n".format(mem_used))
            f.write('-'*50 + '\n')
