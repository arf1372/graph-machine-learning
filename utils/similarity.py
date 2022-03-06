"""This module contains utility functions and classes for
computing nodes, edges and graph similarities
"""


from typing import Union, List, Callable


def dot_product(a: List[int], b: List[int]) -> int:
    """Compute the dot product of two vectors

    Args:
        a (List[int]): first vector
        b (List[int]): second vector

    Returns:
        int: dot product of the two vectors
    """

    if (len(a) != len(b)):
        raise ValueError(
            f"Vectors must be of the same length. ({len(a)}, {len(b)} given)")

    return sum(a[i] * b[i] for i in range(len(a)))


def vector_length(a: List[int]) -> float:
    """Compute the length of a vector

    Args:
        a (List[int]): vector

    Returns:
        float: length of the vector
    """

    return sum(a[i] ** 2 for i in range(len(a))) ** 0.5


def jaccard_index(nodes_a: List[int], nodes_b: List[int]) -> float:
    """Compute the Jaccard index of two nodes

    Args:
        nodes_a (set): first nodes
        nodes_b (set): second nodes

    Returns:
        float: Jaccard index of the two nodes
    """

    return dot_product(nodes_a, nodes_b) / (
        sum(nodes_a) + sum(nodes_b) - dot_product(nodes_a, nodes_b)
    )


def cosine_similarity(nodes_a: List[int], nodes_b: List[int]) -> float:
    """Compute the cosine similarity of two nodes

    Args:
        nodes_a (List[int]): first adjustency list of nodes
        nodes_b (List[int]): second adjustency list of nodes

    Returns:
        float: cosine similarity of the two nodes
    """

    return dot_product(nodes_a, nodes_b) / (vector_length(nodes_a) * vector_length(nodes_b))


def node_similarity(n1: List[int], n2: List[int], kind: Union(str, Callable) = jaccard_index) -> float:
    """Computes similarity between two nodes in a graph

    args:
        n1 (List[int]): a graph node
        n2 (List[int]): another graph node
        kind ([str, Callable]): the similarity measure
        
    Returns
        float: similarity between two nodes
    """

    if isinstance(kind, str):
        kind = kind.lower()
        if kind == "jaccard":
            kind = jaccard_index
        elif kind == "cosine":
            kind = cosine_similarity
        else:
            raise ValueError("Invalid similarity. 'kind' must be \"jaccard\", \"cosine\" or a callable")
    elif not isinstance(kind, Callable):
        raise ValueError("Invalid similarity. 'kind' must be \"jaccard\", \"cosine\" or a callable")
    
    return kind(n1, n2)

def edge_similarity(e1: List[int], e2: List[int], kind: Union(str, Callable) = jaccard_index) -> float:
    """Computes similarity between two edges in a graph

    args:
        e1 (List[int]): a graph edge
        e2 (List[int]): another graph edge
        kind ([str, Callable]): the similarity measure
        
    Returns
        float: similarity between two edges
    """

    return node_similarity(e1, e2, kind)