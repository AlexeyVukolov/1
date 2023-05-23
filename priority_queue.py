import heapq

add_element = lambda queue, _: heapq.heappush(queue, _)

remove_element = lambda queue: heapq.heappop(queue)

size = lambda queue: len(queue)

max = lambda queue: heapq.nlargest(1, queue)

def void(queue):
    num = len(queue)
    if num == 0:
        return 'Очередь пуста'
    else:
        return 'Очередь не пуста'
