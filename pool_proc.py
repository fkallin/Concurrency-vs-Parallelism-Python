from concurrent.futures import ProcessPoolExecutor,	as_completed
from random import randint
from time import sleep


def run(name):
    sleep(0.05)
    value = randint(0, 100)
    print(f'Hi, I am {name} and my value is {value}')
    return (name, value)

with ProcessPoolExecutor(max_workers=3) as executor:
    futures = [
        executor.submit(run, f'P{name}') for name in range(5)
    ]
    for future in as_completed(futures):
        name, value = future.result()
        print(f'Process {name} returned {value}')
