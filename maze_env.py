import gym
import numpy as np
import matplotlib.pyplot as plt

class MazeEnv(gym.Env):
    def __init__(self):
        self.action_list = np.array([[0, 1], [0, -1], [1, 0], [-1, 0]])

        self.map = np.array([["s", 1, 1, 1, 1, 0, 1, 1, 1, 1, 1,  1 ],
                             [ 1 , 1, 1, 1, 1, 0, 1, 1, 1, 1, 1,  1 ],
                             [ 0 , 0, 1, 1, 1, 0, 1, 1, 0, 1, 0,  0 ],
                             [ 1 , 1, 1, 0, 0, 0, 1, 1, 0, 1, 1,  1 ],
                             [ 1 , 1, 1, 0, 1, 0, 1, 1, 0, 1, 1,  1 ],
                             [ 1 , 0, 0, 0, 1, 0, 1, 1, 0, 0, 0,  1 ],
                             [ 1 , 1, 1, 1, 1, 0, 1, 1, 0, 1, 1,  1 ],
                             [ 1 , 1, 1, 1, 0, 0, 1, 0, 0, 1, 1,  1 ],
                             [ 1 , 1, 1, 1, 0, 1, 1, 0, 1, 1, 0,  1 ],
                             [ 1 , 0, 0, 1, 0, 1, 1, 0, 1, 1, 0,  1 ],
                             [ 1 , 0, 0, 1, 1, 1, 1, 0, 1, 0, 0,  0 ],
                             [ 1 , 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, "g"]], dtype=object)

        action_num = 4
        self.action_space = gym.spaces.Discrete(action_num)
        self.max_position = [self.map.shape[1]-1, self.map.shape[0]-1]
        self.min_position = [0, 0]
        high = np.array(self.max_position, dtype=np.float32)
        low = np.array(self.min_position, dtype=np.float32)
        self.observation_space = gym.spaces.Box(low, high, dtype=np.float32)
        
        self.fig = plt.figure(figsize=(7,7))
        self.ax = self.fig.add_subplot(111)

        self.reset()

    def step(self, action_num):
        action = self.action_list[action_num]
        robot_position = self.state + action
        x, y = robot_position
        if x > self.max_position[1] or y > self.max_position[0] or x < self.min_position[1] or y < self.min_position[0]:
            pass
        elif self.map[y][x] != 0: 
            self.state = robot_position
        
        done = bool(self.map[self.state[0]][self.state[1]] == "g")

        if done:
            reward = 100
        else:
            reward = -1
        
        return self.state, reward, done, {}

    def reset(self):
        self.state = [0, 0]
        return self.state

    def render(self):
        plt.xlim(0, self.map.shape[1])
        plt.ylim(0, self.map.shape[0])
        vgpoint = np.arange(0, self.map.shape[0], 1)
        hgpoint = np.arange(0, self.map.shape[1], 1)
        plt.vlines(vgpoint, 0, self.map.shape[0], linewidth=0.3)
        plt.hlines(hgpoint, 0, self.map.shape[1], linewidth=0.3)
        
        for y in range(self.map.shape[0]):
            for x in range(self.map.shape[1]):
                if self.map[y][x] == "s":
                    #plt.plot(x, y, marker="o", color="r", markersize=10, alpha = 0.9)
                    plt.axvspan(xmin=x, xmax=x+1, ymin=y/self.map.shape[0], ymax=(y+1)/self.map.shape[0], color = "c", alpha=0.5)
                    plt.text(x+0.5, y, "start", horizontalalignment='center', size=10, alpha=0.9, color="b")
                elif self.map[y][x] == "g":
                    plt.plot(x+0.5, y+0.5, marker="*", color="y", markersize=20, alpha = 0.9)
                elif self.map[y][x] == 0:
                    plt.axvspan(xmin=x, xmax=x+1, ymin=y/self.map.shape[0], ymax=(y+1)/self.map.shape[0], color = "k", alpha=0.9)
        
        plt.plot(self.state[0]+0.5, self.state[1]+0.5, marker="o", color="r", markersize=20, alpha = 0.9)

        plt.axis([0, self.map.shape[1], 0, self.map.shape[0]])
        self.ax.set_aspect('equal')
        plt.pause(0.00001)
        plt.cla()

