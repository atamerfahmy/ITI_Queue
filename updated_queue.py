from My_Queue import Queue


class UpdatedQueue(Queue):
    all_queues = []

    def __init__(self, data=None, name="", size=10):
        super(UpdatedQueue, self).__init__(data)
        self.name = name
        self.size = size
        UpdatedQueue.all_queues.append(self)

    def insert(self, value):
        if len(self.data) == self.size:
            raise Exception("QueueOutOfRangeException")
        else:
            super(UpdatedQueue, self).insert(value)

    @staticmethod
    def get_queue(name):
        for i in UpdatedQueue.all_queues:
            if i.name == name:
                return i

        return None

