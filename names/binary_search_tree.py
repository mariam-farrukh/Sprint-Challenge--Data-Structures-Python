import sys
sys.path.append('../queue_and_stack')

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        # self.queue = Queue()
        # self.stack = Stack()
        

    # Insert the given value into the tree
    def insert(self, value):
        # If the value is less than than the value of the node being compared, go left
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else: #else go right which would be >= self.value
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            return False
        else:
            if self.right:
                return self.right.contains(target)
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        return self.value # This is if it's not on the right, so then the first node on the left is the max value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

        # How to do this iterativly:
        # self.stack.push(self)
        # while self.stack.len() > 0
        #   current_node = stack.pop()
        #   if current_node.right:
        #       stack.push(current_node.right)
        #   if current_node.left:
        #       stack.push(current_node.left)
        #   cb(current_node.value) 


    # # Print all the values in order from low to high
    # # Hint:  Use a recursive, depth first traversal
    # def in_order_print(self, node):
    #     if node is not None:
    #         self.in_order_print(node.left)
    #         print(node.value)
    #         self.in_order_print(node.right)

    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    # # Means that we're going in order of it appearing so like a queue/ line
    # def bft_print(self, node):
    #     self.queue.enqueue(self)
    #     while(self.queue.size > 0):
    #         node = self.queue.dequeue()
    #         # check if it has children
    #         if node.right:
    #             self.queue.enqueue(node.right)
    #         if node.left:
    #             self.queue.enqueue(node.left)
    #         print(node.value)

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # # Means that we're going through the stack on one side first
    # def dft_print(self, node):
    #     self.stack.push(self)
    #     while(self.stack.size > 0):
    #         node = self.stack.pop()
    #         if node.left is not None:
    #             self.stack.push(node.left)
    #         if node.right is not None:
    #             self.stack.push(node.right)
    #         print(node.value)

    # # STRETCH Goals -------------------------
    # # Note: Research may be required

    # # Print In-order recursive DFT
    # def pre_order_dft(self, node):
    #     if node:
    #         print(node.value)
    #         self.pre_order_dft(node.left)
    #         self.pre_order_dft(node.right)

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     if node:
    #         self.post_order_dft(node.left)
    #         self.post_order_dft(node.right)
    #         print(node.value)
