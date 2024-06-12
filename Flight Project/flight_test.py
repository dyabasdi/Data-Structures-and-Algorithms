import unittest
import pandas as pd
from final_project import Flight, Airport, Network

class final_project_test(unittest.TestCase):
    def setUp(self):
        self.network = Network(9)
        self.network = self.network.create_graphs(9,"dataset.xlsx", "airports.xlsx")
        self.origin = 0
        self.destination = 2
        self.network.clear()
        self.network.create_adj_matrix(self.network.airports[self.origin])
        self.dijkstra, self.paths = self.network.dijkstra(self.origin)

    
    def test_HND_airport(self):
        path = []
        path = self.network.find_path(self.destination, self.paths, path)
        total_cost = self.dijkstra[self.destination]
        self.assertEqual(total_cost, 1302)
        self.assertEqual(path, [0,2])
    
    def test_BKK_airport(self):
        self.destination = 8
        path = []
        path = self.network.find_path(self.destination, self.paths, path)
        total_cost = self.dijkstra[self.destination]
        self.assertEqual(total_cost, 1743)
        self.assertEqual(path, [0,5,1,8])

    
    def test_IST_airport(self):
        self.destination = 1
        path = []
        path = self.network.find_path(self.destination, self.paths, path)
        total_cost = self.dijkstra[self.destination]
        self.assertEqual(total_cost, 1043)
        print(path)
        self.assertEqual(path, [0,5,1])


if __name__ == '__main__':
    unittest.main()