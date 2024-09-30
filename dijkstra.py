import heapq

class Graph:
    def __init__(self):
        self.edges = {}
    
    def add_edge(self, source, sink, cost):
        if source not in self.edges:
            self.edges[source] = []
        if sink not in self.edges:
            self.edges[sink] = []
        
        self.edges[source].append((cost, sink))
        self.edges[sink].append((cost, source))  

    def dijkstra(self, start, target):
        queue = [(0, start, [])]  
        visited = set()  

        while queue:
            (cost, node, path) = heapq.heappop(queue) 
            if node in visited:
                continue

            path = path + [node]

            if node == target:
                return cost, path

            visited.add(node)

            for edge_cost, neighbor in self.edges[node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + edge_cost, neighbor, path))

        return float("inf"), [] 


graph = Graph()
graph.add_edge('1', '2', 17)
graph.add_edge('1', '3', 28)
graph.add_edge('1', '4', 21)
graph.add_edge('2', '3', 20)
graph.add_edge('3', '8', 17)
graph.add_edge('3', '9', 24)
graph.add_edge('4', '5', 18)
graph.add_edge('5', '6', 45)
graph.add_edge('5', '11', 21)
graph.add_edge('6', '7', 16)
graph.add_edge('6', '11', 34)
graph.add_edge('7', '15', 22)
graph.add_edge('8', '6', 14)
graph.add_edge('8', '7', 9)
graph.add_edge('9', '10', 24)
graph.add_edge('9', '13', 12)
graph.add_edge('10', '12', 50)
graph.add_edge('11', '21', 70)
graph.add_edge('12', '17', 23)
graph.add_edge('13', '12', 30)
graph.add_edge('14', '7', 17)
graph.add_edge('14', '15', 16)
graph.add_edge('15', '16', 20)
graph.add_edge('16', '21', 20)
graph.add_edge('17', '14', 40)
graph.add_edge('17', '18', 12)
graph.add_edge('18', '19', 60)
graph.add_edge('18', '20', 46)
graph.add_edge('19', '20', 11)
graph.add_edge('20', '16', 30)
graph.add_edge('20', '21', 22)


start_node = '1'
target_node = '21'
cost, path = graph.dijkstra(start_node, target_node)

print(f"O menor caminho de {start_node} para {target_node} tem custo {cost} e passa por: {path}")
