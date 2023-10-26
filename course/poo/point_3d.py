from typing import Type, Self
from math import sqrt
from point_2d import Point2D

class Point3D(Point2D):
    def __init__(self, x: float, y: float, z: float) -> None:
        super().__init__(x, y)
        self.z = z
        
    def distance_to_origin(self) -> float:
        return round(sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2), 2)
    
    def distance_to_other(self, other: type[Self]):
        return round(sqrt((self.x - other.x - other.z) ** 2 + (self.y - other.y - other.z)), 2)
    
toto = Point3D(25, 35, 50)
toto2 = Point3D(65, 45, 20)
print(toto.distance_to_origin())
print(toto.distance_to_other(toto2))