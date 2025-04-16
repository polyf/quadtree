class Interval:
    def __init__(self, min: object, max: object) -> None:
        self.min = min
        self.max = max

    def contains(self, x: object) -> bool:
        return self.min <= x <= self.max

