import networkx as nx
import matplotlib.pyplot as plt
import random
import json

# 创建一个随机的无向图
G = nx.Graph()

# 添加10个站点
num_stations = 10
stations = range(1, num_stations + 1)
G.add_nodes_from(stations)


for _ in range(15):
    u, v = random.sample(stations, 2)
    if not G.has_edge(u, v):
        distance = random.randint(1, 10)  # 距离1-10之间
        congestion = random.choice(['Low', 'Medium', 'High'])  # 拥挤度
        G.add_edge(u, v, distance=distance, congestion=congestion)

# 将图的数据保存到文件中
graph_data = {
    "edges": [
        {
            "from": u,
            "to": v,
            "distance": G[u][v]['distance'],
            "congestion": G[u][v]['congestion']
        }
        for u, v in G.edges
    ]
}


file_path = '/train.json'
with open(file_path, 'w') as file:
    json.dump(graph_data, file)


pos = nx.spring_layout(G)
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", alpha=0.8)
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={(u, v): f"{G[u][v]['distance']}km, {G[u][v]['congestion']}" for u, v in G.edges},
    font_color='red'
)
plt.title("Random Subway Network")
plt.show()



