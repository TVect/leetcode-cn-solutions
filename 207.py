"""
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]

给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

示例 1:

输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。

示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
 

提示：

输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
1 <= numCourses <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 深度优先
    def canFinish_1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0: 未检测. 1: 正在检测. 2: 检测完成
        status = [0] * numCourses
        course_requisites = {}
        for item in prerequisites:
            if item[0] not in course_requisites:
                course_requisites[item[0]] = []
            course_requisites[item[0]].append(item[1])

        def dfs(course_id):
            status[course_id] = 1
            for require_course in course_requisites.get(course_id, []):
                if status[require_course] == 1:
                    return False
                elif status[require_course] == 0:
                    if not dfs(require_course):
                        return False
            status[course_id] = 2
            return True

        for course_id in range(numCourses):
            if status[course_id] == 0:
                res = dfs(course_id)
                if not res:
                    return False
        return True

    # 广度优先，从入度为 0 的节点开始加入队列
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        post_courses = {}    # 某个 course 被其他哪些 course 直接依赖
        in_degree = [0] * numCourses    # 某个 course 依赖于几个其他的 course
        for item in prerequisites:
            if item[1] not in post_courses:
                post_courses[item[1]] = []
            post_courses[item[1]].append(item[0])
            in_degree[item[0]] += 1

        visited = 0
        course_queue = [course_id for course_id in range(numCourses) if in_degree[course_id] == 0]
        while len(course_queue):
            visited += 1
            course_id = course_queue.pop(0)
            for post_course in post_courses.get(course_id, []):
                in_degree[post_course] -= 1
                if in_degree[post_course] == 0:
                    course_queue.append(post_course)
        return visited == numCourses


numCourses = 2
prerequisites = [[1, 0], [0, 1]]

numCourses = 2
prerequisites = [[0, 1]]

numCourses = 3
prerequisites = [[0, 2], [1, 2], [2, 0]]

print(Solution().canFinish(numCourses, prerequisites))
