import threading
import random
import time


class Philosopher(threading.Thread):
    running = True  # used to check if everyone is finished eating

    def __init__(self, index, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while self.running:
            # Philosopher is thinking
            time.sleep(30)
            print(f"Philosopher {self.index} is hungry.")
            self.dine()

    def dine(self):
        # if both the semaphores(forks) are free,
        # then philosopher will eat
        fork1, fork2 = self.left_fork, self.right_fork
        while self.running:
            fork1.acquire()  # wait operation on left fork
            locked = fork2.acquire(False)
            if locked:
                break  # if right fork is not available leave left fork
            fork1.release()
            print(f"Philosopher {self.index} swaps forks.")
            fork1, fork2 = fork2, fork1
        else:
            return

        self.dining()
        # release both the fork after dining
        fork2.release()
        fork1.release()

    def dining(self):
        print(f'Philosopher {self.index} starts eating.')
        time.sleep(30)
        print(
            f'Philosopher {self.index} finishes eating and leaves to think.'
        )


def main():
    # initialising array of semaphore i.e forks
    forks = [threading.Semaphore() for n in range(5)]

    # here (i+1)%5 is used to get right and left forks circularly between 1-5
    philosophers = [
        Philosopher(i, forks[i % 5], forks[(i + 1) % 5]) for i in range(5)
    ]

    Philosopher.running = True
    for p in philosophers:
        p.start()
    time.sleep(100)
    Philosopher.running = False
    print("Now we're finishing.")


if __name__ == "__main__":
    main()
