import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


def load_graph_from_json(file_path):
    """
    从JSON文件加载图数据。
    """
    with open(file_path, 'r') as file:
        graph_data = json.load(file)

    G = nx.Graph()
    for edge in graph_data["edges"]:
        G.add_edge(edge["from"], edge["to"], distance=edge["distance"])

    return G
# 创建邻接矩阵并初始化
num_nodes = 10
graph = np.full((num_nodes, num_nodes), float('inf'))

for edge in data["edges"]:
    from_node = edge["from"] - 1
    to_node = edge["to"] - 1
    distance = edge["distance"]
    graph[from_node][to_node] = distance


distance_matrix = np.copy(graph)

for k in range(num_nodes):
    for i in range(num_nodes):
        for j in range(num_nodes):
            if distance_matrix[i][k] + distance_matrix[k][j] < distance_matrix[i][j]:
                distance_matrix[i][j] = distance_matrix[i][k] + distance_matrix[k][j]


print("最短路径矩阵：")
print(distance_matrix)

plt.imshow(distance_matrix, cmap='viridis', interpolation='nearest')
plt.colorbar(label='Distance')
plt.title('Shortest Path Distance Matrix')
plt.show()
