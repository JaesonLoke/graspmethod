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

	instances.append("./Instances/frb30-15-1.clq")
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


if __name__ == '__main__':
	main()