import networkx as nx
import json
import time


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


def find_shortest_path(G, start, end):
    """
    使用Dijkstra算法找到两个站点之间的最短路径。
    """
    path = nx.dijkstra_path(G, source=start, target=end, weight='distance')
    path_length = nx.dijkstra_path_length(G, source=start, target=end, weight='distance')
    return path, path_length


def main():
    file_path = 'train.json'
    G = load_graph_from_json(file_path)

    start = 2  # 起点站编号
    end = 3  # 终点站编号

    if start not in G.nodes() or end not in G.nodes():
        print("指定的站点不在图中，请检查站点编号")
        return

    start_time = time.time()
    path, path_length = find_shortest_path(G, start, end)
    end_time = time.time()

    # 输出结果
    print("最短路径:", path)
    print("路径长度:", path_length)
    print("执行时间:", end_time - start_time, "秒")


if __name__ == "__main__":
    main()
