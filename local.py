import threading
from random import randint

local = threading.local()

def run(local, barrier):
    local.my_value = randint(0, 100)
    t = threading.currentThread()
    print(f'Thread {t.name} has value {local.my_value}')
    barrier.wait()
    print(f'Thread {t.name} still has value {local.my_value}')


count = 3
barrier = threading.Barrier(count)
threads = [
        threading.Thread(
            target=run, name=f'T{name}', args=(local, barrier)
        ) for name in range(count)
]

for t in threads:
    t.start()
