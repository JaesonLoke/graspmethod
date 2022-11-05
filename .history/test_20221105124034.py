#!/usr/bin/python
import time
import sys
import grasp

	


def main():
	instances = []

	instances.append("./Instances/frb30-15-1.clq")
    
	for instance in instances:
        
        file = open(instance, 'r')

	    x, y, nVertices, nEdges = [i for i in next(file).split()]

	    print("X: " + x)
	    print("y: ", y)
	    print("nV: " + nVertices)


if __name__ == '__main__':
	main()