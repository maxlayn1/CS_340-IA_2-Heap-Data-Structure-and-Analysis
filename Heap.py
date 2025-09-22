class Heap:                                                 # constructor to initialize the array
    def __init__(self):
        self.data = []

    def __del__(self):
        del self.data

    def find_left(self, index):                             # returns index of left child
        left = index * 2 + 1
        if left < len(self.data):                           # will only return if within bounds
            return left
        else:
            return None

    def find_right(self, index):
        right = index * 2 + 2
        if right < len(self.data):
            return right
        else:
            return None

    def find_parent(self, index):                          # find the parent index to a given node
        if index != 0:
            parent = (index - 1) // 2                      # floor of index - 1 for parent index          
            return parent
        else:
            return None

    def get_value(self, index):                            # return value of element at given index
        if index < len(self.data):
            return self.data[index]
        else:
            return None

    def heap(self, index):
        node_val = self.get_value(index)

        # get child indices
        left_index = self.find_left(index)
        right_index = self.find_right(index)

        # get child values and use neg inf if None
        left_val = self.get_value(left_index) if left_index is not None else float('-inf')
        right_val = self.get_value(right_index) if right_index is not None else float('-inf')

        if left_val > right_val:                        # determine largest chile
            largest_child_index = left_index
        else:
            largest_child_index = right_index

        # swap with largest child if needed and recursively heapify
        if largest_child_index is not None and node_val < self.get_value(largest_child_index):
            self.data[index], self.data[largest_child_index] = self.data[largest_child_index], self.data[index]
            self.heap(largest_child_index)

    def build_heap(self):
        last_parent_index = (len(self.data) // 2) - 1
        while (last_parent_index != -1):
            self.heap(last_parent_index)
            last_parent_index -= 1

    def heap_sort(self):                                    
        self.build_heap()
        end = len(self.data) - 1
        while end > 0:
            self.data[0], self.data[end] = self.data[end], self.data[0] 
            orig_data = self.data
            self.data = self.data[:end]                     # temporarily reduce heap size
            self.heap(0)
            self.data = orig_data                           # restore full array
            end -= 1

    def extract_max(self):
        if (len(self.data) == 0):
            return None
        elif (len(self.data) == 1):
            return self.data.pop()
        
        max_value = self.data[0]
        last_value = self.data.pop()
        self.data[0] = last_value
        self.heap(0)
        return max_value
    
    def insert(self, value):
        self.data.append(value)
        current_index = len(self.data) - 1

        while current_index > 0:
            parent_index = self.find_parent(current_index)
            if self.data[current_index] > self.data[parent_index]:
                self.data[current_index], self.data[parent_index] = self.data[parent_index], self.data[current_index]
                current_index = parent_index
            else:
                break

def main():
    '''heap = Heap()

    for value in [50, 30, 40, 10, 20, 60]:
        print(f"Inserting {value}...")
        heap.insert(value)
        print("Heap array:", heap.data)

    for _ in range(3):
        max_val = heap.extract_max()
        print(f"Extracted max: {max_val}")
        print("Heap array after extraction:", heap.data)

    print("\nBuilding heap from current data...")
    heap.build_heap()
    print("Heap array after build_heap:", heap.data)

    print("\nPerforming heap sort...")
    heap.heap_sort()
    print("Heap array after heap_sort:", heap.data)'''

if __name__ == "__main__":
    main()
