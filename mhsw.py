import time
from typing import Dict, List, Tuple

class MHSW:
    def __init__(self, window: float = 5.0):
        self.heap : List[Tuple[float, Tuple[str, str], List[float]]] = []
        self.window = window

    def parent(self, i): return (i - 1) // 2
    def left(self, i):   return 2 * i + 1
    def right(self, i):  return 2 * i + 2

    def push(self, entry: Tuple):
        self.heap.append(entry)
        self.heapify_up(len(self.heap) - 1)

    def pop(self) -> Tuple:
        if not self.heap:
            raise IndexError("empty heap")
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        entry = self.heap.pop()
        if self.heap:
            self.heapify_down(0)
        return entry

    def heapify_up(self, i):
        while i > 0:
            p = self.parent(i)
            if self.heap[i][0] < self.heap[p][0]:
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p
            else:
                break

    def heapify_down(self, i):
        n = len(self.heap)
        while True:
            smallest = i
            l, r = self.left(i), self.right(i)
            if l < n and self.heap[l][0] < self.heap[smallest][0]:
                smallest = l
            if r < n and self.heap[r][0] < self.heap[smallest][0]:
                smallest = r
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    def evict(self):
        cutoff = time.time() - self.window
        while self.heap and self.heap[0][0] < cutoff:
            self.pop()

    def insert(self, source: str, target: str, weights: List[float]):
        if source == target:
            raise ValueError("must be two different electrodes")
        edge = (source, target) if source < target else (target, source)
        self.push((time.time(), edge, weights))
        return edge

    def snapshot(self) -> Dict[Tuple[str, str], List[float]]:
        self.evict()
        state : Dict[Tuple[str, str], List[float]] = {}
        for timestamp, edge, weights in sorted(self.heap, key=lambda x: x[0]):
            state[edge] = weights  # latest entry per edge wins
        return state
