# https://leetcode.com/problems/evaluate-division/
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build a directed graph with costs using our equations.
        # Nodes are variables, costs are the equation relationship.
        graph = defaultdict(list)
        for (v1, v2), cost in zip(equations, values):
            graph[v1].append((v2, cost))
            graph[v2].append((v1, 1 / cost))
        
        answers = []
        for v1, v2 in queries:
            if v1 not in graph or v2 not in graph:
                answers.append(-1.0)
                continue

            # Use BFS to find an answer to a query by computing product of costs.
            q = deque([(v1, 1)])
            seen = set()
            ans = -1.0
            while q:
                node, total_cost = q.popleft()
                seen.add(node)
                if node == v2:
                    ans = total_cost
                    break
                
                for neighbour, cost in graph[node]:
                    if neighbour in seen:
                        continue
                    q.append((neighbour, total_cost * cost))
            
            answers.append(ans)
                
        return answers
