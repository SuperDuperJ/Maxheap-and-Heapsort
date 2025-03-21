from collections import deque

class MaxHeap:

    def __init__(self, unsorted_list = []):
        self._count = 0
        self._heap = [None]
        for elt in unsorted_list:
            self.push(elt)
    
    # getters and setters
    def get_count(self):
        return self._count
    
    def set_count(self, count):
        self._count = count
    
    def get_heap(self):
        return self._heap
    
    def peek(self):
        return self._heap[1]

    # index helper methods
    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    # helper methods
    def child_present(self, idx):
        return self.left_child_idx(idx) <= self._count
    
    def parent_present(self, idx):
        return self.parent_idx(idx) >= 1

    def get_larger_child_idx(self, idx):
        # No children
        if self.left_child_idx(idx) > self._count and self.right_child_idx(idx) > self._count:
            return None
        # left child exists but right child does not
        elif self.left_child_idx(idx) <= self._count and self.right_child_idx(idx) > self._count:
            return self.left_child_idx(idx)
        # right child exists but left child does not
        if self.left_child_idx(idx) > self._count and self.right_child_idx(idx) <= self._count:
            return self.right_child_idx(idx)
        # both children exist
        else:
            left_child = self._heap[self.left_child_idx(idx)]
            right_child = self._heap[self.right_child_idx(idx)]
        if left_child > right_child:
            return self.left_child_idx(idx)
        else:
            return self.right_child_idx(idx)        

    # push
    def push(self, value):
        self._count += 1
        self._heap.append(value)
        self.heapify_up(self._count)

    # delete
    def delete(self, idx):
        if idx >= 1 and idx <= self._count:
            deleted_elt = self._heap[idx]
            self._heap[idx] = self._heap[self._count]
            self._count -= 1
            self._heap.pop()
            self.heapify_down(idx)
            return deleted_elt
        else:
            return None


    # heap_pop
    def heap_pop(self):
        self.delete(1)

    # heapify_up
    def heapify_up(self, idx):
        while self.parent_present(idx):
            child = self._heap[idx]
            parent_index = self.parent_idx(idx)
            parent = self._heap[parent_index]
            if parent < child:
                self._heap[parent_index], self._heap[idx] = child, parent
            idx = parent_index

    # heapify_down
    def heapify_down(self, idx):
        while self.child_present(idx):
            parent = self._heap[idx]
            child_index = self.get_larger_child_idx(idx)
            child = self._heap[child_index]
            if parent < child:
                self._heap[idx], self._heap[child_index] = child, parent
            idx = child_index
    
    def __str__(self):
        stack = deque()
        stack.append([self.peek(), 1, 0])
        level_str = "\n"
        #prev_level = 0
        level = 0
        while stack:
            #prev_level = level
            value, idx, level = stack.pop()
            
            if level > 0 and len(stack) > 0 and level <= stack[-1][1]:
                level_str += "   "*(level-1)+ "├─"
            elif level > 0:
                level_str += "   "*(level-1)+ "└─"
            level_str += str(value)
            level_str += "\n"
            level += 1
            left_child_index = self.left_child_idx(idx)
            right_child_index = self.right_child_idx(idx)
            if left_child_index <= self._count:
                stack.append([self._heap[left_child_index], left_child_index, level])
            if right_child_index <= self._count:
                stack.append([self._heap[right_child_index], right_child_index, level])
        return level_str

