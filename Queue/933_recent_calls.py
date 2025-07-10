from collections import deque
class RecentCounter:

    def __init__(self):
        self.PING_CHECK_PERIOD = 3000
        self.time_queue = deque()

    def ping(self, t: int) -> int:
        self.time_queue.append(t)
        while self.time_queue and self.time_queue[0] < t - self.PING_CHECK_PERIOD:
            self.time_queue.popleft()
        return len(self.time_queue)