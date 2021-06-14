#!/user/bin/python3
from threading import Thread
import sys
import time

global prime_count


class Prime_Thread(Thread):
    def __init__(self, start, end, count=0):
        self.start = start
        self.end = end
        self.thread_count = count
        super(Prime_Thread, self).__init__()

    def run(self):
        print("will count primes in range {0} to {1}".format(self.start, self.end))
        global prime_count
        local_count = count_primes_in_range(self.start, self.end)
        print("local_count is {0}. total_count is {1}".format(local_count, prime_count))
        prime_count += local_count

    def __str__(self):
        return "This is a thread"


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
    global prime_count
    prime_count = 0
    range_start = 100
    range_end = 100000
    total_range = range_end - range_start
    my_treads = []
    num_treads_input = sys.argv[1]
    num_treads = int(num_treads_input)
    tread_range = int(total_range / num_treads)
    thread_count = 0

    tread_start = range_start
    while thread_count < num_treads:
        tread_end = tread_start + tread_range
        print("creating thread")
        my_thread = Prime_Thread(tread_start, tread_end, thread_count)
        my_treads.append(my_thread)
        tread_start = tread_end + 1
        thread_count += 1

    time.sleep(1/3)
    print(len(my_treads))

    for t in my_treads:
        print("starting tread")
        print(str(t))
        t.start()
        time.sleep(1)

    for t in my_treads:
        if not t.is_alive():
            t.join()

    print("All done! Counted {0} primes in the range {1} to {2}".format(prime_count, range_start, range_end))


if __name__ == "__main__":
    main()