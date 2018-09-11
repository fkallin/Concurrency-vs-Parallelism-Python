import multiprocessing

def sum_and_product(a, b):
    s, p = a + b, a * b
    print(f'{a}+{b}={s}, {a}*{b}={p}')

p = multiprocessing.Process(
    target=sum_and_product, name='SumProd', args=(3, 7)
)

p.start()
