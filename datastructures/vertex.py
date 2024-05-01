from __future__ import annotations
from datastructures.array import Array
from datastructures.edge import Edge
from typing import Any

from datastructures.linked_list import LinkedList

class Vertex:
    """A vertex in a graph."""
    def __init__(self, vertex_data: Any=None):
        """Create a vertex with the given value.
        
        Examples:
            >>> vertex = Vertex("Portland")
            >>> vertex.vertex_data
            Portland
            >>> vertex.edges
            []
            
        Args:
            vertex_data (Any): The data of the vertex.

        Returns:
            None
        """
        self._vertex_data = vertex_data
        self._edges = []
        self._visited = False

    @property
    def vertex_data(self) -> Any:
        """Return the data of the vertex.
        
        Examples:
            >>> vertex = Vertex("Portland")
            >>> vertex.vertex_data
            Portland
            
        Returns:
            Any: The data of the vertex.
        """
        return self._vertex_data
    
    @vertex_data.setter
    def vertex_data(self, vertex_data) -> None:
        """Set the data of the vertex.
        
        Examples:
            >>> vertex = Vertex("Portland")
            >>> vertex.vertex_data = "Salem"
            >>> vertex.vertex_data
            Salem

        Args:
            vertex_data (Any): The data of the vertex.

        Returns:
            None
        """
        self._vertex_data = vertex_data

    @property
    def edges(self) -> Array[Any]:
        """Return the edges of the vertex.
        
        Examples:
            >>> vertex = Vertex("Portland")
            >>> vertex.edges
            []

        Returns:
            Array[Edge]: The edges of the vertex.
        """
        return self._edges

    def add_edge(self, edge: Edge) -> None:
        """Add an edge to the vertex.
        
        Examples:
            >>> vertex = Vertex("Portland")
            >>> vertex.add_edge(Edge(Vertex("Salem"), 100))
            >>> vertex.edges

        Args:
            edge (Edge): The edge to add to the vertex.

        Returns:
            None
        """
        self._edges.append(edge)

    def remove_edge(self, destination_vertex: Vertex) -> None:
        """Remove an edge from the vertex.
        
        Examples:
            >>> vertex = Vertex("Portland")
            >>> vertex.add_edge(Edge(Vertex("Salem"), 100))

        Args:
            destination_vertex (Vertex): The destination vertex of the edge.

        Returns:
            None

        Raises:
            ValueError: If the edge is not found.
        """
        for edge in self._edges:
            if edge.destination_vertex == destination_vertex:
                self._edges.remove(edge)
        
        raise ValueError("Edge not found")
    
    def get_edge(self, destination_vertex: Vertex) -> Edge:
        """Return the edge to the given destination vertex.
        
        Examples:   
            >>> vertex = Vertex("Portland")
            >>> vertex.add_edge(Edge(Vertex("Salem"), 100))
            >>> vertex.get_edge(Vertex("Salem"))
            Edge(Vertex("Salem"), 100)

        Args:
            destination_vertex (Vertex): The destination vertex of the edge.

        Returns:
            Edge: The edge to the given destination vertex.

        Raises: 
            ValueError: If the edge is not found.
        """
        for edge in self._edges:
            if edge.destination_vertex == destination_vertex:
                return edge
        
        raise ValueError("Edge not found")

    def __str__(self) -> str:
        """Return a string representation of the vertex.
        
        Examples:
            >>> vertex = Vertex("Portland")
            >>> print(vertex)
            Vertex with value Portland
            
        Returns:
            str: A string representation of the vertex.
        """
        return f"Vertex with value {self._vertex_data}"

    def __repr__(self) -> str:
        """Return a string representation of the vertex.
        
        Examples:
            >>> vertex = Vertex("Portland")
            >>> repr(vertex)
            Vertex with value Portland
            
        Returns:
            str: A string representation of the vertex.    
        """
        return f"Vertex({self._vertex_data})"