# simulator.py

def simulate(order, start_head):
    head = start_head
    total_seek = 0
    movement = [head]

    for r in order:
        total_seek += abs(r - head)
        head = r
        movement.append(head)

    average_seek = total_seek / len(order)
    return total_seek, average_seek, movement
