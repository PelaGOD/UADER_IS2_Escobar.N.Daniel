class StringCollection:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return ForwardIterator(self.data)

    def reverse_iterator(self):
        return ReverseIterator(self.data)


class ForwardIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            char = self.data[self.index]
            self.index += 1
            return char
        else:
            raise StopIteration


class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            char = self.data[self.index]
            self.index -= 1
            return char
        else:
            raise StopIteration
