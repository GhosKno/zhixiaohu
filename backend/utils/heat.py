from queue import LifoQueue

DEFAULT_QUEUE_SIZE = 100


class HeatQueue(object):
    queue = LifoQueue(DEFAULT_QUEUE_SIZE)

    @classmethod
    def put(cls, topic):
        if cls.queue.full():
            old = cls.queue.get()
            old.heat -= 1
        cls.queue.put(topic)
        topic.heat += 1
