def my_generators():
    print('1st item')
    yield 10

    print('2nd item')
    yield 20

    print('3rd item')
    yield 30


gen = my_generators()

next(gen)
next(gen)

next(gen)  # stop iteration error as elements executed


def get_sequence_up_to(x):
    for i in range(x):
        yield i


seq = get_sequence_up_to(10)

next(seq)
next(seq)
