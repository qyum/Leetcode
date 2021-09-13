#Generalizable DFS + Graph Coloring 

class Solution:
    def __init__(self):
        self.result=[]
        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        WHITE, GREY, BLACK = 0, 1, 2 # White: Never Visited, Grey: Currently visting in DFS Path, Black: DFS concluded as a valid node (i.e no loops)
        graph, colors = {}, {}
        
        for i in range(numCourses):
            graph[i] = []
            colors[i] = WHITE # Set all nodes to never visited
        
        for x, y in prerequisites:
            graph[x].append(y)
            
        def dfs(node):
            if colors[node] == BLACK: return True # Node has been visted previously. Exit with Success
            if colors[node] == GREY: return False # Node is currently being visited in a DFS search oper
            colors[node] = GREY # Set node as currently visiting
            for child in graph[node]:
                if not dfs(child): return False # DFS search on all children to make sure no loops in child paths 
            colors[node] = BLACK
            if node not in self.result:
                self.result.append(node) # If not added as part of a different search path, add now.
            return True
        
        for node in graph:
            if graph[node]:
                if not dfs(node): return [] # Short circuit as failure if loop found in DFS
            else:
                if node not in self.result: # Check if node has already been added in a previous DFS search
                    self.result.append(node)
            
        return self.result
