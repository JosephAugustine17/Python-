def merge_heap(marzieh, nick):
    '''(Heap, Heap) -> Heap
    Takes two heaps and merges them together
    '''
    # Create new heap which will contain both heaps in paramaters
    merge_heap = Heap(None)
    # loop through both heaps inserting all data
    while nick.is_empty() != True:
        data = nick.extract_min()
        merge_heap.insert(data)
    while marzieh.is_empty() != True:
        data2 = marzieh.extract_min()
        merge_heap.insert(data2)
        # fix the order so that the heap has the property that children are greater than parents
        merge_heap.upheap_bubbling()
    # return back heap
    return merge_heap



def first_and_last(heap1):
    '''(Heap) -> tuple of obj
    given a heap return a tuple representing the first and last nodes
    '''
    if(heap1.is_empty()):
        result = ()
    else:
        first = heap1.min()
        last = heap1.remove_last_node()
        heap1.insert(last)
        result = (first, last)

    return result