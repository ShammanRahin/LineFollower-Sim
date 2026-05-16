import math

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
        omega =(v_r - v_l)/ self.L
        self.x += v * math.cos(self.theta) * dt
        self.y += v * math.sin(self.theta) * dt
        self.theta += omega *dt
        
        self.x_pos.append(self.x)
        self.y_pos.append(self.y)
        
        ##normalize theta
        self.theta = math.atan2(math.sin(self.theta), math.cos(self.theta))
        
    def plot(self):
        import matplotlib.pyplot as plt
        plt.style.use("default")
        plt.figure()
        plt.plot(self.x_pos, self.y_pos , label="Path")
        plt.scatter(self.x_pos[0], self.y_pos[0], label="Start")
        plt.scatter(self.x_pos[-1], self.y_pos[-1], label="End")

        plt.title("Differential Drive Robot Trajectory")
        plt.xlabel("X position (m)")
        plt.ylabel("Y position (m)")
        plt.axis("equal")
        plt.grid()
        plt.legend()
        plt.show()
        
        

        