import os
from multiprocessing import Process, current_process


def square(number):
    result = number * number
    process_id = os.getpid()
    process_name = current_process().name
    print(
        f"The number {number} squers to {result}",
        f" with id {process_id} and name: {process_name}"
    )


if __name__ == "__main__":
    processes = []
    numbers = [1, 2, 3, 4]

    for number in numbers:
        process = Process(target=square, args=(number,))
        processes.append(process)
        process.start()
        square(number)
    for txt in processes:
        print(f" *** {txt}")
