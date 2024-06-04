from SortedList.node import Node

class Word(Node):
    def __init__(self, name, frequency=1):
        self.original_name = name  # Store original case
        self.name = name.lower().strip()  # Normalize to lower case for comparison
        self.frequency = frequency
        super().__init__()

    def size(self):
        return len(self.name)

    def __eq__(self, otherNode):
        if otherNode is None:
            return False
        return self.name == otherNode.name

    def __lt__(self, otherNode):
        if otherNode is None:
            raise TypeError(
                "'<' not supported between instances of 'Word' and 'NoneType'")
        if self.frequency == otherNode.frequency:
            return self.name < otherNode.name
        return self.frequency > otherNode.frequency

    def __str__(self):
        return f'{self.original_name}: {self.frequency}'