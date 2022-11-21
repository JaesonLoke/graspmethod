from itertools import combinations
import networkx as nx
import time


def read_file(filename):
    file = open(filename, 'r')

    x, y, nVertices, nEdges = [i for i in next(file).split()]

    vertices = []
    for i in range(int(nVertices)):
        vertices.append(i + 1)

    edges = []
    for i in range(int(nEdges)):
        z, x, y = [j for j in next(file).split()]
        edges.append([int(x), int(y)])

    return [vertices, edges]


def k_cliques(graph, size_k):
    # 2-cliques
    cliques = [{i, j} for i, j in graph.edges() if i != j]
    k = 2

    while cliques:
        # result
        yield k, cliques
        if k == size_k:
            break

        # merge k-cliques into (k+1)-cliques
        cliques_1 = set()
        for u, v in combinations(cliques, 2):
            w = u ^ v
            if len(w) == 2 and graph.has_edge(*w):
                cliques_1.add(tuple(u | w))

        # remove duplicates
        cliques = list(map(set, cliques_1))

        if len(cliques) == 0:
            print('No %d-cliques found.' % size_k)
        k += 1


def print_cliques(graph, size_k):
    for k, cliques in k_cliques(graph, size_k):
        if k == size_k:
            return '%d-cliques = %d, %s.' % (k, len(cliques), cliques)


if __name__ == '__main__':

    size_k = 8
    instances = []

    for i in range(1, 11):
        instances.append(f"./InstancesCliqueSet/Graph-{i}.txt")

    for instance in instances:
        nodes, edges = read_file(instance)

        graph = nx.Graph()
        graph.add_nodes_from(range(len(nodes)))
        for i in range(len(edges)):
            graph.add_edge(edges[i][0], edges[i][1])

        begin = time.time()
        result = print_cliques(graph, size_k)
        print(result)
        end = time.time()
        excTime = end - begin
        print("Executed in: " + str(excTime) + " secs")

        file = open("./InstancesCliqueSetC - Output/" + instance.replace("./InstancesCliqueSet/", "")
                    .replace(".clq", "") + ".txt", "w")
        file.write("FILE: " + instance.replace("./Instances/", "") + "\n")
        file.write(str(result) + "\n")
        file.write("EXECUTED TIME: " + str(excTime) + "\n")
