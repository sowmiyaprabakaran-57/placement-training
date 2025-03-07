class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, x):
        self.queue.append(x)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue Underflow"
    def is_empty(self):
        return len(self.queue) == 0
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue(), "dequeued from queue")
print("Front element is", q.queue[0] if not q.is_empty() else "Queue is empty")
