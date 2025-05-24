class MazeEnvironment:
    def __init__(self,maze):

        self.start, self.goal= self.pos_start_goal(maze)
        self.maze = maze

    def pos_start_goal(self, maze):
        start = None
        goal = None
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == 'g':
                    goal = (i,j)
                if maze[i][j] == 's':
                    start = (i,j)

        return start, goal

    def get_neighbors(self, pos):
        actions = [
            (pos[0], pos[1] + 1),  # direita
            (pos[0], pos[1] - 1),  # esquerda
            (pos[0] + 1, pos[1]),  # baixo
            (pos[0], pos[1])  # posição atual
        ]
        neighbors = []
        for action in actions:
            i, j = action
            # Se está dentro do tabuleiro
            if 0 <= i < len(self.maze) and 0 <= j < len(self.maze[0]):
                # Se é uma posição livre ou o objetivo
                if self.maze[i][j] == 0 or self.maze[i][j] == 'g':
                    # Ignora a posição atual como vizinha
                    if action != pos:
                        neighbors.append(action)
        return neighbors