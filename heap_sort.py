from heap import MaxHeap
from collections import deque

def heap_sort(unsorted_list):
    sorted_list = deque()
    heap = MaxHeap(unsorted_list)
    while heap.get_count() > 0:
        sorted_list.appendleft(heap.delete(1))
    return sorted_list