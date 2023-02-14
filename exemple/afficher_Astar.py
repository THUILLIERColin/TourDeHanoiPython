import tkinter as tk
from expemple_AStar import *

class AStarVisualization:
    def __init__(self, maze, path):
        self.maze = maze
        self.path = path
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        self.draw_maze()
        self.draw_path()
        self.root.mainloop()

    def draw_maze(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                x1, y1 = j * 50, i * 50
                x2, y2 = x1 + 50, y1 + 50
                if self.maze[i][j] == 1:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")

    def draw_path(self):
        for i in range(len(self.path) - 1):
            x1, y1 = self.path[i][1] * 50 + 25, self.path[i][0] * 50 + 25
            x2, y2 = self.path[i + 1][1] * 50 + 25, self.path[i + 1][0] * 50 + 25
            self.canvas.create_line(x1, y1, x2, y2, fill="red", width=3)

def main():
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    path = astar(maze, start, end)
    AStarVisualization(maze, path)

if __name__ == "__main__":
    main()
