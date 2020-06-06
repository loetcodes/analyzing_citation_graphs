"""
Week 2: Assignment - Question 1

Loads citation data and maps it as a graph(physics citation graph).
Plots the log/log distribution of the normalized distribution of the graph.

Desktop Python version.
Windows cmd call: py - 3.8

Online version: http://www.codeskulptor.org/#user47_EfijJINTuy_16.py

"""
#!/bin/python3

# import math
import urllib.request
import matplotlib.pyplot as plt
import module1_graph as module_1


# Citation url
CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"


def load_graph(graph_url):
    """ Function that loads a graph given the URL for a text representation of the graph.
    Returns a dictionary that models a graph.
    """
    graph_lines = []
    # Open and process the url
    with urllib.request.urlopen(graph_url) as response:
        graph_text = response.read().decode()
        graph_lines = graph_text.split('\n')
        graph_lines = graph_lines[:-1]

    # Create the graph.
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(" ")
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1:-1]:
            answer_graph[node].add(int(neighbor))
    return answer_graph


def normalize_distribution(graph, nodes):
    """ Function that computes the normalized distribution of a graph given a
    graph of in-degrees distribution.
    """
    result_graph = {}
    for key, value in graph.items():
        result_graph[key] = value / nodes
    return result_graph


def get_xy_values(graph_dict):
    """ Function that computes the x and y values to be plotted.
    """
    plot_x, plot_y = [], []
    for degree, value in graph_dict.items():
        if degree != 0:
            plot_x.append(degree)
            plot_y.append(value)
    return plot_x, plot_y


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



if __name__ == "__main__":
    # Loads and creates the citation graph.
    citation_graph = load_graph(CITATION_URL)

    # Compute the unnormalized_distribution
    unnormalized_distr = module_1.in_degree_distribution(citation_graph)

    # Compute the normalized distribution - values normalized to sum of 1.
    num_nodes = len(citation_graph)
    normalized_distr = normalize_distribution(unnormalized_distr, num_nodes)

    # Compute the values and then plot the log/log of the normalized distribution.
    VALUES = sorted(normalized_distr.items())
    X, Y = zip(*VALUES)

    # Draw the plot.
    PLOT_NAME = "Physics_Citation_Graph_Distribution"
    TITLE = "Normalized Distribution of a Physics Citation graph"
    SUBTITLE = "Nodes=" + str(num_nodes)
    LABEL_Y = "In-degrees Distribution (log)"
    LABEL_X = "Degrees (log)"
    PLOT_INFO = {
        "plot_name": PLOT_NAME,
        "title" : TITLE,
        "subtitle" : SUBTITLE,
        "label_x" : LABEL_X,
        "label_y" : LABEL_Y,
        "x" : X,
        "y" : Y
    }
    draw_plot(PLOT_INFO, "log", "#d92b54", (1e0, 1e4), (1e-5, 1e0))
    # draw_plot(X, Y, LABEL_X, LABEL_Y, PLOT_NAME, TITLE, SUBTITLE, "log", "#d92b54",
    #           (1e0, 1e4), (1e-5, 1e0))
