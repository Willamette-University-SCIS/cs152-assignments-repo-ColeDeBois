from __future__ import annotations
from typing import Any

from datastructures.array import Array
from datastructures.hash_map import HashMap
from datastructures.vertex import Vertex
from datastructures.edge import Edge

class Graph:
    """ Class Graph. Represents a graph data structure containing
            vertices and edges.
        Depends on Edge and Vertex classes.
        Stipulations:
        1. Must adhere to the docstring requirements per method, including raising
            raising appropriate exceptions where indicated.
    """
    def __init__(self) -> None:
        """Create an empty graph.
        
        Examples:
            >>> graph = Graph()
            
        Returns:
            None    
        """
        self._vertices: HashMap[Vertex] = HashMap()

    @property
    def vertices(self) -> Array[Vertex]:
        """Return the vertices of the graph.
        
        Examples: 
            >>> graph = Graph()
            >>> graph.add_vertex("Portland")
            >>> graph.vertices
            [Portland]
            
        Returns:
            Array[Vertex]: The vertices of the graph.
        """
        vertices = Array(len(self._vertices))
        for i, vertex in enumerate(self._vertices.keys()):
            vertices[i] = vertex

        return vertices

    def add_vertex(self, vertex_data: Any) -> None:
        """Add a vertex to the graph.
        
        Examples:
            >>> graph = Graph()
            >>> graph.add_vertex("Portland")
            >>> graph.add_vertex("Salem")
            >>> graph.vertices
            [Portland, Salem]
        
        Args:
            vertex_data (Any): The vertex data for the vertex to add to the graph.
            
        Returns:
            None
            
        """
        self._vertices[vertex_data] = Vertex(vertex_data)

    def remove_vertex(self, vertex_data: Any) -> None:
        """Remove a vertex from the graph.
        
        Examples:
            >>> graph = Graph()
            >>> graph.add_vertex(Vertex("Portland"))
            >>> graph.add_vertex(Vertex("Salem"))
            >>> graph.remove_vertex(Vertex("Portland"))
            >>> graph.vertices
            [Salem]

        Args:
            vertex (Vertex): The vertex to remove from the graph.

        Returns:
            None

        Raises:
            ValueError: If the vertex is not in the graph.
        """
        del self._vertices[vertex_data]

    def add_edge(self, vertex1_data: Any, vertex2_data: Any, edge_data: Any, weight: Any) -> None:
        """Add an edge between two vertices with the given weight. The vertices will be added if they do not exist.
        
        Examples:
            >>> graph = Graph()
            >>> graph.add_edge("Portland", "Salem", "I-5", 50)
            >>> graph.edges_from("Portland")
            [Salem via I-5 (50)]

        Args:
            vertex1_data (Any): The data of the first vertex.
            vertex2_data (Any): The data of the second vertex.
            edge_data (Any): The data of the edge.
            weight (Any): The weight of the edge.
        """
        vertex1: Vertex = None
        vertex2: Vertex = None

        for vertex_data, vertex in self._vertices.items():
            if vertex_data == vertex1_data:
                vertex1 = vertex
            elif vertex_data == vertex2_data:
                vertex2 = vertex
        
        if vertex1 is None:
            vertex1 = Vertex(vertex1_data)
            self._vertices[vertex1_data] = vertex1

        if vertex2 is None:
            vertex2 = Vertex(vertex2_data)
            self._vertices[vertex2_data] = vertex2

        edge = Edge(vertex2, edge_data, weight)
        vertex1.add_edge(edge)

    def remove_edge(self, vertex1_data: Any, vertex2_data: Any, edge_data:Any) -> None:
        """Remove an edge between two vertices. The vertices will not be removed.
        
        Examples:
            >>> graph = Graph()
            >>> graph.add_edge("Portland", "Salem", "I-5", 50)
            >>> graph.add_edge("Portland", "Salem", "Hwy 99", 59)
            >>> graph.edges_from("Portland")
            [Salem via I-5 (50), Salem via Hwy 99 (59)]
            >>> graph.remove_edge("Portland", "Salem", "I-5")
            >>> graph.edges_from("Portland")
            [Salem via Hwy 99 (59)]

        Args:
            vertex1_data (Vertex): The data of the first vertex.
            vertex2_data (Vertex): The data of the second vertex.
            edge_data (Any): The data of the edge.

        Returns:
            None

        Raises: 
            ValueError: If either vertex does not exist or the edge does not exist between the two vertices.
        """
        vertex1: Vertex = None
        vertex2: Vertex = None
        edge : Edge = None

        for vertex in self._vertices:
            if vertex.data == vertex1_data:
                vertex1 = vertex
            elif vertex.data == vertex2_data:
                vertex2 = vertex
        
        if vertex1 is None or vertex2 is None:
            raise ValueError("Vertex not found")
        
        for e in vertex1.edges:
            if e.destination_vertex == vertex2 and e.data == edge_data:
                edge = e

        if edge is None:
            raise ValueError("Edge not found")
        
        vertex1.remove_edge(edge)

    def edges_from(self, vertex_data: Any) -> Array[Any]:
        """Return the edges from the given vertex.
        
        Examples:
            >>> graph = Graph()
            >>> graph.add_vertex("Portland")
            >>> graph.add_vertex("Salem")
            >>> graph.add_edge("Portland", "Salem", "I-5", 50)
            >>> graph.edges_from("Portland")
            [I-5]

        Args:
            vertex_data (Any): The data of the vertex.

        Returns:
            Array[Any]: The data from the edges from the vertex.

        Raises:
            ValueError: If the vertex is not in the graph.
        """

        vertex: Vertex = None
        v: Vertex = None
        for v in self._vertices.values():
            if v.vertex_data == vertex_data:
                vertex = v
        
        if vertex is None:
            raise ValueError("Vertex not found")
        
        return vertex.edges
    def get_vertex(self, vertex_data: Any) -> Vertex:
        """Return the vertex with the given data.
        
        Examples:
            >>> graph = Graph()
            >>> graph.add_vertex("Portland")
            >>> vertex = graph.get_vertex("Portland")
            >>> print(vertex)
            Vertex with value Portland

        Args:
            vertex_data (Any): The data of the vertex.

        Returns:
            Vertex: The vertex with the given data.

        Raises:
            ValueError: If the vertex is not in the graph.
        """
        for vertex in self._vertices.values():
            if vertex.vertex_data == vertex_data:
                return vertex
        
        raise ValueError("Vertex not found")

    def __str__(self) -> str:
        """Return a string representation of the graph.
        
        Examples:
            >>> graph = Graph()
            >>> graph.add_vertex(Vertex("Portland"))
            >>> graph.add_vertex(Vertex("Salem"))
            >>> str(graph)
            [Portland, Salem]
        """

        return f"{self._vertices}"

    def __repr__(self) -> str:
        """Return a string representation of the graph.
        
        Examples:
            >>> graph = Graph()
            >>> graph.add_vertex(Vertex("Portland"))
            >>> graph.add_vertex(Vertex("Salem"))
            >>> repr(graph)
            [Portland, Salem]
        """
        return str(self)
