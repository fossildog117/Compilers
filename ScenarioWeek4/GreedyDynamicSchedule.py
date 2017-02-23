from ScenarioWeek4 import *

rob = robots()
number_of_robots = len(rob)

polygons = polygon()

print("number of robots: {number_of_robots}".format(number_of_robots=number_of_robots))

infinity = 1000000000000000000

class Robot:

    def __init__(self, x, y, status, isRobot):
        self.x = x
        self.y = y
        self.status = status
        self.closest = -1
        self.distanceAcquiredSinceLastJump = 0
        self.remainingDistance = infinity
        self.intermediatePoints = [[x, y]]
        self.isRobot = isRobot


def shortestDistance(firstRobot, secondRobot, shapeList):
    """
    :param firstRobot:
    :param secondRobot:
    :param shapeList:
    :return: float
    """

    firstRobotPosition, secondRobotPosition = Coordinate(True, firstRobot.x, firstRobot.y), Coordinate(True,
                                                                                                       secondRobot.x,
                                                                                                       secondRobot.y)
    # foreach shape
    for shape in shapeList:
        for i in range(-1, len(shape) - 1):
            e1, e2 = Coordinate(False, shape[i][0], shape[i][1]), Coordinate(False, shape[i + 1][0], shape[i + 1][1])
            if intersect(firstRobotPosition, secondRobotPosition, e1, e2):
                # find distance
                print("intersection")


    return math.sqrt( ((firstRobot.x - secondRobot.x) * (firstRobot.x - secondRobot.x)) +
                      ((firstRobot.y - secondRobot.y) * (firstRobot.y - secondRobot.y))) - firstRobot.distanceAcquiredSinceLastJump


def greedy_dynamic_schedule():
    r = []
    r.append(Robot(rob[0][0], rob[0][1], True))
    # make copy of robots
    for r1 in rob[1:]:
        r.append(Robot(r1[0], r1[1], False))

    targetList = []
    targetList.append([0, -1])

    for x in range(1, number_of_robots):  # fill in target list
        for i in range(0, number_of_robots):  # calculate distance to nearest robots for all awake bots
            if r[i].status:
                r[i].closest = -1
                r[i].remainingDistance = infinity

                for j in range(0, number_of_robots):
                    if not r[j].status:
                        d = math.sqrt(
                            ((r[i].x - r[j].x) * (r[i].x - r[j].x)) + ((r[i].y - r[j].y) * (r[i].y - r[j].y))) - r[
                                i].distanceAcquiredSinceLastJump
                        if d < r[i].remainingDistance:
                            r[i].remainingDistance = d
                            r[i].closest = j

        # see which robot will reach target first
        nextRobotToReachTarget = -1
        d = infinity

        for i in range(0, number_of_robots):
            if r[i].status and r[i].remainingDistance < d:
                d = r[i].remainingDistance
                nextRobotToReachTarget = i

        if d == infinity:
            break

        # update acquired distance for all awake robots
        for i in range(0, number_of_robots):
            if r[i].status:
                r[i].distanceAcquiredSinceLastJump += d

        # reset robot that made jump
        r[nextRobotToReachTarget].distanceAcquiredSinceLastJump = 0
        r[nextRobotToReachTarget].x = r[r[nextRobotToReachTarget].closest].x
        r[nextRobotToReachTarget].y = r[r[nextRobotToReachTarget].closest].y

        # add the two robots to target list in numerical order
        if r[nextRobotToReachTarget].closest < nextRobotToReachTarget:
            targetList.append([r[nextRobotToReachTarget].closest, -1])
            targetList.append([nextRobotToReachTarget, -1])
        else:
            targetList.append([nextRobotToReachTarget, -1])
            targetList.append([r[nextRobotToReachTarget].closest, -1])

        # update newly awakened robot
        r[r[nextRobotToReachTarget].closest].status = True

        # update target list
        updated = False
        for i in range(0, len(targetList)):
            if targetList[i][0] == nextRobotToReachTarget and targetList[i][1] == -1 and updated is False:
                targetList[i][1] = r[nextRobotToReachTarget].closest
                updated = True

    s = []

    for i in range(0, len(targetList)):
        s.append(targetList[i][1])

    return s


# schedule = greedy_dynamic_schedule()
# # print(schedule)
# # print(rob[1:])
#
# idleRobots = []

# for r1 in rob:
#     idleRobots.append(Robot(r1[0], r1[1], False))
#
# idleRobots[0].status = True
#
# while schedule is not []:
#
#     if schedule == []:
#         break
#
#     num, counter = 0, 0
#     for robotx in idleRobots:
#         if robotx.status:
#             num += 1
#
#     for robotX in idleRobots:
#
#         if schedule == []:
#             break
#
#         if robotX.status is True:
#
#             if counter >= num:
#                 break
#
#             counter += 1
#
#             if schedule[0] == -1:
#                 robotX.status = False
#                 # print("stopping robot: {x}, {y} : status: {s}".format(x=robotX.x,
#                 #                                                       y=robotX.y,
#                 #                                                       s=robotX.status))
#
#             else:
#                 robotX.intermediatePoints.append(rob[schedule[0]])
#                 idleRobots[schedule[0]].status = True
#                 # print("starting robot: {x}, {y} : status: {s}".format(x=idleRobots[schedule[0]].x,
#                 #                                                       y=idleRobots[schedule[0]].y,
#                 #                                                       s=idleRobots[schedule[0]].status))
#             schedule.remove(schedule[0])
#     print("*****_____*****")
#
# print("------")
# outputString = ""
# for bott in idleRobots:
#     if len(bott.intermediatePoints) <= 1:
#         pass
#     else:
#         for interPoint in bott.intermediatePoints:
#             if interPoint == bott.intermediatePoints[-1]:
#                 outputString += "({x},{y})".format(x=interPoint[0], y=interPoint[1])
#             else:
#                 outputString += "({x},{y}),".format(x=interPoint[0], y=interPoint[1])
#         outputString += ";"
#
#
# print(outputString)