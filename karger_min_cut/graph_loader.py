def load_line(graph, line):
	line = line.rstrip()
	tokes = line.split(" ")
	node = tokes[0]
	edges = tokes[1:]
	graph[node] = edges


# represent graph as adjacency list
def load_graph(graph_def):
	graph = {}
	with open(graph_def['file']) as f:
		for line in f:
			load_line(graph, line)
	return graph
