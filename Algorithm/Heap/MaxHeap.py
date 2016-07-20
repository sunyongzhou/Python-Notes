import heapq


class MaxHeap(heapq):
    """Push item into max heap, and maintain the heap invariant"""
    def _heappush_max(self, heap, item):
        heap.append(item)
        heapq._siftdown_max(heap, 0, len(heap) - 1)


