import networkx as nx
import matplotlib.pyplot as plt
from numpy import savetxt, array
from scipy.sparse import load_npz
from WrangleData import papers

Adjacency = load_npz("Adjacency.npz")

print("file loaded")

# plotting the graph did not yield useful results
Graph = nx.from_scipy_sparse_array(Adjacency.transpose(), create_using=nx.DiGraph) # makes a directed graph. This creates a directed edge i → j whenever Adjacency[i, j] != 0.
# e take the transpose of the matrix because we want arrows to point from cited articles to the articles that cite them. Adjacency[i, j] = 1 when i cites j so we want j → i.

for i, name in enumerate(papers): # set the node labels to the paper API paths
    Graph.nodes[i]["label"] = name

'''# Graph the Adjacecny matrix

plt.figure(figsize=(6,6))
plt.imshow(Adjacency, cmap="Greys", interpolation="none")
plt.title("Adjacency Matrix Structure")
plt.xlabel("Node index")
plt.ylabel("Node index")''' # this is for a dense matrix

# plot sparse matrix structure
plt.figure(figsize=(6,6))
plt.title("Adjacency Matrix Structure")
plt.ylabel("Paper index")
plt.xlabel("Citation index")
plt.spy(Adjacency, markersize=0.1)
plt.title("Citation Adjacency (Sparsity Pattern)")

# plot the subgraph of the top 20 papers by their degrees (number of branches)

# compute degrees
plt.figure(figsize=(6,6)) # start new figure

degrees = dict(Graph.out_degree()) # since outdegrees outnumber in_degrees so much, this hardly makes a difference

# select top 200 nodes by degree
top20 = sorted(degrees, key=degrees.get, reverse=True)[:20]

# induced subgraph
G_sub = Graph.subgraph(top20).copy()

labels = nx.get_node_attributes(G_sub, "label") # labels

pos = nx.circular_layout(G_sub)
nx.draw(G_sub, pos, labels=labels, node_size=50, edge_color="gray", font_size=8, with_labels=True)
plt.axis('equal') # ensures a circular layout looks like a circle


openAlexIDs = [labels[key] for key in labels.keys()]
from pyalex import Works
savetxt("20 most referenced papers in network.txt", array([openAlexIDs,[Works()[openAlexIDs[i]]["title"] for i in range(20)]],dtype=str),  fmt="%s", encoding="utf-8", delimiter=',')

plt.show()