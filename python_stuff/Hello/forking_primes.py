#!/user/bin/python3
import sys
import os


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

def main():
    num_processes_input = sys.argv[1]
    num_processes = int(num_processes_input)
    range_start = 100
    range_end = 100000
    total_range = range_end - range_start
    process_range = int(total_range / num_processes)
    print("running the parent processes")
    fork_pids = []
    fork_ranges = []
    fork_totals = []

    for i in range(0, num_processes):
        cur_start = range_start + process_range * i
        cur_end = range_start + process_range * (i + 1) - 1
        fork_ranges.append((cur_start, cur_end))

    for x in range(0, num_processes):
        ret = os.fork()
        if ret == 0:
            print("starting new child process")
            local_count = count_primes_in_range(fork_ranges[x][0], fork_ranges[x][1])
            print("local_count is {0}.".format(local_count))
            fork_totals.append(local_count)
            print("")
            return
        else:
            print("parent process: child pid {0}.".format(ret))
            fork_pids.append(ret)

    for child_pid in fork_pids:
        print("waiting for {0}".format(child_pid))
        os.waitpid(child_pid, 0)
    print("All child threads done!")

    total_primes = 0
    for primes in fork_totals:
        total_primes += primes


if __name__ == "__main__":
    main()