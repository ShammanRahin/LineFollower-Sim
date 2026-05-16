import math
import matplotlib.pyplot as plt

class Robot:
    def __init__(self, wheel_base):
        self.L = wheel_base

        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

        # store trajectory
        self.path_x = []
        self.path_y = []

    def update(self, v_l, v_r, dt):
        v = (v_r + v_l) / 2.0
        omega = (v_r - v_l) / self.L

        self.x += v * math.cos(self.theta) * dt
        self.y += v * math.sin(self.theta) * dt
        self.theta += omega * dt

        self.theta = math.atan2(math.sin(self.theta), math.cos(self.theta))

        # save path
        self.path_x.append(self.x)
        self.path_y.append(self.y)

    def plot(self):
        plt.figure()
        plt.plot(self.path_x, self.path_y)
        plt.scatter(self.path_x[0], self.path_y[0], label="Start")
        plt.scatter(self.path_x[-1], self.path_y[-1], label="End")

        plt.title("Differential Drive Robot Trajectory")
        plt.xlabel("X position (m)")
        plt.ylabel("Y position (m)")
        plt.axis("equal")
        plt.grid()
        plt.legend()
        plt.show()


# ---------------- RUN SIM ----------------
robot = Robot(wheel_base=0.12)

dt = 0.01
steps = 5000

for i in range(steps):
    # example motion: curve
    v_l = 1.2
    v_r = -1.2

    robot.update(v_l, v_r, dt)

robot.plot()