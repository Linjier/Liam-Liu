import networkx as nx
import matplotlib.pyplot as plt
import heapq
import json


def load_graph_from_json(file_path):
    """
    从JSON文件加载图数据。
    """
    with open(file_path, 'r') as file:
        graph_data = json.load(file)

    G = nx.Graph()
    for edge in graph_data["edges"]:
        G.add_edge(edge["from"], edge["to"], distance=edge["distance"], congestion=edge["congestion"])

    return G


def heuristic(G, current, target):
    """
    启发函数，基于当前节点到目标节点的拥挤程度估计。
    """
    congestion_levels = {"Low": 1, "Medium": 2, "High": 3}
    congestion = 0
    if G.has_edge(current, target):
        congestion = congestion_levels.get(G[current][target]['congestion'], 1)
    return congestion


def a_star_search(G, start, goal):
    """
    使用 A* 算法寻找最短路径。
    """
    open_set = [(0, start, [start])]
    heapq.heapify(open_set)

    while open_set:
        _, current, path = heapq.heappop(open_set)

        if current == goal:
            # 计算路径的总距离和总拥挤度
            total_distance = sum(G[path[i]][path[i + 1]]['distance'] for i in range(len(path) - 1))
            total_congestion = sum(heuristic(G, path[i], path[i + 1]) for i in range(len(path) - 1))
            return path, total_distance, total_congestion

        for neighbor in G.neighbors(current):
            if neighbor not in path:
                new_cost = nx.dijkstra_path_length(G, start, current, weight='distance') + heuristic(G, neighbor, goal)
                new_path = path + [neighbor]
                heapq.heappush(open_set, (new_cost, neighbor, new_path))


def visualize_path(G, path):
    """
    可视化路径，包括每个节点和边的完整信息。
    """
    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", alpha=0.8)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{d['distance']}km, {d['congestion']}" for u, v, d in
                                                      G.edges(data=True)}, font_color='red')
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    plt.title("A* Path Visualization")
    plt.show()



G = load_graph_from_json('E:\\PycharmProjects\\地铁乘客路径推荐算法设计\\train.json')
start = 2 # 起点站编号
end = 3  # 终点站编号


path, total_distance, total_congestion = a_star_search(G, start, end)
visualize_path(G, path)


print("实际路径:", path)
print("总距离:", total_distance, "km")
print("总拥挤程度:", total_congestion)
