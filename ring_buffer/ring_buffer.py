from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # print(item)
        if self.capacity == len(self.storage):
            # Need a condition when current is None. Need to move it to the end
            if self.current is None:
                self.current = self.storage.tail
            #When current has a value, it should be the item
            self.current.value = item
            #if there is a previous, then set the previous as the current, otherwise set to tail
            if self.current.prev:
                self.current = self.current.prev
            else: 
                self.current = self.storage.tail
        elif len(self.storage) < self.capacity: # if it hasn't reached the capcity, then add the item to the head
            self.storage.add_to_head(item)

    def get(self):
        list_buffer_contents = []
        storage_node = self.storage.tail
        while storage_node:
            if storage_node.value is not None:
                list_buffer_contents.append(storage_node.value)
            storage_node = storage_node.prev

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
