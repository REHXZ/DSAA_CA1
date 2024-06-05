from SortedList.node import Node

class Word(Node):
    def _init_(self, name, frequency=1):
        self.original_name = name  # Store original case
        self.name = name.lower().strip()  # Normalize to lower case for comparison
        self.frequency = frequency
        super()._init_()

    def size(self):
        return len(self.name)

    def _eq_(self, otherNode):
        if otherNode is None:
            return False
        return self.name == otherNode.name

    def _lt_(self, otherNode):
        if otherNode is None:
            raise TypeError(
                "'<' not supported between instances of 'Word' and 'NoneType'")
        if self.frequency == otherNode.frequency:
            return self.name < otherNode.name
        return self.frequency > otherNode.frequency

    def _str_(self):
        return f'{self.original_name}: {self.frequency}'