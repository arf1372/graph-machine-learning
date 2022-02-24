"""This module contains utility functions and classes for
computing nodes, edges and graph similarities
"""

from typing import Union, List


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
