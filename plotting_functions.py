"""

Plotting Functions

Used to plot graph

"""
#!/bin/python3

import matplotlib.pyplot as plt
import module1_graph as module_1


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


def plot_graph(graph_details, plot_details, plot_type="log",
               plot_color="#8116de", xy_limits=("", "")):
    """ Given the graph values, plot the normalized distribution of the graph.
    """
    # Compute the unnormalized_distribution
    unnormalized_distr = module_1.in_degree_distribution(graph_details)

    # Compute the normalized distribution - values normalized to a sum of 1.
    nodes = len(graph_details)
    normalized_distr = normalize_distribution(unnormalized_distr, nodes)

    # Sort the graph and create x and y points.
    values = sorted(normalized_distr.items())
    plot_x_vals, plot_y_vals = zip(*values)

    # Add vals to plot details
    plot_details["x"] = plot_x_vals
    plot_details["y"] = plot_y_vals

    # Draw the plot of the log log values of the graph.
    draw_plot(plot_details, plot_type, plot_color, xy_limits[0], xy_limits[1])


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
    # Graph 1 - 100 nodes, 0.8, 40 values
    PLOT_NAME = "DRGraph_100Nodes_0.8Prob-log"
    TITLE = "Loglog: Normalized Distribution of Random Directed Graph"
    SUBTITLE = "Nodes=100, Probability=0.8"
    LABEL_Y = "In-degrees Distribution (log)"
    LABEL_X = "Degrees (log)"
    PLOT_INFO = store_details(PLOT_NAME, TITLE, SUBTITLE, LABEL_X, LABEL_Y)

    NODES = 100
    RANDOM_GRAPH = module_1.make_complete_graph(NODES)
    plot_graph(RANDOM_GRAPH, PLOT_INFO)
