from My_Queue import Queue
from updated_queue import UpdatedQueue


if __name__ == '__main__':
    queue = UpdatedQueue(name="queue1", size=3)
    # queue = Queue()
    queue.insert(1)
    queue.insert(2)
    queue.insert(2)

    queue22 = UpdatedQueue(name="queue2", size=4)
    # queue22 = Queue()
    queue22.insert(6)
    queue22.insert(2)
    # queue.pop()
    print(queue)
    # print(queue.is_empty())

    print(UpdatedQueue.get_queue("queue2"))
    # print(queue)
