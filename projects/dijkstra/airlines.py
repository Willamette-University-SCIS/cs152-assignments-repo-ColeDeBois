import csv
from typing import Any, NamedTuple
from datastructures.graph import Graph
from datastructures.hash_map import HashMap
from datastructures.list_queue import ListQueue as Queue
from datastructures.list_stack import ListStack as Stack
from haversine import haversine, Unit

class Airport(NamedTuple):
    id: int
    name: str
    code: str
    city: str
    country: str
    latitude: float
    longitude: float
    __str__ = lambda self: f'{self.name} ({self.code})'
    __repr__ = lambda self: f'Airport({self.code})'

class Flight():
    def __init__(self, origin: Airport, destination: Airport) -> None:
        self._origin: Airport = origin
        self._destination: Airport = destination

    @property
    def weight(self) -> float:
        origin = (self._origin.latitude, self._origin.longitude)
        destination = (self._destination.latitude, self._destination.longitude)
        return haversine(origin, destination, Unit.MILES)
    
    def __lt__(self, object: Any) -> bool:
        if not isinstance(object, Flight):
            return False
        return self.weight < object.weight
    
class FlightPlanner:
    def __init__(self, filename:str='projects/dijkstra/routes.csv') -> None:
        '''initialize the class with the graph, airports, distances, and previous hashmaps, and a fake source airport to avoid errors'''
        self.graph = Graph()
        self.airports = {}
        self.distances = HashMap()
        self.previous = HashMap()
        self.source:Airport = Airport(0, 'NOT REAL', 'FAKE', 'ATLANTIS', 'ATLANTICA', 0, 0)
        
        '''initialize the graph and airports from the csv file'''
        csv_reader = csv.DictReader(open(filename, newline="\n", encoding="utf-8-sig"))
        for row in csv_reader:
            origin = Airport(
                int(row['origin_airport_id']), 
                row['origin_airport'], 
                row['origin_airport_code'], 
                row['origin_city'], 
                row['origin_country'], 
                float(row['origin_airport_latitude']), 
                float(row['origin_airport_longitude']))
            
            destination = Airport(
                int(row['destination_airport_id']), 
                row['destination_airport'], 
                row['destination_airport_code'], 
                row['destination_city'], 
                row['destination_country'], 
                float(row['destination_airport_latitude']), 
                float(row['destination_airport_longitude']))

            flight = Flight(origin, destination)
            weight = flight.weight
            self.graph.add_edge(origin, destination, flight, weight)
            self.airports[origin.code] = origin
            self.airports[destination.code] = destination



    def dijkstra(self, start:str)->None:
        '''runs dijkstras algorithm on the graph from the start airport, adds the distances and previous to the class'''
        #make tables
        caps=len(self.graph.vertices)*2
        distances=HashMap(caps)
        previous=HashMap(caps)
        visited=HashMap(caps)
        que=Queue()

        #initialize tables
        source=self.airports[start]
        for vertex in self.graph.vertices:
            if vertex == source:
                distances[vertex]=0
            else: distances[vertex]=-1
            previous[vertex]=None
            visited[vertex]=False
        
        #run algorithm loop
        que.enqueue(source)
        while not que.empty:
            current=que.dequeue()
            visited[current]=True
            neighbors=sorted(self.graph.edges_from(current))
            for e in neighbors:
                dest_vertex=e.destination_vertex
                dist=e.weight + distances[current]
                dest=dest_vertex.vertex_data

                if dist < distances[dest] or distances[dest] < 0:
                    distances[dest] = dist
                    previous[dest] = current
                    if not visited[dest]:
                        que.enqueue(dest)
                    
        self.distances=distances
        self.previous=previous
        self.source=source
    
    def backtrack(self, end:Airport) -> Stack:
        '''returns a stack of the path from the source to the end airport'''
        path=Stack()
        current=end
        while current is not None:
            path.push(current)
            current=self.previous[current]
        return path
    
    def print_path(self, end:str)->None:
        '''prints the path from the source to the end airport'''
        end=self.airports[end]
        print(f'From {self.source.code} to {end} - {self.distances[end]} miles\n')
        path=self.backtrack(end)
        indent=0
        while not path.empty:
            airport=path.pop()
            print(' '*indent,f'\u2708 {airport} - {self.distances[airport]} miles')
            indent+=1

