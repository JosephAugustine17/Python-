from week4_DLL import DNode, DoubleLinkedList


def reverse_merge(dll1, dll2):
    '''(DoubleLinkedList, DoubleLinkedList) -> DoubleLinkedList
    '''
    final = DoubleLinkedList()
    while((not dll1.is_empty()) and (not dll2.is_empty())):
        if(dll1.get_first().get_element() < dll2.get_last().get_element()):
            final.add_last(dll1.get_first().get_element())
            dll1.remove_first()
        elif(dll1.get_first().get_element() > dll2.get_last().get_element()):
            final.add_last(dll2.get_last().get_element())
            dll2.remove_last()
        else:
            final.add_last(dll1.get_first().get_element())
            dll1.remove_first()
            dll2.remove_last()
    if(dll1.is_empty() and (not dll2.is_empty())):
        while(not dll2.is_empty()):
            final.add_last(dll2.get_last().get_element())
            dll2.remove_last()
    elif(dll2.is_empty() and (not dll1.is_empty())):
        while(not dll1.is_empty()):
            final.add_last(dll1.get_first().get_element())
            dll1.remove_first()
    return final


def allocate_room(dll, room, capacity, index):
    '''(DoubleLinkedList, str, int, int) -> str
    '''
    counter = 0
    while(counter < index):
        dll.remove_first()
        counter = counter + 1
    first_initials = dll.get_first().get_element()[0:2]
    if(dll.size() < capacity-index):
        print(dll.get_last().get_element())
        last_initials = dll.get_last().get_element()[0:2]
    else:
        while(counter < index+capacity-1):
            dll.remove_first()
            counter = counter + 1
        last_initials = dll.get_first().get_element()[0:2]
    result = room + " " + first_initials.upper() + "-" + last_initials.upper()
    return (result)

if (__name__ == "__main__"):
    dll1 = DoubleLinkedList()
    dll2 = DoubleLinkedList()
    dll1.add_last("Ali")
    dll1.add_last("Bqad")
    dll1.add_last("Brad")
    dll1.add_last("Creed")
    dll2.add_last("Moradi")
    dll2.add_last("Hopkins")
    dll2.add_last("Auer")
    dll2.add_last("Arnold")
    print(dll1)
    print(dll2)
    finaldll = reverse_merge(dll1, dll2)
    print(finaldll)
    print (allocate_room(finaldll, "SW", 3, 1))
