class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = UnionFind(len(edges))
        res = []
        for l in edges:
            if dsu.find(l[0]) != dsu.find(l[1]):
                dsu.join(l[0], l[1])
            else:
                res = l
        return res

class UnionFind():
    def __init__(self, n):
        self.l = [0] * (n+1)
        for i in range(len(self.l)):
            self.l[i] = i
    def join(self, a, b):
        aa = self.find(a)
        bb = self.find(b)
        if aa == bb:
            return
        self.l[aa] = bb

    def find(self, a):
        aa = self.l[a]
        if aa != a:
            self.l[aa] = self.find(aa)

        return self.l[aa]      