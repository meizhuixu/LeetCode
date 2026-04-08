class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. 建图
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # 2. 初始化
        pq = [(0, k)]  # (当前累积时间, 当前节点)
        visited = {}   # 用字典存储 {节点: 最短时间}
        
        while pq:
            time, u = heapq.heappop(pq)
            
            # --- 核心填空逻辑 ---
            if u in visited:
                continue
            # 第一次弹出时，记录最短时间
            visited[u] = time
            
            # 遍历邻居
            if u in graph:
                for v, w in graph[u]:
                    if v not in visited:
                        heapq.heappush(pq, (time + w, v))
        
        # 3. 结果判断
        # 如果访问到的节点数等于 n，返回 visited 中最大的时间，否则返回 -1
        return max(visited.values()) if len(visited) == n else -1