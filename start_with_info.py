import threading
from time import sleep

def sum_and_product(a, b):
    sleep(.2)
    s, p = a + b, a * b
    print(f'{a}+{b}={s}, {a}*{b}={p}')


def status(t):
    if t.is_alive():
        print(f'Thread {t.name} is alive.')
    else:
        print(f'Thread {t.name} has terminated.')

def print_current():
    print('The current thread is {}.'.format(
        threading.currentThread()
    ))
    print('Threads: {}'.format(list(threading.enumerate())))

print_current()
t = threading.Thread(
    target=sum_and_product, name='SumProd', args=(3, 7)
)

t.start()
status(t)
t.join()
status(t)
