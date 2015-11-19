import pygraphviz as pgv
import networkx as nx
import matplotlib.pylab as plt

def Iris_network(ant, data):
    #G = nx.watts_strogatz_graph(100,3,0.6)
    #G = nx.cubical_graph()
    G = nx.Graph() #無向グラフ

    tmp1 = []
    tmp2 = []
    tmp3 = []
    for i in range(len(data)):
        if data[i][4] == 'setosa':
            tmp1.append(str(i))
        elif data[i][4] == 'versicolor':
            tmp2.append(str(i))
        elif data[i][4] == 'virginica':
            tmp3.append(str(i))

    for i in range(len(data)):
        if len(ant[i].parent) == 0 : pass
        else:
            dest = ant[i].parent[0]
            #G.add_edge(str(ant[i].data), str(ant[dest].data))
            G.add_edge(str(ant[i].Id), str(ant[dest].Id))

    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(G, pos, nodelist=tmp1, node_size=30, node_color="r")
    nx.draw_networkx_nodes(G, pos, nodelist=tmp2, node_size=30, node_color="w")
    nx.draw_networkx_nodes(G, pos, nodelist=tmp3, node_size=30, node_color="w")
    nx.draw_networkx_edges(G, pos, width=1)
    #nx.draw_networkx_labels(G, pos, font_size=10, font_color="b")
    plt.xticks([])
    plt.yticks([])
    plt.show()

def corner_network(ant, data, fname):
    #G = nx.cubical_graph()
    G = nx.Graph() #無向グラフ
    tmp1 = []
    tmp2 = []
    tmp3 = []
    tmp4 = []
    #for i in range(len(data)):
        #if data[i][2] == 'lu':
            #tmp1.append(str(i))
        #elif data[i][2] == 'ld':
            #tmp2.append(str(i))
        #elif data[i][2] == 'ru':
            #tmp3.append(str(i))
        #elif data[i][2] == 'rd' :
            #tmp4.append(str(i))

    for i in range(len(data)):
        if len(ant[i].parent) == 0 : pass
        else :
            dest = ant[i].parent[0]
            G.add_edge(str(data[i]), str(data[dest]))

    pos = nx.spring_layout(G)
    
    nx.draw_networkx_nodes(G, pos, nodelist=tmp1, node_size=30, node_color="r")
    #nx.draw_networkx_nodes(G, pos, nodelist=tmp2, node_size=30, node_color="b")
    #nx.draw_networkx_nodes(G, pos, nodelist=tmp3, node_size=30, node_color="g")
    #nx.draw_networkx_nodes(G, pos, nodelist=tmp4, node_size=30, node_color="y")
    #nx.draw_networkx_nodes(G, pos, node_size=20, node_color="blue")
    nx.draw_networkx_edges(G, pos, width=1)

    A = nx.to_agraph(G)
    A.layout()
    A.draw(fname+".png")
    #plt.xticks([])
    #plt.yticks([])
    #plt.show()
