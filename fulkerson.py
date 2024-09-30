class Edge(object):
    def __init__(self, source, sink, capacity):
        self.source = source
        self.sink = sink
        self.capacity = capacity

    def __repr__(self):
        return "%s -> %s : %d" % (self.source, self.sink, self.capacity)

class Flow(object):

    def __init__(self):
        self.edges = {}
        self.adjacents = {}

    def add_edges(self, source, sink, capacity):
        if source == sink:
            raise ValueError("Source cannot be the Sink.")
        
        edge = Edge(source, sink, capacity)
        redge = Edge(sink, source, 0)
        
        self.edges[edge] = 0
        self.edges[redge] = 0

        if source not in self.adjacents:
            self.adjacents[source] = []
        if sink not in self.adjacents:
            self.adjacents[sink] = []

        self.adjacents[source].append(edge)
        self.adjacents[sink].append(redge)

    def valid_path(self, source, sink, path):

        if source == sink:
            return path
        for edge in self.adjacents[source]:
            if edge not in path:
                if edge.capacity - self.edges[edge] > 0:
                    result = self.valid_path(edge.sink, sink, path + [edge])
                    if result:
                        return result

        return None

    def max_flow(self, source, sink):
        path = self.valid_path(source, sink, [])

        while path:
            min_flow = min(edge.capacity - self.edges[edge] for edge in path)
            for edge in path:
                self.edges[edge] += min_flow
                for redge in self.adjacents[edge.sink]:
                    if redge.sink == edge.source:
                        self.edges[redge] -= min_flow
            
            path = self.valid_path(source, sink, [])

        return sum(self.edges[edge] for edge in self.adjacents[source])


t = Flow()
t.add_edges('1', '2', 17)
t.add_edges('1', '3', 28)
t.add_edges('1', '4', 21)
t.add_edges('2', '3', 20)
t.add_edges('3', '8', 17)
t.add_edges('3', '9', 24)
t.add_edges('4', '5', 18)
t.add_edges('5', '6', 45)
t.add_edges('5', '11', 21)
t.add_edges('6', '7', 16)
t.add_edges('6', '11', 34)
t.add_edges('7', '15', 22)
t.add_edges('8', '6', 14)
t.add_edges('8', '7', 9)
t.add_edges('9', '10', 24)
t.add_edges('9', '13', 12)
t.add_edges('10', '12', 50)
t.add_edges('11', '21', 70)
t.add_edges('12', '17', 23)
t.add_edges('13', '12', 30)
t.add_edges('14', '7', 17)
t.add_edges('14', '15', 16)
t.add_edges('15', '16', 20)
t.add_edges('16', '21', 20)
t.add_edges('17', '14', 40)
t.add_edges('17', '18', 12)
t.add_edges('18', '19', 60)
t.add_edges('18', '20', 46)
t.add_edges('19', '20', 11)
t.add_edges('20', '16', 30)
t.add_edges('20', '21', 22)


print("Fluxo máximo: ",t.max_flow('1', '21'))
