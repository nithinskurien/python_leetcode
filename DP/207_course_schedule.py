# 207. Course Schedule
#
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array
# prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take
# course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
#
#
#
# Example 1:
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]] Output: false Explanation: There are a total of 2 courses to
# take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course
# 1. So it is impossible.
#
#
# Constraints:
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
#
# Logic:
# We want to check if there are loops to a course as if that is the case we cannot satisfy the prerequisites. We will
# initially build a dict where a course has its prerequisites in a list. Then for each course we will check if a loop is
# present by initialising a set with seen courses and add the course to it. We will then go to the prereq of the courses
# and recursively call the same loop function and add those prereq to the seen set and if we encounter a course we have
# previously seen we will return. We can after checking if a course can be taken we can initialise the prereq list to
# empty so that for other courses we do not need to go through the child of this course as we have already verified that
# this course can be taken. If we go through all the courses and do not find any loops we can return with true.


from collections import defaultdict


class Solution:

    def __init__(self):
        self.seen = None
        self.coursesDict = None

    def loopPresent(self, course: int) -> bool:
        if course in self.seen:
            return True
        self.seen.add(course)
        for prereq in self.coursesDict[course]:
            if self.loopPresent(prereq):
                return True
        self.coursesDict[course] = []
        self.seen.remove(course)
        return False

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        self.coursesDict = defaultdict(list)
        self.seen = set()
        for course, prereq in prerequisites:
            self.coursesDict[course].append(prereq)
        for course in range(numCourses):
            if self.loopPresent(course):
                return False
        return True
