#!/usr/bin/python
import time
import sys
import grasp

def readFile(filename):
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

def main():
	instances = []

	for i in range(1, 11):
		instances.append(f"./Instances/InstancesCliqueSet/Graph-{i}.txt")

	'''
	instances.append("./Instances/frb30-15-2.clq")
	instances.append("./Instances/frb30-15-3.clq")
	instances.append("./Instances/frb30-15-4.clq")
	instances.append("./Instances/frb30-15-5.clq")
	
	instances.append("./Instances/frb45-21-1.clq")
	instances.append("./Instances/frb45-21-2.clq")
	instances.append("./Instances/frb45-21-3.clq")
	instances.append("./Instances/frb45-21-4.clq")
	instances.append("./Instances/frb45-21-5.clq")
	'''
	
	for instance in instances:
		vertices, edges = readFile(instance)

		graph = grasp.createMatrixGraph(vertices, edges)
		graph = grasp.getGraphComplement(graph)
		edges = grasp.getComplementEdges(graph)

		begin = time.time()
		
		clique = grasp.grasp(5, vertices, edges)
		
		end = time.time()
		excTime = end - begin

		file = open("./Output/InstancesCliqueSet - Output3/" + instance.replace("./Instances/InstancesCliqueSet/", "")
                    .replace(".clq", "") + ".txt", "w")
		file.write("FILE: " + instance.replace("./Instances/", "") + "\n")
		file.write("MAX CLIQUE: " + str(len(clique)) + "\n")
		file.write("EXECUTED TIME: " + str(excTime) + "s" + "\n")

		file.write("Clique vertices: ", clique)

		print("Maximum clique: " + str(len(clique)))
		print("Clique vertices: ", clique)
		print("Executed in: " + str(excTime) + " secs")

if __name__ == '__main__':
	main()