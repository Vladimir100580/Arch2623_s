from collections import namedtuple

Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
d = {
    Point(2, 3, 4): 'first',
    Point(10, -100, -500): 'second',
    Point(3, 7, 11): 'last',
}

print(d)
# {Point(x=2, y=3, z=4): 'first', Point(x=10, y=-100, z=-500): 'second', Point(x=3, y=7, z=11): 'last'}

mut_point = Point(2, [3, 4, 5], 6)

print(mut_point)
