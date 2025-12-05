# algorithms.py

def fcfs(requests, head):
    return requests


def sstf(requests, head):
    order = []
    pool = requests.copy()

    while pool:
        nearest = min(pool, key=lambda x: abs(x - head))
        order.append(nearest)
        head = nearest
        pool.remove(nearest)

    return order


def scan(requests, head):
    data = sorted(requests)
    left = [x for x in data if x < head]
    right = [x for x in data if x >= head]
    return right + left[::-1]


def cscan(requests, head):
    data = sorted(requests)
    right = [x for x in data if x >= head]
    left = [x for x in data if x < head]
    return right + left


def look(requests, head):
    data = sorted(requests)
    left = [x for x in data if x < head]
    right = [x for x in data if x >= head]
    return right + left[::-1]
