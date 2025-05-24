class BFS:
    def __init__(self, env):
        self.env = env
        self.goal = env.goal
        self.visited = {env.start: ''}
        self.F = [env.start]

    def search(self):
        while self.F:
            node = self.F.pop(0)
            if node == self.goal:
                return node
            for v in self.env.get_neighbors(node):
                if v not in self.visited:
                    self.visited[v] = node
                    self.F.append(v)

    def get_path(self, goal):
        node = goal
        path = [node]
        while self.visited[node] != '':
            node = self.visited[node]
            path.append(node)
        path.reverse()
        return path


class DFS:
    def __init__(self, env):
        self.env = env
        self.goal = env.goal
        self.visited = {env.start: ''}
        self.F = [env.start]

    def search(self):
        while self.F:
            node = self.F.pop()
            if node == self.goal:
                return node
            for v in self.env.get_neighbors(node):
                if v not in self.visited:
                    self.visited[v] = node  # garantir que só marca se for novo
                    self.F.append(v)

    def get_path(self, goal):
        node = goal
        path = [node]
        while self.visited[node] != '':
            node = self.visited[node]
            path.append(node)
        path.reverse()
        return path