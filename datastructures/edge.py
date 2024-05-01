from typing import Any

class Edge:
    """An edge in a graph."""
    def __init__(self, destination_vertex=None, edge_data: Any=None, weight: Any=None) -> None:
        """Create an edge to the given vertex with the given weight.

        Examples:
            >>> edge = Edge(Vertex("Portland"), 100)
            >>> edge.destination_vertex
            Portland
            >>> edge.weight
            100
        
        Args:
            destination_vertex (Vertex): The destination vertex of the edge.
            weight (Any): The weight of the edge.
            
        Returns:
            None
        """
        self._destination_vertex = destination_vertex
        self._edge_data = edge_data
        self._weight = weight

    @property
    def destination_vertex(self):
        """Return the destination vertex of the edge.
        
        Examples:
            >>> edge = Edge(Vertex("Portland"), 100)
            >>> edge.destination_vertex
            Portland
            
        Returns:
            Vertex: The destination vertex of the edge.
        """
        return self._destination_vertex

    @property
    def weight(self) -> Any:
        """Return the weight of the edge.
        
        Examples:
            >>> edge = Edge(Vertex("Portland"), 100)
            >>> edge.weight
            100
            
        Returns:
            Any: The weight of the edge.
        """
        return self._weight
    
    def __lt__(self, object: Any) -> bool:
        """Return True if the weight of the edge is less than the weight of the object.
        
        Examples:
            >>> edge = Edge(Vertex("Portland"), 100)
            >>> edge2 = Edge(Vertex("Salem"), 200)
            >>> edge < edge2
            True
            
        Args:
            object (Any): The object to compare the edge to.
            
        Returns:
            bool: True if the weight of the edge is less than the weight of the object.
        """
        if not isinstance(object, Edge):
            return False
        return self.weight < object.weight
    
    def __gt__(self, object: Any) -> bool:
        """Return True if the weight of the edge is greater than the weight of the object.
        
        Examples:
            >>> edge = Edge(Vertex("Portland"), 100)
            >>> edge2 = Edge(Vertex("Salem"), 200)
            >>> edge > edge2
            False
            
        Args:
            object (Any): The object to compare the edge to.
            
        Returns:
            bool: True if the weight of the edge is greater than the weight of the object.
        """
        if not isinstance(object, Edge):
            return False
        return self.weight > object.weight

    @destination_vertex.setter
    def destination_vertex(self, destination_vertex) -> None:
        """Set the destination vertex of the edge.
        
        Examples:
            >>> edge = Edge(Vertex("Portland"), 100)
            >>> edge.destination_vertex = Vertex("Salem")
            >>> edge.destination_vertex
            Salem

        Args:
            destination_vertex (Vertex): The destination vertex of the edge.

        Returns:
            None
        """
        self._destination_vertex = destination_vertex

    @weight.setter
    def weight(self, weight) -> None:
        """Set the weight of the edge.
        
        Examples:
            >>> edge = Edge(Vertex("Portland"), 100)
            >>> edge.weight = 200
            >>> edge.weight
            200
            
        Args:
            weight (Any): The weight of the edge.
        """
        self._weight = weight
    
    @property
    def edge_data(self) -> Any:
        """Return the edge data of the edge.

        Examples:
            >>> edge = Edge(Vertex("Portland"), 100, "I-5")
            >>> edge.edge_data
            I-5

        Returns:
            Any: The edge data of the edge.
        """
        return self._edge_data
    
    @edge_data.setter
    def edge_data(self, edge_data) -> None:
        """Set the edge data of the edge.
        
        Examples:
            >>> edge = Edge(Vertex("Portland"), 100, "I-5")
            >>> edge.edge_data = "I-205"
            >>> edge.edge_data
            I-205

        Args:
            edge_data (Any): The edge data of the edge.

        Returns:
            None
        """
        self._edge_data = edge_data

    def __str__(self) -> str:
        """Return a string representation of the edge.
        
        Examples:
            >>> edge = Edge(Vertex("Portland"), 100)
            >>> str(edge)
            Edge to Portland with weight 100
        
        Returns:
            str: A string representation of the edge.
        """
        return f"Edge to {self._destination_vertex} with weight {self._weight}"

    def __repr__(self) -> str:
        """Return a string representation of the edge.
        
        Examples:
            >>> edge = Edge(Vertex("Portland"), 100)
            >>> repr(edge)
            Edge to Portland with weight 100
            
        Returns:
            str: A string representation of the edge.
        """
        return str(self)