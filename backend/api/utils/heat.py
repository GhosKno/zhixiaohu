from queue import LifoQueue
import copy

from api.models import Topic

DEFAULT_QUEUE_SIZE = 100


class HeatQueue(object):
    queue = LifoQueue(DEFAULT_QUEUE_SIZE)

    @classmethod
    def put(cls, topic):
        if cls.queue.full():
            old = cls.queue.get()
            old.heat -= 1
            old.save()
        cls.queue.put(topic)
        topic.heat += 1
        topic.save()

    @classmethod
    def from_str(cls, string):
        list_id = string.split(' ')
        list_id.pop(len(list_id)-1)
        for topic_id in list_id:
            topic = Topic.objects.get(id=topic_id)
            cls.queue.put(topic)

    @classmethod
    def to_str(cls):
        temp = copy.copy(cls.queue)
        string = ''
        while not temp.empty():
            string += temp.get().id +' '
        return string