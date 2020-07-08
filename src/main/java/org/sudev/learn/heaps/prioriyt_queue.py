from collections import defaultdict


class PQ(object):
    def __init__(self):
        self.heap_holder = [None] * 1000
        self.heap_size = 0

    # function to get right child of a node of a tree
    def get_right_child(self, index):
        r = (2 * index) + 1
        if (r < len(self.heap_holder) and (index >= 1)):
            return r
        return -1

    # function to get left child of a node of a tree
    def get_left_child(self, index):
        l = 2 * index
        if (l < len(self.heap_holder)) and index >= 1:
            return l
        return -1

    # function to get the parent of a node of a tree
    def get_parent(self, index):
        if (index > 1) and (index < len(self.heap_holder)):
            return index // 2
        return -1

    def max_heapify(self, index):
        left_child_index = self.get_left_child(index)
        right_child_index = self.get_right_child(index)

        # finding largest among index, left child and right child
        largest = index

        if ((left_child_index <= self.heap_size) and (left_child_index > 0)):
            if (self.heap_holder[left_child_index] >
                    self.heap_holder[largest]):
                largest = left_child_index

        if ((right_child_index <= self.heap_size and (right_child_index > 0))):
            if (self.heap_holder[right_child_index] >
                    self.heap_holder[largest]):
                largest = right_child_index

        # largest is not the node, node is not a heap
        if (largest != index):
            self.heap_holder[index], self.heap_holder[
                largest] = self.heap_holder[largest], self.heap_holder[index]
            self.max_heapify(largest)

    def build_max_heap(self):
        for i in range(self.heap_size // 2, 0, -1):
            self.max_heapify(i)

    def maximum(self):
        return self.heap_holder[1]

    def extract_max(self):
        maxm = self.heap_holder[1]
        self.heap_holder[1] = self.heap_holder[self.heap_size]
        self.heap_size = self.heap_size - 1
        self.max_heapify(1)
        return maxm

    def increase_key(self, index, key):
        self.heap_holder[index] = key
        parent_index = self.get_parent(index)
        while ((index > 1)
               and (self.heap_holder[parent_index] < self.heap_holder[index])):
            # Swap
            self.heap_holder[index], self.heap_holder[
                parent_indx] = self.heap_holder[
                    parent_index], self.heap_holder[index]
            index = parent_index

    def decrease_key(self, index, key):
        self.heap_holder[index] = key
        self.max_heapify(index)

    def insert(self, key):
        self.heap_size = self.heap_size + 1
        self.increase_key(self.heap_size, key)


if __name__ == '__main__':
    pq = PQ()
    [pq.insert(x) for x in [20, 15, 8, 10, 5, 7, 6, 2, 9, 1]]
    pq.build_max_heap()
    pq.extract_max()