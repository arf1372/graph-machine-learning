"""Utility functions for working with graphs"""

import networkx as nx


def adjustency_graph(g: nx.Graph) -> nx.Graph:
    """Converts a graph to it's edge graph

    An adjustency graph (edge graph) is a graph made by considering
    each edge as a node, and each node as an edge.

    Args:
        g: A networkx graph

    Returns:
        A networkx graph
    """
    adj_g = nx.Graph()
    edges_set = set(g.edgeslist())
    for edge in edges_set:
        adj_g.add_node(f"{edge[0]}-{edge[1]}", edge=edge)
    for n1, edge_1 in adj_g.nodes.items():
        for n2, edge_2 in adj_g.nodes.items():
            if edge_1["edge"] == edge_2["edge"]:
                continue
            if set(edge_1["edge"]).intersection(set(edge_2["edge"])):
                adj_g.add_edge(n1, n2)

    return adj_g