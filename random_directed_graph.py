"""

ANALYZING A RANDOM DIRECTED GRAPH

Creates a random directed graph given a certain probability.
Plots a log/log normalized distribution of the graph.

Online link using codeskulptor: http://www.codeskulptor.org/#user47_A442WuiJpj_18.py

"""
#!/bin/python3

import math
import random
import module1_graph as module_1
import matplotlib.pyplot as plt

def make_random_directed_graph(num_nodes, probability):
  """ Takes the number of nodes and a probability of an edge between nodes and creates a complete directed graph based on the probability.
  """
  if num_nodes <= 0:
    return {}
  graph = {}
  for node in range(num_nodes):
    nodes = []
    for j in range(num_nodes):
      a = random.random()
      if a < probability and node != j:
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


def plot_log_graph(size, graph):
  """ Function that computes the log distribution of a graph by plotting a log of graph of keys against the log of values of a given graph.
  Returns the points to be plotted.
  """
  plotX = []
  plotY = []
  for degree, value in graph.items():
    if degree != 0:
      plotX.append(math.log(degree))
      plotY.append(math.log(value))
  return plotX, plotY


def draw_plot(plotX, plotY, xLabel, yLabel, plotName, title, subtitle=""):
  """ Draws the plot figure given the x and y values, and the x and y 
  axis labels and the plot title.
  """
  plt.figure(figsize=[7.4,5.8], facecolor="#e8e8e8")
  plt.figtext(0.2, 0.945, s=title, fontsize='large')
  plt.figtext(0.35, 0.9, s=subtitle, fontsize='large')
  plt.xlabel(xLabel, fontsize="medium")
  plt.ylabel(yLabel, fontsize="medium")
  plt.scatter(plotX, plotY, c="#8116de")
  plt.savefig(plotName + ".png")
  plt.close()


def plot_random_graph(num_nodes, probability, plot_count, xLabel, yLabel, plotName, title, subtitle=""):
  """ Given the number of nodes and probability, plot a directed random
  graph.
  """
  # Create the random er graph
  random_directed_graph = make_random_directed_graph(num_nodes, probability)

  # Compute the unnormalized_distribution
  unnormalized_distr = module_1.in_degree_distribution(random_directed_graph)

  # Compute the normalized distribution - values normalized to a sum of 1.
  nodes = len(random_directed_graph)
  normalized_distr = normalize_distribution(unnormalized_distr, nodes)

  # Compute the log log values.
  plotX, plotY = plot_log_graph(plot_count, normalized_distr)

  # Draw the plot of the log log values of the graph.
  draw_plot(plotX, plotY, xLabel, yLabel, plotName, title, subtitle)



if __name__ == "__main__":
  # # Uncomment the graphs to create the graphs.

  # # Graph 1 - 50 nodes, 0.8, 40 values
  # plotName = "DRGraph_100Nodes_0.8Prob"
  # title = "Normalized Distribution of Random Directed Graph"
  # subtitle = "Nodes=100, Probability=0.8"
  # yLabel = "In-degrees Distribution (log)"
  # xLabel = "Degrees (log)"
  # plot_random_graph(100, 0.8, 50, xLabel, yLabel, plotName, title, subtitle)

  # # Graph 2 - 500 nodes, 0.8, 50
  # plotName = "DRGraph_500Nodes_0.8Prob"
  # title = "Normalized Distribution of Random Directed Graph"
  # subtitle = "Nodes=500, Probability=0.8"
  # yLabel = "In-degrees Distribution (log)"
  # xLabel = "Degrees (log)"
  # plot_random_graph(500, 0.8, 50, xLabel, yLabel, plotName, title, subtitle)

  # # Graph 3 - 1000 nodes, 0.8, 50
  # plotName = "DRGraph_1000Nodes_0.8Prob"
  # title = "Normalized Distribution of Random Directed Graph"
  # subtitle = "Nodes=1000, Probability=0.8"
  # yLabel = "In-degrees Distribution (log)"
  # xLabel = "Degrees (log)"
  # plot_random_graph(1000, 0.8, 50, xLabel, yLabel, plotName, title, subtitle)

  # # Graph 4 - 5000 nodes, 0.8, 50
  # plotName = "DRGraph_5000Nodes_0.8Prob"
  # title = "Normalized Distribution of Random Directed Graph"
  # subtitle = "Nodes=5000, Probability=0.8"
  # yLabel = "In-degrees Distribution (log)"
  # xLabel = "Degrees (log)"
  # plot_random_graph(5000, 0.8, 50, xLabel, yLabel, plotName, title, subtitle)

  # # Graph 5 - 1000 nodes, 0.5, 50
  # plotName = "DRGraph_1000Nodes_1.0Prob"
  # title = "Normalized Distribution of Random Directed Graph"
  # subtitle = "Nodes=1000, Probability=0.5"
  # yLabel = "In-degrees Distribution (log)"
  # xLabel = "Degrees (log)"
  # plot_random_graph(1000, 0.5, 50, xLabel, yLabel, plotName, title, subtitle)

