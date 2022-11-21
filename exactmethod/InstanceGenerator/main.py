import networkx as nx

if __name__ == '__main__':
    nodes = 25
    # 20/57-30% 20/76-40% 20/95-50% 20/114-60% 20/133-70%
    edges = 250
    filename = "Graph"

    for i in range(1, 16):
        file = open(f"./InstancesNodesSetA/{filename}-{i}.txt", "w")
        file.write(f"p edge {nodes} {edges}" + "\n")

        graph = nx.gnm_random_graph(nodes, edges)
        cliques = [[i + 1, j + 1] for i, j in graph.edges() if i != j]
        for x in range(len(cliques)):
            file.write(f"e {cliques[x][0]} {cliques[x][1]}" + "\n")

        # close file after writing
        file.close()
