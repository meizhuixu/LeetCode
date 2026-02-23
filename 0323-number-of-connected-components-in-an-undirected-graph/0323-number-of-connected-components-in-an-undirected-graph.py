# add count to record the number of components
# initiate count as the number of nodes
# whenever join two nodes(edge), count - 1
# after join all the nodes by edges, return count
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]  # idx: node  val: its parent
        self.count = n
        
    def find(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
        
    def isSame(self, u, v):  # No need here
        u = self.find(u)
        v = self.find(v)
        return u == v
        
    def join(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        self.parent[u] = v
        self.count -= 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.join(u, v)
        return uf.count
            
        
        