from agents import BFS, DFS
from environment import MazeEnvironment

'''maze = [
    [ 0,  0,   0,    0,   0,   0,  0,  0 ],
    [ 0 , 0,   0,   0,   1,   0,   0,  0 ],
    [ 0,  0,  'g',  0,   0,   0,   0,  0 ],
    [ 0 , 0,   1,   1,   1,   1,   1,  0 ],
    [ 0, 1,   0,    0,   0,   0,   0,  0 ],
    [ 0 , 0,   1,  's',  0,   0,   1,  0 ],
    [ 0,  0,   0,   0,   0,   0,   0,  0 ],
    [ 0 , 0,   0,   0,   0,   0,   0,  0 ]
]'''
maze = [
    ['s', 0,   1,   0,   0],
    [ 1 , 0,   1,   0,   1],
    [ 0 , 0,   0,   0,  'g']
]

print("Labirinto original:")
for row in maze:
    print(row)

env = MazeEnvironment(maze)

''''# Escolha entre BFS e DFS:
choice = input("Escolha o agente de busca (BFS ou DFS): ").strip().upper()

if choice == 'BFS':
    agent = BFS(env)
elif choice == 'DFS':
    agent = DFS(env)

goal = agent.search()
path = agent.get_path(goal)

print(f"\nCaminho encontrado ({choice}):")'''
agent = DFS(env)
goal = agent.search()
path = agent.get_path(goal)
print(path)

maze_with_path = [row.copy() for row in maze]
for r, c in path:
    if maze_with_path[r][c] not in ['s', 'g']:
        maze_with_path[r][c] = '*'

print("\nLabirinto com o caminho marcado:")
for row in maze_with_path:
    print(row)