# Analysis of best and worst running times of each function

## find_left(index), find_right(index), find_parent(index), get_value(index)
### index calculations or array lookups
### time complexity:
#### best case: O(1)
#### worst case: O(1)
### just a math calculation / array lookup, doesn't depend on heap size

## heap(index)
### recursively move a node down to restore max-heap property
### time complexity:
#### best case: O(1) -> node already larger than both children, so no swaps
#### worst case: O(log n) -> node moves all the way from root to leaf
### max heap height is log n, so at most that many swaps

## build_heap()
### call heap on every non-leaf node, from last parent to root
### time complexity:
#### best case: O(n) -> all nodes are already heaps, so heap does little work
#### worst case: O(n) -> building heap is still O(n) overall
### most nodes near the bottom, and few swaps needed, so total work adds to linear time

## heap_sort()
### builds heap, repeatedly swaps root with last element and heapify down
### time complexity:
#### best case -> O(n log n) -> heap property still requires log n swaps per extraction
#### worst case -> same as best case, each of the extractions may require log n swaps
### each of the n extractions may require log n swaps

## extract_max()
### removes the root, replaces it with last element, heapify down
### time complexity:
#### best case -> heap has only one element or new root is already larger than children
#### worst case -> O(log n) -> new root moves all the way down to a leaf
### only the path from root to leaf matters

## insert(value)
### append value and bubble it up
### time complexity:
#### best case: value is smaller than its parent, so no swaps needed
#### worst case: O(log n) -> value bubbles all the way up to the root
### at most it travels the height of the heap