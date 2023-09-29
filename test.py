import math
from collections import namedtuple
Point = namedtuple('Point', 'x, y')

point1=Point(200.0,300.0)
point2=Point(100,200)
def get_food_place(point1,point2):
        distance = math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)
        
        dx = point2.x - point1.x
        dy = point2.y - point1.y
        angle = math.degrees(math.atan2(dy, dx))
        
        return distance,angle

print(get_food_place(point1,point2))