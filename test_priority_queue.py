import priority_queue
import heapq

queue = []
heapq.heapify(queue)

buffer = True
while(buffer == True):
    num = input('1: Проверка очереди\n'
              '2: Размер очереди\n'
              '3: Добавление элемента\n'
              '4: Удаление элемента\n'
              '5: Просмотр очереди\n'
              '6: Просмотр максимального элемента\n'
              '7: Выход\n')

    if num == '1':
            print(priority_queue.void(queue))
    elif num == '2':
            print(priority_queue.size(queue))
    elif num == '3':
            priority_queue.add_element(queue, int(input('Какой элемент добавить? ')))
    elif num == '4':
            priority_queue.remove_element(queue)
    elif num == '5':
            print(queue)
    elif num == '6':
            print(priority_queue.max(queue))
    elif num == '7':
            buffer = False
    print()
