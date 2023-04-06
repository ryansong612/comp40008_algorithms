class Arc:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def set_start(self, new_start):
        self.start = new_start

    def set_end(self, new_end):
        self.end = new_end

    def __eq__(self, other):
        return isinstance(other, Arc) \
               and (other.start == self.start) \
               and (other.end == self.end)

    def __str__(self):
        return f"Arc({self.start}, {self.end})"
