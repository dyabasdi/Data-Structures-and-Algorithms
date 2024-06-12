import sys
import pandas as pd
class Flight():
    """
    Flight Instance Object
    Contains destination, time, price
    """
    def __init__(self,origin,destination,departure_time,arrival_time,price):
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price


    def __str__(self): #/n doesnt work properly here
        string = 'Origin: ' + str(self.origin) +'\n'
        string += 'Destination: ' + str(self.destination) + '\n'
        string += 'Departure Time: ' + str(self.departure_time) + '\n'
        string += 'Arrival Time: ' + str(self.arrival_time) +'\n'
        string += f'Price: ${self.price:.2f} \n'
        return string


class Airport():
    """
    Airport Object containing array of flight objects
    Contains list of destinations and list of flights
    Acts as node in graph. 
    Label to access them by name and number to access by index in graph
    """
    def __init__(self,name):
        self.name = name
        self.flights = []
        self.destinations = set()
        self.visited = False

    def add_flight(self,flight):
        #adds a flight object to list of flights
        self.flights.append(flight)
        self.destinations.add(flight.destination)
    
    def get_flights(self,destination):
        #Returns list of flights to destination.
        #Destination is string parameter indicating label of airport
        flights = []
        for flight in self.flights:
            if flight.destination == destination:
                flights.append(flight)
        return flights

    def unvisit(self):
        self.visited = False
    
    def visit(self):
        self.visited = True
    
    def get_destinations(self):
        #returns destinations from airport as an array
        destinations = []
        for item in self.destinations:
            destinations.append(item)
        return destinations
    
    def remove_flight(self,flight):
        #remove flight from airport
        self.flights.remove(flight)
        self.destinations = set()
        for item in self.flights:
            self.destinations.add(item.destination)
    
    def __str__(self):
        return str(self.name)
 
  

class Network():
    """
    Class containing network of airports
    """
    def __init__(self,vertices,weight = "Cost"):
        self.vertices = vertices
        self.airports = []
        self.adj_mat = [[0 for i in range(vertices)]for j in range(vertices)]
        self.weight = weight

    def has_vertex(self, label):
        """Check if an airport is already in the graph"""
        for item in self.airports:
            if label == item.name:
                return True
        return False


    def get_index(self, label):
        """Given a label get the index of an airport"""
        for i, airport in enumerate(self.airports):
            if airport.name == label:
                return i 
        return -1

    def get_airport(self,label):
        """Returns airport with specified label from array"""
        for airport in self.airports:
            if airport.name == label:
                return airport
        return -1

    def add_vertex(self, airport):
        """Add an airport with a given label to the graph"""
        label = airport.name
        if self.has_vertex(label):
            return
        # add vertex to the list of airports
        self.airports.append(airport)

    def add_directed_edge(self, start, finish, weight=1):
        """Add weighted directed edge to graph"""
        self.adj_mat[start][finish] = weight

    def add_undirected_edge(self, start, finish, weight=1):
        """Add weighted undirected edge to graph"""
        self.adj_mat[start][finish] = weight
        self.adj_mat[finish][start] = weight
    
    def clear(self):
        for airport in self.airports:
            airport.unvisit()

    def print_adj_mat(self):
        for row in self.adj_mat:
            for val in row:
                string=''.join([str(val)+' ' for val in row])
            print(string)

    def create_adj_matrix(self,origin):
        #origin is an airport object representing airport to start from
        #function performs filtering to remove all flights with departure times after arrival time
        #destination is an airport object
      
        #recursive implementation to create adj_matrix starting from specified origin node
        while origin.visited == False:
            origin.visit()
            for destination in origin.get_destinations():
                #acquire all flights to a destination and sort by weight parameter to determine weighting
                flights = origin.get_flights(destination)
                flights = sorted(flights, key = lambda flight: flight.price)
                weight = flights[0].price
                #Weight by lowest cost/flight time depending on parameter and mark used flight as edge
                #create edge in adj_mat from origin to destination
                self.add_directed_edge(self.get_index(origin.name), self.get_index(destination),weight)
                self.create_adj_matrix(self.get_airport(destination))
             
    def minweight(self,weight,visited):
        min = sys.maxsize
        min_index = 0
        for vertex in range(self.vertices):
            if weight[vertex] < min and visited[vertex] == False:
                min = weight[vertex]
                min_index = vertex
        return min_index

    def dijkstra(self,start):
        #creates shortest path tree to all nodes from start path based on weighting.
        #start is a string containing the name of the airport to start at
        #convert string name to node number of index containing that name
        origin = self.get_index(start)
        origin = start
        if origin != -1:
            #array to store weight values for each vertex
            weight = [sys.maxsize for i in range(self.vertices)]
            weight[origin]=0
            paths = [-1]*self.vertices
            paths[origin] = -1
            visited = [False for i in range(self.vertices)]
            for i in range(self.vertices):
                nearest_vertex = self.minweight(weight,visited)
                visited[nearest_vertex]=True
                for vertex in range(self.vertices):
                    #iterate over all vertices adjacent to vertice x and check update weighting
                    #weight[y] > weight[x] + self.adj_mat[x][y] checks if weight to that vertice has been updated
                    if self.adj_mat[nearest_vertex][vertex] > 0 and visited[vertex] == False and \
                            weight[vertex] > weight[nearest_vertex] + self.adj_mat[nearest_vertex][vertex]:
                        weight[vertex] = weight[nearest_vertex] + self.adj_mat[nearest_vertex][vertex]
                        paths[vertex] = nearest_vertex
            return weight,paths


    def find_path(self,vertex,paths,path=[]):
        #recursively calculates path taken by dijkstra and returns as array
        if vertex == -1:
            return
        self.find_path(paths[vertex],paths,path)
        path.append(vertex)
        return path


    def print_path(self,origin,destination,path):
        #Properly formats the Steps in which airports are traversed in print statements
        #origin is the index number of original airport. Can find index with get_index()function
        print_path = "Start: " + self.airports[origin].name + '\n'
        print_path += "Destination: " + self.airports[destination].name + '\n'
        for i in range(len(path)-1):
            print_path += self.airports[path[i]].name + " --> " + self.airports[path[i+1]].name +'\n'
        print(print_path)


    def create_graphs(self,num_airports, excel_file1, excel_file2):
        df1 = pd.read_excel(excel_file1)
        df2 = pd.read_excel(excel_file2)
        airports = list(df2.Airports)
        list_airports = []
        for i in range(len(airports)):
            list_airports.append(i)
            list_airports[i] = Airport(airports[i])
        origin = list(df1.Origin)
        destination = list(df1.Destination)
        dep_time = list(df1.DepartureTime)
        arr_time = list(df1.ArrivalTime)
        price = list(df1.Price)
        graph = Network(num_airports)
        graph.airports = list_airports
        num_flights = len(origin)
        flights = []
        for i in range(num_flights):
            flights.append(Flight(origin[i], destination[i], dep_time[i], arr_time[i], price[i]))
        for airport in list_airports:
            for flight in flights:
                if airport.name == flight.origin:
                    airport.add_flight(flight)
            graph.add_vertex(airport)
        return graph


def main():
    network = Network(9)
    network = network.create_graphs(9,"dataset.xlsx", "airports.xlsx")
    network.clear()
    origin = 0
    valid = False
    while not valid:
        destination_input = str(input("Enter a destination:"))
        for i in range(len(network.airports)):
            if destination_input == network.airports[i].name:
                destination = i
                valid = True
                break
        else:
            print("Invalid Destination. Try again.")
    
    network.create_adj_matrix(network.airports[origin])
    dijkstra, paths = network.dijkstra(origin)
    path = network.find_path(destination,paths)
    total_cost=dijkstra[destination]
    print(f'Total cost: ${total_cost:.2f}')
    network.print_path(origin, destination, path)


if __name__ =="__main__":
    main()
