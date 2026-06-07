import heapq
from typing import Self
from dataclasses import dataclass

@dataclass
class Task:
    letter: str
    frequency: int

    def __lt__(self, other: Self) -> bool:
        return self.frequency < other.frequency

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_frequencies: dict[str, int] = defaultdict(int)

        for task in tasks:
            task_frequencies[task] += 1

        heap: list[Task] = [Task(k, task_frequencies[k]) for k in task_frequencies]
        heapq.heapify_max(heap)

        queue: deque[tuple[Task, int]] = deque()

        counter = 0
        while len(queue) > 0 or len(heap) > 0:
            if len(queue) > 0 and counter - queue[0][1] > n:
                task, _ = queue.popleft()
                if task.frequency >= 1:
                    heapq.heappush_max(heap, task)

            if len(heap) > 0:
                task = heapq.heappop_max(heap)
                task.frequency = task.frequency - 1
                if task.frequency > 0:
                    queue.append((task, counter))
            counter += 1

        return counter

        



