import random
import math
import karger_min_cut.graph_loader as loader


def replace(arr, a, b):
	for idx in range(0, len(arr)):
		if arr[idx] == a:
			arr[idx] = b


def calc_min_cut(graph):
	while len(graph) > 2:
		node_a = random.choice(list(graph))
		edges = graph[node_a]
		node_b = random.choice(edges)

		for node in graph:
			replace(graph[node], node_a, node_b)
		# merge nodes
		merged = graph[node_a] + graph[node_b]
		graph[node_b] = merged

		# edge will now contain a link to itself, remove this
		if (node_b in graph) and (node_b in graph[node_b]):
			graph[node_b] = [x for x in graph[node_b] if x != node_b]
		graph.pop(node_a)

	return len(graph.popitem()[1])


def run(graph_def):
	# Karger has only got a 1/n^2 probability of getting the right answer first time, so we need to run n^2 * log(n) times
	min_cut = 1000
	no_of_nodes = graph_def['nodes']
	iterations = int((no_of_nodes ** 2) * math.log(no_of_nodes))
	print('running for ', iterations, 'iterations')
	for i in range(1, iterations):
		if i % 10 == 0:
			print('\r Completed {0} of {1} iterations. Best cut found so far: {2}'.format(i, iterations, min_cut))
		graph = loader.load_graph(graph_def)
		curr_best_cut = calc_min_cut(graph)
		if curr_best_cut < min_cut:
			min_cut = curr_best_cut
	return min_cut

