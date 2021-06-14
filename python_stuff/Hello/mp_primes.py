#!/user/bin/python3
from multiprocessing import Process
import sys


def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def count_primes_in_range(start, end):
    total = 0
    for x in range(start, end):
        if is_prime(x):
            total += 1
    return total


def child_primes(start, end, primes):
    print("starting new child process")
    local_count = count_primes_in_range(start, end)
    print("local_count is {0} in the range {1} to {2}.".format(local_count, start, end))
    primes.append(local_count)
    print("")

def main():
    num_processes_input = sys.argv[1]
    num_processes = int(num_processes_input)
    range_start = 100
    range_end = 100000
    total_range = range_end - range_start
    process_range = int(total_range / num_processes)
    print("running the parent processes")
    fork_processes = []
    fork_ranges = []
    fork_primes =[]

    for i in range(0, num_processes):
        cur_start = range_start + process_range * i
        cur_end = range_start + process_range * (i + 1) - 1
        fork_ranges.append((cur_start, cur_end))

    for x in range(0, num_processes):
        cur_process = Process(target=child_primes, args=(fork_ranges[x][0], fork_ranges[x][1], fork_primes))
        fork_processes.append(cur_process)
        fork_processes[x].start()

    for proc in fork_processes:
        proc.join()
    print("All child processes finished.")


if __name__ == "__main__":
    main()