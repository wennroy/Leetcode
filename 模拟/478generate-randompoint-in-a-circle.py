import random
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.center = [x_center, y_center]

    def randPoint(self) -> List[float]:
        radius = self.radius * math.sqrt(random.random())
        theta = random.random() * math.pi * 2
        x = math.cos(theta) * radius
        y = math.sin(theta) * radius
        return [self.center[0] + x, self.center[1] + y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()