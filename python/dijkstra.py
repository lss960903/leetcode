class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))
        stops = [float('inf')] * n
        hp = []
        heappush(hp, [0,src, 0])
        while hp:
            cur = heappop(hp)
            cost = cur[0]
            node = cur[1]
            steps = cur[2]

            if steps > stops[node] or steps > k+1:
                continue
            stops[node] = steps
            if node == dst:
                return cost
            if node in adj:
                for l in adj[node]:
                    newcost = cost + l[1]
                    heappush(hp, [newcost, l[0], steps+1])
        return -1
