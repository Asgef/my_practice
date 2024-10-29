from inspect import getgeneratorstate
from time import sleep


def corutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class BlaBlaException(Exception):
    pass


@corutine
def average():
    count = 0
    sum = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
            break
        except BlaBlaException:
            print(">>>>>>>>>>")
            break
        else:
            count += 1
            sum += x
            average = round(sum / count, 2)
    return average


g = average()
getgeneratorstate(g)
g.send(5)
g.send(6)
g.send(1)

try:
    g.throw(StopIteration)
except StopIteration as e:
    print('Average', e.value)

# Done
# Average 4.0


##############################################################################


def corutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class BlaBlaException(Exception):
    pass


def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            break
        else:
            print('..............', message)
    return 'Returned from subgen()'


@corutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaException as e:
    #         g.throw(e)
    result = yield from g
    print(result)


sg = subgen()
g = delegator(sg)
g.send('asdf')
g.throw(StopIteration)


##############################################################################


queue = []


def counter():
    counter = 0
    while True:
        print(counter)
        counter += 1
        yield


def printer():
    counter = 0
    while True:
        if counter % 3 == 0:
            print('Bang!')
        counter += 1
        yield


def main():
    while True:
        g = queue.pop(0)
        next(g)
        queue.append(g)
        sleep(0.5)


if __name__ == '__main__':
    g1 = counter()
    queue.append(g1)
    g2 = printer()
    queue.append(g2)
    main()
