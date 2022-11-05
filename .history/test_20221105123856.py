#!/usr/bin/python
import time
import sys
import grasp

def readFile(filename):
	


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