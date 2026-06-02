class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0
        
        # min_dist[i] 表示点 i 到当前最小生成树的最短距离
        min_dist = [float('inf')] * n
        # 记录点是否已经加入了最小生成树
        in_mst = [False] * n
        
        # 从第 0 个点开始构建
        min_dist[0] = 0
        total_cost = 0
        
        # 每次循环加入一个点，总共需要加入 n 个点
        for _ in range(n):
            # 1. 寻找当前未加入 MST 且距离树最近的点 u
            u = -1
            for i in range(n):
                if not in_mst[i] and (u == -1 or min_dist[i] < min_dist[u]):
                    u = i
            
            # 将点 u 加入 MST，并累加权重
            in_mst[u] = True
            total_cost += min_dist[u]
            
            # 2. 用刚刚加入的点 u 去更新其它未加入点到 MST 的最短距离
            for v in range(n):
                if not in_mst[v]:
                    # 动态计算点 u 和点 v 之间的曼哈顿距离（相当于邻接矩阵的边权）
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if dist < min_dist[v]:
                        min_dist[v] = dist
                        
        return total_cost