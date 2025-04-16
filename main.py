from bst.interval import Interval
from bst.interval_2d import Interval2D
from bst.quadtree import QuadTree
from bst.quadtree_adt import QuadTreeADT

if __name__ == '__main__':
    quad_tree: QuadTreeADT = QuadTree()
    m = [[7, 6, 76],
         [5, 6, 56],
         [1, 1, 11],
         [5, 5, 55],
         [2, 7, 27],
         [3, 3, 33]]
    for a in m:
        quad_tree.insert(a[0], a[1], a[2])

    rect: Interval2D = Interval2D(Interval(1, 8), Interval(4, 8))
    quad_tree.query_2D(rect)