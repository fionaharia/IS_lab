import itertools

class TravellingSalesmanProblem:
    def __init__(self, distances):
        self.distances = distances
        self.num_cities = len(distances)
        self.cities = range(self.num_cities)

    def calculate_route_distance(self, route):
        distance = 0
        for i in range(len(route) - 1):
            distance += self.distances[route[i]][route[i+1]]
        distance += self.distances[route[-1]][route[0]]  
        return distance

    def movegen(self, start_city): #possible routes
        other_cities = [city for city in self.cities if city != start_city]
        routes = itertools.permutations(other_cities)
        full_routes = [(start_city,) + route for route in routes]
        return full_routes

    def goaltest(self, route):
        return len(route) == self.num_cities and len(set(route)) == self.num_cities

    def find_shortest_route(self, start_city=0):
        shortest_route = None
        min_distance = float('inf')
        for route in self.movegen(start_city):
            if self.goaltest(route):
                current_distance = self.calculate_route_distance(route)
                if current_distance < min_distance:
                    min_distance = current_distance
                    shortest_route = route
        return shortest_route, min_distance

def main():
    print("Enter the number of cities:")
    num_cities = int(input())
    
    distances = []
    print("Enter the distance matrix (enter the distances row by row):")
    for i in range(num_cities):
        row = list(map(int, input().split()))
        distances.append(row)
    
    tsp = TravellingSalesmanProblem(distances)
    
    start_city = 0  
    shortest_route, min_distance = tsp.find_shortest_route(start_city)
    
    print(f"The shortest route starting from city {start_city} is: {shortest_route}")
    print(f"The minimum distance is: {min_distance}")

if __name__ == "__main__":
    main()
