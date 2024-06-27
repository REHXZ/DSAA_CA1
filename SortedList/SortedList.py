from SortedList.Word import Word

"""
LinkedList that when inserting elements it will sort by doing operator overloading using less than <.
"""
class SortedList:
    def __init__(self):
        # Pointer towards the first Node (currently nothing)
        self.headNode = None
        self.currentNode = None
        self.length = 0  # Variable we manually keep track of number of Nodes in the list
    """
    A private function to append element to the start of the LinkedList
    """
    def __appendToHead(self, newNode):
        oldHeadNode = self.headNode
        self.headNode = newNode
        self.headNode.nextNode = oldHeadNode
    """
    The insert function takes in a newNode variable to add it in the LinkedList.
    Raise a TypeError to make sure that the newNode variable is a Word object.
    It loops through using linearSorting algorithm to check each element to see what is __lt__
    """
    def insert(self, newNode):
        if not isinstance(newNode,Word):
            raise TypeError("Only Word Class Objects can be inserted into SortedList")
        self.length += 1
        # If list is currently empty
        if self.headNode == None:
            self.headNode = newNode
            return

        # Check if it is going to be new head
        if newNode < self.headNode:
            self.__appendToHead(newNode)
            return

        # Check it is going to be inserted
        # between any pair of Nodes (left, right)
        leftNode = self.headNode
        rightNode = self.headNode.nextNode
        while rightNode != None:
            if newNode < rightNode:
                leftNode.nextNode = newNode
                newNode.nextNode = rightNode
                return
            leftNode = rightNode
            rightNode = rightNode.nextNode
        # Once we reach here it must be added at the tail
        # Because newNode is largest than all the other nodes.
        leftNode.nextNode = newNode

    """
    Loop through and concatenate the node values together
    """
    def __str__(self):
        # We start at the head
        output = ""
        node = self.headNode
        firstNode = True
        while node != None:
            if firstNode:
                output = f"{node.__str__()}"
                firstNode = False
            else:
                output += (', ' + f"{node.__str__()}")
            node = node.nextNode
        return f"{output}"