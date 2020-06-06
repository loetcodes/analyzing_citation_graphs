"""

Week 2: Assignment - Question 2

Generates random directed graphs using the ER algorithm with a slight
modification: For every ordered pair of distinct nodes (i, j), the
modified algorithm adds the directed edge from i to j with probability p.

Online link: http://www.codeskulptor.org/#user47_A442WuiJpj_18.py

"""
#!/bin/python3

# import math
import random
import matplotlib.pyplot as plt
import module1_graph as module_1


def make_random_directed_graph(num_nodes, probability):
    """ Takes the number of nodes and a probability of an edge between
    nodes and creates a complete directed graph based on the probability.
    """
    if num_nodes <= 0:
        return {}
    graph = {}
    for node in range(num_nodes):
        nodes = []
        for j in range(num_nodes):
            val = random.random()
            if val < probability and node != j:
                nodes.append(j)
        graph[node] = set(nodes)
    return graph


def normalize_distribution(graph, nodes):
    """ Function that computes the normalized distribution of a graph given a
        graph of in-degrees distribution.
    """
    result_graph = {}
    for key, value in graph.items():
        result_graph[key] = round(float(value) / nodes, 6)
    return result_graph


def draw_plot(plot_details, plot_type="log", point_color="#8116de", x_limit="", y_limit=""):
    """ Draws the plot figure given the x and y values, and the x and y
    axis labels and the plot title.
    """
    plt.figure(figsize=[7.4, 5.8], facecolor="#e8e8e8")
    plt.figtext(0.2, 0.945, s=plot_details["title"], fontsize='large')
    plt.figtext(0.4, 0.9, s=plot_details["subtitle"], fontsize='large')
    plt.xscale(plot_type)
    plt.yscale(plot_type)
    if x_limit != "":
        plt.xlim(x_limit[0], x_limit[1])
    if y_limit != "":
        plt.ylim(y_limit[0], y_limit[1])
    plt.xlabel(plot_details["label_x"], fontsize="medium")
    plt.ylabel(plot_details["label_y"], fontsize="medium")
    plt.scatter(plot_details["x"], plot_details["y"], c=point_color)
    plt.savefig(plot_details["plot_name"] + ".png")
    plt.close()


def plot_graph(nodes_and_probability, plot_details, plot_type="log",
               plot_color="#8116de", x_limit="", y_limit=""):
    """ Given the number of nodes and probability, plot a directed random
    graph.
    """
    # Create the random er graph
    num_nodes = nodes_and_probability[0]
    probability = nodes_and_probability[1]
    random_directed_graph = make_random_directed_graph(num_nodes, probability)

    # Compute the unnormalized_distribution
    unnormalized_distr = module_1.in_degree_distribution(random_directed_graph)

    # Compute the normalized distribution - values normalized to a sum of 1.
    nodes = len(random_directed_graph)
    normalized_distr = normalize_distribution(unnormalized_distr, nodes)

    # Sort the graph and create x and y points.
    values = sorted(normalized_distr.items())
    plot_x_vals, plot_y_vals = zip(*values)

    # Add vals to plot details
    plot_details["x"] = plot_x_vals
    plot_details["y"] = plot_y_vals

    # Draw the plot of the log log values of the graph.
    draw_plot(plot_details, plot_type, plot_color, x_limit, y_limit)


def store_details(name, title, subtitle, x_label, y_label):
    """ Returns a dictionary with properties of the plot set.
    """
    details = {}
    details["plot_name"] = name
    details["title"] = title
    details["subtitle"] = subtitle
    details["label_x"] = x_label
    details["label_y"] = y_label
    return details


if __name__ == "__main__":
    print("Creating graphs")
    # # Graph 1 - 100 nodes, 0.8, 40 values
    # PLOT_NAME = "DRGraph_100Nodes_0.8Prob-log"
    # TITLE = "Loglog: Normalized Distribution of Random Directed Graph"
    # SUBTITLE = "Nodes=100, Probability=0.8"
    # LABEL_Y = "In-degrees Distribution (log)"
    # LABEL_X = "Degrees (log)"
    # PLOT_INFO = store_details(PLOT_NAME, TITLE, SUBTITLE, LABEL_Y, LABEL_X)
    # NODES_PROB = (100, 0.8)
    # plot_graph(NODES_PROB, PLOT_INFO)
    # # plot_graph(100, 0.8, 500, xLabel, yLabel, plotName, title, subtitle)

    # # Graph 2 - 500 nodes, 0.8
    # PLOT_NAME = "DRGraph_500Nodes_0.8Prob-log"
    # TITLE = "Loglog: Normalized Distribution of Random Directed Graph"
    # SUBTITLE = "Nodes=500, Probability=0.8"
    # LABEL_Y = "In-degrees Distribution (log)"
    # LABEL_X = "Degrees (log)"
    # PLOT_INFO = store_details(PLOT_NAME, TITLE, SUBTITLE, LABEL_Y, LABEL_X)
    # NODES_PROB = (500, 0.8)
    # plot_graph(NODES_PROB, PLOT_INFO)

    # # Graph 3 - 1000 nodes, 0.8
    # PLOT_NAME = "DRGraph_1000Nodes_0.8Prob-log"
    # TITLE = "Loglog: Normalized Distribution of Random Directed Graph"
    # SUBTITLE = "Nodes=1000, Probability=0.8"
    # LABEL_Y = "In-degrees Distribution (log)"
    # LABEL_X = "Degrees (log)"
    # PLOT_INFO = store_details(PLOT_NAME, TITLE, SUBTITLE, LABEL_Y, LABEL_X)
    # NODES_PROB = (1000, 0.8)
    # plot_graph(NODES_PROB, PLOT_INFO)

    # # Graph 3.1 - 1000 nodes, 0.8
    # PLOT_NAME = "DRGraph_1000Nodes_0.8Prob-Standard"
    # TITLE = "Standard: Normalized Distribution of Random Directed Graph"
    # SUBTITLE = "Nodes=1000, Probability=0.8"
    # LABEL_Y = "In-degrees Distribution"
    # LABEL_X = "Degrees"
    # PLOT_INFO = store_details(PLOT_NAME, TITLE, SUBTITLE, LABEL_Y, LABEL_X)
    # NODES_PROB = (1000, 0.8)
    # plot_graph(NODES_PROB, PLOT_INFO, plot_type="linear", plot_color="#d69a00")

    # # Graph 4 - 5000 nodes, 0.8
    # PLOT_NAME = "DRGraph_5000Nodes_0.8Prob-log"
    # TITLE = "Loglog: Normalized Distribution of Random Directed Graph"
    # SUBTITLE = "Nodes=5000, Probability=0.8"
    # LABEL_Y = "In-degrees Distribution (log)"
    # LABEL_X = "Degrees (log)"
    # PLOT_INFO = store_details(PLOT_NAME, TITLE, SUBTITLE, LABEL_Y, LABEL_X)
    # NODES_PROB = (5000, 0.8)
    # plot_graph(NODES_PROB, PLOT_INFO)

    # # Graph 4.1 - 5000 nodes, 0.8
    # PLOT_NAME = "DRGraph_5000Nodes_0.8Prob-Standard"
    # TITLE = "Standard: Normalized Distribution of Random Directed Graph"
    # SUBTITLE = "Nodes=5000, Probability=0.8"
    # LABEL_Y = "In-degrees Distribution"
    # LABEL_X = "Degrees"
    # PLOT_INFO = store_details(PLOT_NAME, TITLE, SUBTITLE, LABEL_Y, LABEL_X)
    # NODES_PROB = (5000, 0.8)
    # plot_graph(NODES_PROB, PLOT_INFO, plot_type="linear", plot_color="#d69a00")

    # # Graph 5 - 5000 nodes, 0.5
    # PLOT_NAME = "DRGraph_5000Nodes_0.5Prob-log"
    # TITLE = "Loglog: Normalized Distribution of Random Directed Graph"
    # SUBTITLE = "Nodes=5000, Probability=0.5"
    # LABEL_Y = "In-degrees Distribution (log)"
    # LABEL_X = "Degrees (log)"
    # PLOT_INFO = store_details(PLOT_NAME, TITLE, SUBTITLE, LABEL_Y, LABEL_X)
    # NODES_PROB = (5000, 0.5)
    # plot_graph(NODES_PROB, PLOT_INFO)

    # # Graph 5.1 - 5000 nodes, 0.5
    # PLOT_NAME = "DRGraph_5000Nodes_0.5Prob-Standard"
    # TITLE = "Standard: Normalized Distribution of Random Directed Graph"
    # SUBTITLE = "Nodes=5000, Probability=0.5"
    # LABEL_Y = "In-degrees Distribution"
    # LABEL_X = "Degrees"
    # PLOT_INFO = store_details(PLOT_NAME, TITLE, SUBTITLE, LABEL_Y, LABEL_X)
    # NODES_PROB = (5000, 0.5)
    # plot_graph(NODES_PROB, PLOT_INFO, plot_type="linear", plot_color="#d69a00")
