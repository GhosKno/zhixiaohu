from queue import LifoQueue
import copy

from api.models import Topic

DEFAULT_QUEUE_SIZE = 100


class HeatQueue(object):
    answered_queue = LifoQueue(DEFAULT_QUEUE_SIZE)
    visited_queue = LifoQueue(DEFAULT_QUEUE_SIZE)

    @classmethod
    def put_answered(cls, topic):
        if cls.answered_queue.full():
            old = cls.answered_queue.get()
            old.heat -= 5
            old.save()
        cls.answered_queue.put(topic)
        topic.heat += 5
        topic.save()

    @classmethod
    def put_visited(cls, topic):
        if cls.visited_queue.full():
            old = cls.visited_queue.get()
            old.heat -= 1
            old.save()
        cls.visited_queue.put(topic)
        topic.heat += 1
        topic.save()

    @classmethod
    def from_str(cls, string):
        list_id = string.split(' ')
        list_id.pop(len(list_id)-1)
        for topic_id in list_id:
            topic = Topic.objects.get(id=topic_id)
            cls.answered_queue.put(topic)

    @classmethod
    def to_str(cls):
        temp = copy.copy(cls.answered_queue)
        string = ''
        while not temp.empty():
            string += temp.get().id +' '
        return string