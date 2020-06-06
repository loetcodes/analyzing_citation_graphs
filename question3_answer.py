"""

Week 2: Assignment - Question 3

Consider a different process for generating synthetic directed graphs.
In this process, a random directed graph is generated iteratively,
where in each iteration a new node is created, added to the graph, and connected
to a subset of the existing nodes. This subset is chosen based on the in-degrees
of the existing nodes.
More formally, to generate a random directed graph, the user must specify two
parameters: n, which is the final number of nodes and m (where m <= n), which
is the number of existing nodes to which a new node is connected during each
iteration. Notice that m is fixed throughout the procedure.

Online link: http://www.codeskulptor.org/#user47_A442WuiJpj_18.py

"""
#!/bin/python3

# import math
import random
import module1_graph as module_1
import plotting_functions as plot_module


class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm.    
    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are in the same proportion
    as the desired probabilities.
    Uses random.choice() to select a node number from this list for each trial.
    """
    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a complete graph with
        num_nodes nodes. Note the initial list of node numbers has num_nodes
        copies of each node number.
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]

    def run_trial(self, num_nodes):
        """
        Conduct num_nodes trials by applying random.choice() to the list of
        node numbers. Updates the list of node numbers so that the number
        of instances of each node number is in the same ratio as the desired
        probabilities.
        Returns a set of nodes.
        """
        # Compute neighbors for new node
        new_neighbors = set()
        for _ in range(num_nodes):
            new_neighbors.add(random.choice(self._node_numbers))

        # Update the list of node numbers so each node numbers appears in correct
        # ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_neighbors))

        # Update number of nodes
        self._num_nodes += 1
        return new_neighbors


def make_dpa_graphs(n, m):
    """ DPA Algorithm creates a complete directed graph on m nodes.
    Then adds n - m nodes, where each new node is connected to m
    nodes randomly chosen from the set of existing nodes.
    """
    # Create the complete graph with m nodes
    graph = module_1.make_complete_graph(m)

    # Compute new nodes, add (n - m) nodes
    trial = DPATrial(m)
    for idx in range(m, n):
        # Get new nodes, Add the new node and set of in-degrees nodes to graph
        total_in_degrees = trial.run_trial(m)
        graph[idx] = total_in_degrees

    return graph



if __name__ == "__main__":
    # Create graphs
    print("Creating plots of graphs")

    # ---------------------------------------------------------------
    # Graph 1 - 20000N 100M
    # print("Creating Graph:", "DPAGraph_20000N_100M")
    # PLOT_NAME = "DPAGraph_20000N_100M"
    # TITLE = "Loglog: Normalized Distribution of DPA Graph"
    # SUBTITLE = "Total Nodes=20000 Existing Nodes=100"
    # LABEL_Y = "In-degrees Distribution (log)"
    # LABEL_X = "Degrees (log)"
    # PLOT_INFO = plot_module.store_details(PLOT_NAME, TITLE, SUBTITLE,
    #                                       LABEL_X, LABEL_Y)
    # TOTAL_NODES = 20000
    # EXISTING_NODES = 100
    # DPA_GRAPH = make_dpa_graphs(TOTAL_NODES, EXISTING_NODES)
    # plot_module.plot_graph(DPA_GRAPH, PLOT_INFO, plot_color="#f7d80c",
    #                        xy_limits=((1e0, 1e4), (1e-5, 1e0)))


    # ---------------------------------------------------------------
    # Graph 1b - 20000N 50M
    # print("Creating Graph:", "DPAGraph_20000N_50M")
    # PLOT_NAME = "DPAGraph_20000N_50M"
    # TITLE = "Loglog: Normalized Distribution of DPA Graph"
    # SUBTITLE = "Total Nodes=20000 Existing Nodes=50"
    # LABEL_Y = "In-degrees Distribution (log)"
    # LABEL_X = "Degrees (log)"
    # PLOT_INFO = plot_module.store_details(PLOT_NAME, TITLE, SUBTITLE,
    #                                       LABEL_X, LABEL_Y)
    # TOTAL_NODES = 20000
    # EXISTING_NODES = 50
    # DPA_GRAPH = make_dpa_graphs(TOTAL_NODES, EXISTING_NODES)
    # plot_module.plot_graph(DPA_GRAPH, PLOT_INFO, plot_color="#f7d80c",
    #                        xy_limits=((1e0, 1e4), (1e-5, 1e0)))


    # ---------------------------------------------------------------
    # Graph 1c - 20000N 10M
    # print("Creating Graph:", "DPAGraph_20000N_10M")
    # PLOT_NAME = "DPAGraph_20000N_10M"
    # TITLE = "Loglog: Normalized Distribution of DPA Graph"
    # SUBTITLE = "Total Nodes=20000 Existing Nodes=10"
    # LABEL_Y = "In-degrees Distribution (log)"
    # LABEL_X = "Degrees (log)"
    # PLOT_INFO = plot_module.store_details(PLOT_NAME, TITLE, SUBTITLE,
    #                                       LABEL_X, LABEL_Y)
    # TOTAL_NODES = 20000
    # EXISTING_NODES = 10
    # DPA_GRAPH = make_dpa_graphs(TOTAL_NODES, EXISTING_NODES)
    # plot_module.plot_graph(DPA_GRAPH, PLOT_INFO, plot_color="#f7d80c",
    #                        xy_limits=((1e0, 1e4), (1e-5, 1e0)))


    # ---------------------------------------------------------------
    # Graph 2 - 27770N 10M
    # print("Creating Graph:", "DPAGraph_27770N_10M")
    # PLOT_NAME = "DPAGraph_27770N_10M"
    # TITLE = "Loglog: Normalized Distribution of DPA Graph"
    # SUBTITLE = "Total Nodes=27770 Existing Nodes=10"
    # LABEL_Y = "In-degrees Distribution (log)"
    # LABEL_X = "Degrees (log)"
    # PLOT_INFO = plot_module.store_details(PLOT_NAME, TITLE, SUBTITLE,
    #                                       LABEL_X, LABEL_Y)
    # TOTAL_NODES = 27770
    # EXISTING_NODES = 10
    # DPA_GRAPH = make_dpa_graphs(TOTAL_NODES, EXISTING_NODES)
    # plot_module.plot_graph(DPA_GRAPH, PLOT_INFO, plot_color="#f7d80c",
    #                        xy_limits=((1e0, 1e4), (1e-5, 1e0)))


    # ---------------------------------------------------------------
    # Graph 2b - 27770N 10M
    # print("Creating Graph:", "DPAGraph_27770N_12M")
    # PLOT_NAME = "DPAGraph_27770N_12M"
    # TITLE = "Loglog: Normalized Distribution of DPA Graph"
    # SUBTITLE = "Total_Nodes=27770 Existing_Nodes=12"
    # LABEL_Y = "In-degrees Distribution (log)"
    # LABEL_X = "Degrees (log)"
    # PLOT_INFO = plot_module.store_details(PLOT_NAME, TITLE, SUBTITLE,
    #                                       LABEL_X, LABEL_Y)
    # TOTAL_NODES = 27770
    # EXISTING_NODES = 12
    # DPA_GRAPH = make_dpa_graphs(TOTAL_NODES, EXISTING_NODES)
    # plot_module.plot_graph(DPA_GRAPH, PLOT_INFO, plot_color="#f7d80c",
    #                        xy_limits=((1e0, 1e4), (1e-5, 1e0)))


    # ---------------------------------------------------------------
    # Graph 2b - 27770N 13M
    # print("Creating Graph:", "DPAGraph_27770N_13M")
    # PLOT_NAME = "DPAGraph_27770N_13M"
    # TITLE = "Loglog: Normalized Distribution of DPA Graph"
    # SUBTITLE = "Total_Nodes=27770 Existing_Nodes=13"
    # LABEL_Y = "In-degrees Distribution (log)"
    # LABEL_X = "Degrees (log)"
    # PLOT_INFO = plot_module.store_details(PLOT_NAME, TITLE, SUBTITLE,
    #                                       LABEL_X, LABEL_Y)
    # TOTAL_NODES = 27770
    # EXISTING_NODES = 13
    # DPA_GRAPH = make_dpa_graphs(TOTAL_NODES, EXISTING_NODES)
    # plot_module.plot_graph(DPA_GRAPH, PLOT_INFO, plot_color="#f7d80c",
    #                        xy_limits=((1e0, 1e4), (1e-5, 1e0)))

    # ---------------------------------------------------------------
    # Graph 2c - 27770N 14M
    # print("Creating Graph:", "DPAGraph_27770N_14M")
    # PLOT_NAME = "DPAGraph_27770N_14M"
    # TITLE = "Loglog: Normalized Distribution of DPA Graph"
    # SUBTITLE = "Total_Nodes=27770 Existing_Nodes=14"
    # LABEL_Y = "In-degrees Distribution (log)"
    # LABEL_X = "Degrees (log)"
    # PLOT_INFO = plot_module.store_details(PLOT_NAME, TITLE, SUBTITLE,
    #                                       LABEL_X, LABEL_Y)
    # TOTAL_NODES = 27770
    # EXISTING_NODES = 14
    # DPA_GRAPH = make_dpa_graphs(TOTAL_NODES, EXISTING_NODES)
    # plot_module.plot_graph(DPA_GRAPH, PLOT_INFO, plot_color="#f7d80c",
    #                        xy_limits=((1e0, 1e4), (1e-5, 1e0)))


    # ---------------------------------------------------------------
    # Graph 2d - 27000N 14M
    # print("Creating Graph:", "DPAGraph_27000N_14M")
    # PLOT_NAME = "DPAGraph_27000N_14M"
    # TITLE = "Loglog: Normalized Distribution of DPA Graph"
    # SUBTITLE = "Total_Nodes=27000 Existing_Nodes=14"
    # LABEL_Y = "In-degrees Distribution (log)"
    # LABEL_X = "Degrees (log)"
    # PLOT_INFO = plot_module.store_details(PLOT_NAME, TITLE, SUBTITLE,
    #                                       LABEL_X, LABEL_Y)
    # TOTAL_NODES = 27000
    # EXISTING_NODES = 14
    # DPA_GRAPH = make_dpa_graphs(TOTAL_NODES, EXISTING_NODES)
    # plot_module.plot_graph(DPA_GRAPH, PLOT_INFO, plot_color="#f7d80c",
    #                        xy_limits=((1e0, 1e4), (1e-5, 1e0)))


    # ---------------------------------------------------------------
    # Graph 2e - 27000N 12M
    print("Creating Graph:", "DPAGraph_27000N_12M")
    PLOT_NAME = "DPAGraph_27000N_12M"
    TITLE = "Loglog: Normalized Distribution of DPA Graph"
    SUBTITLE = "Total_Nodes=27000 Existing_Nodes=12"
    LABEL_Y = "In-degrees Distribution (log)"
    LABEL_X = "Degrees (log)"
    PLOT_INFO = plot_module.store_details(PLOT_NAME, TITLE, SUBTITLE,
                                          LABEL_X, LABEL_Y)
    TOTAL_NODES = 27000
    EXISTING_NODES = 12
    DPA_GRAPH = make_dpa_graphs(TOTAL_NODES, EXISTING_NODES)
    plot_module.plot_graph(DPA_GRAPH, PLOT_INFO, plot_color="#f7d80c",
                           xy_limits=((1e0, 1e4), (1e-5, 1e0)))


    print("Done")
    print("=" * 25)
