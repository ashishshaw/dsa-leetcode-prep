#Approach: We can use Kahn's algorithm for topological sorting. 
# We first build a graph representation of the courses and their prerequisites. 
# We also maintain an indegree array to keep track of the number of prerequisites for each course. 
# We then use a queue to process courses with no prerequisites (indegree of 0). 
# We repeatedly remove courses from the queue, add them to the order, and decrease the indegree of their dependent courses. 
# If any dependent course's indegree becomes 0, we add it to the queue. 
# Finally, if we have processed all courses, we return the order; otherwise, we return an empty list indicating that it's not possible to complete all courses.

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        q = deque(i for i in range(numCourses) if indegree[i] == 0)
        order = []

        while q:
            course = q.popleft()
            order.append(course)

            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return order if len(order) == numCourses else []
        