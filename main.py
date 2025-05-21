import json, networkx as nx
import matplotlib.pyplot as plt

with open("network-graph.json") as f:
    graph_data = json.load(f)

G = nx.Graph()
for node, neighbors in graph_data.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

plt.figure(figsize=(20, 15))
nx.draw(G, with_labels=True, node_size=300, font_size=6)
plt.show()