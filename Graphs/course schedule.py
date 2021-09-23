'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

TC : O(V+E) where V is the number of courses and E is the number of prerequisites.
'''


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        cycle=set()#will be used to detect cycles
        dic={i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            dic[i].append(j)
        stack=[]
        
        def dfs(course):
            if course in cycle: #if you encounter a node which is currently being visited or under visiting state
                return False
            if course in visited:# node is visited already
                return True
            
            cycle.add(course)
            for pre in dic[course]:
                if(dfs(pre)==False):
                    return False
            cycle.remove(course)
            visited.add(course)
            stack.append(course)
            
        for i in range(numCourses):
            if(dfs(i)==False):
                return []
        
        return stack
                
    