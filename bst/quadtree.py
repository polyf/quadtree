from typing import List

from bst.interval_2d import Interval2D
from bst.node import Node
from bst.point import Point
from bst.quadtree_adt import QuadTreeADT


class QuadTree(QuadTreeADT):
    def __init__(self) -> None:
        self._root: Node = None

    def clear(self) -> None:
        self._root = None

    def is_empty(self) -> bool:
        return self._root is None

    def insert(self, x: object, y: object, value: object) -> None:
        def insert(current: Node, x: object, y: object, value: object) -> None:
            if current is None:
                return Node(x, y, value)
            elif x < current.x and y >= current.y:
                current.NW = insert(current.NW, x, y, value)
            elif x < current.x and y < current.y:
                current.SW = insert(current.SW, x, y, value)
            elif x >= current.x and y >= current.y:
                current.NE = insert(current.NE, x, y, value)
            elif x >= current.x and y < current.y:
                current.SE = insert(current.SE, x, y, value)
            return current

        self._root = insert(self._root, x, y, value)

    def query_2D(self, rect: Interval2D) -> None:
        def query_2D(current: Node, rect: Interval2D) -> None:
            if current is None:
                return
            x_min = rect.interval_x.min
            x_max = rect.interval_x.max
            y_min = rect.interval_y.min
            y_max = rect.interval_y.max
            if rect.contains(current.x, current.y):
                print(current)
            if x_min < current.x and y_max >= current.y:
                query_2D(current.NW, rect)
            if x_min < current.x and y_min < current.y:
                query_2D(current.SW, rect)
            if x_max >= current.x and y_max >= current.y:
                query_2D(current.NE, rect)
            if x_max >= current.x and y_min < current.y:
                query_2D(current.SE, rect)

        query_2D(self._root, rect)

    def search(self, point: Point) -> object:
        def search(current: Node) -> object:
            if current is None:
                return None
            if current.x == point.x and current.y == point.y:
                return current.value

            if point.x < current.x and point.y >= current.y:
                return search(current.NW)
            elif point.x < current.x and point.y < current.y:
                return search(current.SW)
            elif point.x >= current.x and point.y >= current.y:
                return search(current.NE)
            else:
                return search(current.SE)

        return search(self._root)

    def all_points(self) -> List[Point]:
        def all_points(current: Node) -> List[Point]:
            if current is None:
                return []
            points = [Point(current.x, current.y)]
            points.extend(all_points(current.NW))
            points.extend(all_points(current.NE))
            points.extend(all_points(current.SE))
            points.extend(all_points(current.SW))
            return points

        points_list = all_points(self._root)
        return points_list if points_list else None