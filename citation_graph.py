"""

ANALYZING A PHYSICS CITATION GRAPH

Loads citation data and maps it as a graph(physics citation graph).
Plots the log/log distribution of the normalized distribution of the graph using matplotlib.

Desktop Python version.
Windows cmd call: py - 3.8

Online version: http://www.codeskulptor.org/#user47_EfijJINTuy_16.py

"""
#!/bin/python3

import math
import urllib.request
import module1_graph as module_1
import matplotlib.pyplot as plt


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


def draw_plot(plotX, plotY, xLabel, yLabel, plotName, title="", subtitle="", plotType="log", pointColor="#8116de", xLimit="", yLimit=""):
  """ Draws the plot figure given the x and y values, and the x and y 
  axis labels and the plot title.
  """
  plt.figure(figsize=[7.4,5.8], facecolor="#e8e8e8")
  plt.figtext(0.2, 0.945, s=title, fontsize='large')
  plt.figtext(0.4, 0.9, s=subtitle, fontsize='large')
  plt.xscale(plotType)
  plt.yscale(plotType)
  if xLimit != "":
    plt.xlim(xLimit[0], xLimit[1])
  if yLimit != "":
    plt.ylim(yLimit[0], yLimit[1])
  plt.xlabel(xLabel, fontsize="medium")
  plt.ylabel(yLabel, fontsize="medium")
  plt.scatter(plotX, plotY, c=pointColor)
  plt.savefig(plotName + ".png")
  plt.close()



if __name__ == "__main__":
  # Loads and creates the citation graph.
  citation_graph = load_graph(CITATION_URL)

  # Compute the unnormalized_distribution
  unnormalized_distr = module_1.in_degree_distribution(citation_graph)

  # Compute the normalized distribution - values normalized to sum of 1.
  nodes = len(citation_graph)
  normalized_distr = normalize_distribution(unnormalized_distr, nodes)

  # Compute the values and then plot the log/log of the normalized distribution.
  values = sorted(normalized_distr.items())
  plotX, plotY = zip(*values)

  # Draw the plot.
  plotName = "Physics_Citation_Graph_Distribution"
  title = "Normalized Distribution of a Physics Citation graph"
  subtitle = "Nodes=" + str(nodes)
  yLabel = "In-degrees Distribution (log)"
  xLabel = "Degrees (log)"
  draw_plot(plotX, plotY, xLabel, yLabel, plotName, title, subtitle, "log", "#d92b54", (1e0, 1e4), (1e-5, 1e0))