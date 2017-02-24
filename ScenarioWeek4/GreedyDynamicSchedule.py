from ScenarioWeek4 import *

rob = robots()
number_of_robots = len(rob)

polygons = polygon()

print("number of robots: {number_of_robots}".format(number_of_robots=number_of_robots))

infinity = 1000000000000000000

from ScenarioWeek4 import AStar

modifiedEdges = {}


class Robot:
    def __init__(self, x, y, status):
        self.x = x
        self.y = y
        self.status = status
        self.closest = -1
        self.distanceAcquiredSinceLastJump = 0
        self.remainingDistance = infinity
        self.intermediatePoints = [[x, y]]
        self.jParam = 0
        self.closestNeighbours = []


def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def new_distance(route):
    total_distance = 0
    for i in range(0, len(route) - 1):
        total_distance += distance(route[i], route[i + 1])
    return total_distance


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

    a = AStar.Node(firstRobot.x, firstRobot.y)
    b = AStar.Node(secondRobot.x, secondRobot.y)

    # print((a.x, a.y, b.x, b.y))

    # foreach shape
    # for shape in shapeList:
    #     for i in range(-1, len(shape) - 1):
    #         e1, e2 = Coordinate(False, shape[i][0], shape[i][1]), Coordinate(False, shape[i + 1][0], shape[i + 1][1])
    #         if intersect(firstRobotPosition, secondRobotPosition, e1, e2):
    #             # find distance
    route = AStar.a_star(a, b)
    modifiedEdges[(a.x, a.y, b.x, b.y)] = route
    return new_distance(route)

    # return math.sqrt(((firstRobot.x - secondRobot.x) * (firstRobot.x - secondRobot.x)) +
    #                  ((firstRobot.y - secondRobot.y) * (
    #                      firstRobot.y - secondRobot.y))) - firstRobot.distanceAcquiredSinceLastJump


def greedy_dynamic_schedule():
    r = []
    r.append(Robot(rob[0][0], rob[0][1], True))
    # make copy of robots
    for r1 in rob[1:]:
        r.append(Robot(r1[0], r1[1], False))

    targetList = []
    targetList.append([0, -1])
    counter = 0

    for i in range(0, number_of_robots):
        dist = infinity
        for j in range(0, number_of_robots):
            if i != j:
                d = shortestDistance(r[i], r[j], polygons)
                r[i].closestNeighbours.append((r[j], d))
                # if d < dist:
                #     r[j].jParam = j

        r[i].closestNeighbours.sort(key=lambda x: x[1])
#(0.0,1.0),(2.0,0.0),(3.0,2.0),(3.0,4.0),(3.0,5.0);(2.0,0.0),(9.0,0.0);(3.0,5.0),(8.0,1.0),(6.0,2.0);
#(0.0,1.0),(2.0,0.0),(9.0,0.0);(2.0,0.0),(3.0,2.0),(3.0,4.0),(3.0,5.0);(9.0,0.0),(8.0,1.0),(6.0,2.0);


    print("***()()()***")

    for x in range(1, number_of_robots):  # fill in target list
        print("{cu}: waiting...".format(cu=counter))

        for i in range(0, number_of_robots):

            if r[i].status:
                r[i].closest = -1
                r[i].remainingDistance = infinity
                for bot in r[i].closestNeighbours:
                    if bot[0].status is False:
                        d = bot[1] - r[i].distanceAcquiredSinceLastJump
                        if d < r[i].remainingDistance:
                            r[i].remainingDistance = d
                            r[i].closest = bot[0].jParam

        # for i in range(0, number_of_robots):  # calculate distance to nearest robots for all awake bots
        #     if r[i].status is True:
        #         r[i].closest = -1
        #         r[i].remainingDistance = infinity
        #         for j in range(0, number_of_robots):
        #             if not r[j].status:
        #                 d = shortestDistance(r[i], r[j], polygons) - r[i].distanceAcquiredSinceLastJump
        #                 # d = math.sqrt(
        #                 #     ((r[i].x - r[j].x) * (r[i].x - r[j].x)) + ((r[i].y - r[j].y) * (r[i].y - r[j].y))) - r[
        #                 #         i].distanceAcquiredSinceLastJump
        #                 if d < r[i].remainingDistance:
        #                     r[i].remainingDistance = d
        #                     r[i].closest = j

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
        counter += 1

    s = []

    for i in range(0, len(targetList)):
        s.append(targetList[i][1])

    return s


def constantSchedule():
    numSectors = 8
    dx, dy, k, d = 0, 0, 0, 0
    s = []
    r = []
    c = []

    for i in range(0, number_of_robots):
        c.append([])
        for k in range(0, numSectors):
            c[i].append([-1, infinity])

    # # make copy of robots
    r.append(Robot(rob[0][0], rob[0][1], True))
    for r1 in rob[1:]:
        r.append(Robot(r1[0], r1[1], False))

    for i in range(0, number_of_robots):
        for j in range(0, number_of_robots):
            if i != j:
                dx = r[j].x - r[i].x
                dy = r[j].y - r[i].y
                k = 0
                if dx < 0:
                    k += 4
                if dy < 0:
                    k += 2
                if math.fabs(dx) < math.fabs(dy):
                    k += 1
                if c[i][k][0] == -1 or d < c[i][k][1]:
                    c[i][k][0] = j
                    c[i][k][1] = d

    targetList = []
    targetList.append([0, -1])

    for x in range(number_of_robots):
        nextRobot = -1
        target = -1
        minDist = infinity

        for i in range(number_of_robots):
            if r[i].status is True:
                for k in range(numSectors):
                    v = c[i][k][0]
                    if v > -1:
                        if r[v].status is True:
                            c[i][k][0] = -1
                            c[i][k][1] = infinity
                            # sorted([('abc', 121),('abc', 231),('abc', 148), ('abc',221)], key=lambda x: x[1])

                sorted(c[i], key=lambda x: x[1])
                t = c[i][0][0]
                if t == -1:
                    r[i].status = False
                if r[i].status is True:
                    dx = r[t].x - r[i].x
                    dy = r[t].y - r[i].y

                    print([r[t].x, r[i].x])
                    print([r[t].y, r[i].y])

                    d = shortestDistance(r[i], r[t], polygons) - r[i].d
                    if d < minDist:
                        nextRobot = i
                        target = t
                        minDist = d

        for i in range(number_of_robots):
            if r[i].status is True:
                r[i].d += minDist

        r[nextRobot].d = 0
        r[nextRobot].x = r[target].x
        r[nextRobot].y = r[target].y
        r[target].status = True

        targetList.append([min(nextRobot, target), -1])
        targetList.append([max(nextRobot, target), -1])
        updated = False

        for i in range(0, len(targetList)):
            if targetList[i][0] == nextRobot and targetList[i][1] == -1 and updated is False:
                targetList[i][1] = target
                updated = True
    for i in range(len(targetList)):
        s.append(targetList[i][1])
    return s


def start():
    print("starting")
    # schedule = constantSchedule()
    schedule = greedy_dynamic_schedule()
    # print(schedule)
    # print(rob[1:])

    idleRobots = []

    for r1 in rob:
        idleRobots.append(Robot(r1[0], r1[1], False))

    idleRobots[0].status = True

    while schedule is not []:

        if schedule == []:
            break

        num, counter = 0, 0
        for robotx in idleRobots:
            if robotx.status:
                num += 1

        for robotX in idleRobots:

            if schedule == []:
                break

            if robotX.status is True:

                if counter >= num:
                    break

                counter += 1

                if schedule[0] == -1:
                    robotX.status = False
                    # print("stopping robot: {x}, {y} : status: {s}".format(x=robotX.x,
                    #                                                       y=robotX.y,
                    #                                                       s=robotX.status))

                else:
                    robotX.intermediatePoints.append(rob[schedule[0]])
                    idleRobots[schedule[0]].status = True
                    # print("starting robot: {x}, {y} : status: {s}".format(x=idleRobots[schedule[0]].x,
                    #                                                       y=idleRobots[schedule[0]].y,
                    #                                                       s=idleRobots[schedule[0]].status))
                schedule.remove(schedule[0])
                # print("*****_____*****")

    print("------")

    # for edges in modifiedEdges:
    #     print("{edges}: {md}".format(edges=edges, md=modifiedEdges[edges]))

    for bot in idleRobots:
        for i in range(0, len(bot.intermediatePoints)-1):
            a = (bot.intermediatePoints[i][0], bot.intermediatePoints[i][1], bot.intermediatePoints[i + 1][0],
                 bot.intermediatePoints[i + 1][1])
            if a in modifiedEdges:
                counter = 1
                for j in range(i, len(modifiedEdges[a])):

                    if counter == len(modifiedEdges[a]):
                        break

                    bot.intermediatePoints.insert(j, [modifiedEdges[a][counter][0], modifiedEdges[a][counter][1]])
                    counter += 1

    outputString = ""
    for bott in idleRobots:
        if len(bott.intermediatePoints) <= 1:
            pass
        else:
            for interPoint in bott.intermediatePoints:
                if interPoint == bott.intermediatePoints[-1]:
                    outputString += "({x},{y})".format(x=float(interPoint[0]), y=float(interPoint[1]))
                else:
                    outputString += "({x},{y}),".format(x=float(interPoint[0]), y=float(interPoint[1]))
            outputString += ";"

    print(outputString)
