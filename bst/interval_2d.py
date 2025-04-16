from bst.interval import Interval


class Interval2D:
    def __init__(self, interval_x: Interval, interval_y: Interval) -> None:
        self.interval_x = interval_x
        self.interval_y = interval_y

    def contains(self, x: object, y: object) -> bool:
        return self.interval_x.contains(x) and self.interval_y.contains(y)