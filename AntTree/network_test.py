import networkx as nx
import matplotlib.pylab as plt

G = nx.Graph() #無向グラフ
#G = nx.DiGraph() #有向グラフ
#G.add_node("a")
G.add_node(1)
#G.add_nodes_from(["b", "c"])
#G.add_nodes_from([2, 3])
#G.add_edge("a", "c", weight=3)
#G.add_edge("b", "c", weight=5)
G.add_edge(1, 2, weight=3)
G.add_edge(2, 3, weight=5)

pos = nx.spring_layout(G)
#edge_labels = {("a","c"):3, ("b","c"):5}
edge_labels = {(1,3):3, (2,3):5}

nx.draw_networkx_nodes(G, pos, node_size=200, node_color="blue")
nx.draw_networkx_edges(G, pos, width=1)
#nx.draw_networkx_edge_labels(G, pos, edge_labels)
nx.draw_networkx_labels(G, pos, font_size=16, font_color="r")

plt.xticks([])
plt.yticks([])
plt.show()
