"""
Python code that creates dictionaries corresponding to simple
examples of graphs.

The program also computes the degree distributions of the
in-degrees for nodes in these graph.

"""

EX_GRAPH0 = {
    0 : set([1 ,2]),
    1 : set([]),
    2 : set([])
}

EX_GRAPH1 = {
    0 : set([1,4,5]),
    1 : set([2,6]),
    2 : set([3]),
    3 : set([0]),
    4 : set([1]),
    5 : set([2]),
    6 : set([])
}

EX_GRAPH2 = {
    0 : set([1,4,5]),
    1 : set([2,6]),
    2 : set([3,7]),
    3 : set([7]),
    4 : set([1]),
    5 : set([2]),
    6 : set([]),
    7 : set([3]),
    8 : set([1,2]),
    9 : set([0,3,4,5,6,7])
}


def make_complete_graph(num_nodes):
    """ Takes the number of nodes and returns a dictionary
    corresponding to a complete directed graph with the specified
    number of nodes.
    A complete graph contains all possible edges subject to 
    the restriction that self loops are not allowed.
    Nodes of the graph are numbered 0 to num_nodes - 1 when
    num_nodes is positive.
    """
    if num_nodes <= 0:
        return {}
    graph = {}
    for node in range(num_nodes):
        nodes = [j for j in range(num_nodes) if j != node]
        graph[node] = set(nodes)
    return graph


def compute_in_degrees(digraph):
    """ Takes a digraph(represented as a dictionary) and computes the
    in-degrees for the nodes in the graph. The function returns a dictionary
    with the same set of keys(nodes) as digraph whose corresponding values are
    the number of edges whose head matches a particular node.
    """
    in_degrees = {}
    for node in digraph:
        in_degrees[node] = in_degrees.get(node, 0)
        for tail in digraph[node]:
            in_degrees[tail] = in_degrees.get(tail, 0) + 1 
    return in_degrees
        


def in_degree_distribution(digraph):
    """ Takes a digraph(represented as a dictionary) and computes the unnormalized distribution of the in-degrees of the graph.
    The function returns a dictionary whose keys correspond to the in-degrees of nodes in the graph. 
    The value associated with each particular in-degree is the number of nodes with that in-degree.
    In-degrees with no corresponding nodes in the graph are not included in the
    dictionary.
    """
    degree_dist = {}
    in_degrees = compute_in_degrees(digraph)
    for degree in in_degrees.values():
        degree_dist[degree] = degree_dist.get(degree, 0) + 1
    return degree_dist
