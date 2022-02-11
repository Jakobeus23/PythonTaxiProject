import networkx as nx
import matplotlib.pyplot as plt

seed=1000           # seed the graph for reproducibility, you should be doing this  
G= nx.gnp_random_graph (200, .06, seed=seed )       # here we create a random binomial graph with 20 nodes and an average (expected) connectivity of 10*.3= 3.
print ( G.nodes() )
print(G.edges())


# matplotlib section
# some properties
print("node degree clustering")
for v in nx.nodes(G):
    print(f"{v} {nx.degree(G, v)} {nx.clustering(G, v)}")

print()
print("the adjacency list")
for line in nx.generate_adjlist(G):
    print(line)

pos = nx.spring_layout(G, seed=seed)  
nx.draw(G, pos = nx.nx_pydot.graphviz_layout(G), \
    node_size=1200, node_color='lightblue', linewidths=0.25, \
    font_size=10, font_weight='bold', with_labels=True)
plt.show()

MXG4=nx.DiGraph(G)
nx.dijkstra_path(MXG4,178,179)     # find the shortest path between two nodes using Djikstra's algorithm; in this case between nodes 23 and 187.




