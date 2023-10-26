from math import sqrt
from typing import Self, Type

class Point2D:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        
    def distance_to_origin(self) -> float:
        return round(sqrt(self.x ** 2 + self.y ** 2), 2)
    
    def distance_to_other(self, other:Type[Self]):
        return round(sqrt((self.x - other.x) ** 2 + (self.y - other.y)), 2)
    
point_a = Point2D(3, 5)
point_b = Point2D(10, 4)
print(point_a.distance_to_origin())
print(point_a.distance_to_other(point_b))
