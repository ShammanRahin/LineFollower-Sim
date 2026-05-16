import math
import matplotlib.pyplot as plt

class Robot:
    def __init__(self ,wheel_base: float) -> None:
        self.L = wheel_base
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        
        self.x_pos =[]
        self.y_pos = []
        
    def update(self , v_l: float , v_r : float , dt : float):
        v = (v_l + v_r )/ 2
        omega =(v_l - v_r )/ self.L
        self.x += v * math.cos(self.theta) * dt
        self.y += v * math.sin(self.theta) * dt
        self.theta += omega *dt
        
        self.x_pos.append(self.x)
        self.y_pos.append(self.y)
        
        ##normalize theta
        self.theta = math.atan2(math.sin(self.theta), math.cos(self.theta))
        
    def plot(self):
        pass
        