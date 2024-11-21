# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    frontier = util.Stack()
    visited = set()

    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's children:", problem.getSuccessors(problem.getStartState()))

    start_state = problem.getStartState()

    frontier.push((start_state, []))

    while not frontier.isEmpty():
        state, actions = frontier.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)
            for children, action, stepCost in problem.getSuccessors(state):
                if children not in visited:
                    frontier.push((children, actions + [action]))

    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    frontier = util.Queue()
    visited = set()

    start_state = problem.getStartState()
    frontier.push((start_state, []))

    while not frontier.isEmpty():
        state, actions = frontier.pop()

        if problem.isGoalState(state):
            # count = 0
            #
            # for action in actions:
            #     count += 1
            #
            # print("Number of actions:", count)
            return actions

        if state not in visited:
            visited.add(state)
            for children, action, stepCost in problem.getSuccessors(state):
                if children not in visited:
                    frontier.push((children, actions + [action]))

    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()
    visited = set()

    # print("Start:", problem.getStartState())
    # print("Start's children:", problem.getSuccessors(problem.getStartState()))

    start_state = problem.getStartState()
    frontier.push((start_state, []), 0)

    while not frontier.isEmpty():
        state, actions = frontier.pop()

        if problem.isGoalState(state):
            # count = 0
            #
            # for action in actions:
            #     count += 1
            #
            # print("Number of actions:", count)
            return actions

        if state not in visited:
            visited.add(state)
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    frontier.push((successor, actions + [action]),
                                  problem.getCostOfActions(actions + [action]))

    return []


def nullHeuristic(state, problem = None):
    """
    # A heuristic function estimates the cost from the current state to the nearest
    # goal in the provided SearchProblem.  This heuristic is trivial.
    # """
    # goal_pos = problem.goals
    #
    # if state == goal_pos:
    #     return 0
    #
    # curr_pos = state
    #
    # # Manhattan distance
    # heuristic_cost = abs(curr_pos[0] - goal_pos[0]) + abs(curr_pos[1] - goal_pos[1])

    return 0;


def aStarSearch(problem, heuristic=nullHeuristic):
    "*** YOUR CODE HERE ***"
    # start = problem.getStartState()
    # visited = []
    # frontier = util.PriorityQueue()
    # f_value = 0 + (heuristic(start, problem) or 0)
    # frontier.push((start, [], 0), f_value)
    #
    # while not frontier.isEmpty():

    frontier = util.PriorityQueue()
    visited = set()

    start = problem.getStartState()

    frontier.push((start, [], 0), 0)

    while not frontier.isEmpty():
        state, actions, priority = frontier.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)
            for successor in problem.getSuccessors(state):
                new_state = successor[0]
                new_action = successor[1]
                f_value = successor[2] + priority + heuristic(new_state, problem)
                frontier.push((new_state, actions + [new_action], successor[2] + priority),
                              f_value)

    return []


    # frontier = util.PriorityQueue()
    # start = [problem.getStartState(), 0, []]
    # frontier.push(start, 0) # f_value = cost + heuristic
    # closed = list()
    #
    # while not frontier.isEmpty():
    #     [state, cost, path] = frontier.pop()
    #
    #     if problem.isGoalState(state):
    #         return path
    #
    #     if state not in closed:
    #         closed.append(state)
    #         for child_state, actions, c in problem.getSuccessors(state):
    #             new_cost = c + problem.getCostOfActions(actions)
    #             new_path = path + [actions]
    #             new_f = new_cost + (heuristic(child_state, problem) or 0)
    #             frontier.push([child_state, new_cost, new_path], new_f)
    #             print("path:", new_path)
    # util.raiseNotDefined()

    # print("Start:", start)
    # print("Start's children:", problem.getSuccessors(start))
    # print("Start's heuristic:", heuristic(start, problem) or 0)
    # print("Start's cost:", problem.getCostOfActions([]))
    # print("Start's f_value:", f_value)
    #
    # print(problem.isGoalState(start))#
    #
    # while not frontier.isEmpty():
    #     state, actions, cost = frontier.pop()
    #     print("State:", state)
    #     print("Actions:", actions)
    #     print("Cost:", cost)
    #     print("Is goal state:", problem.isGoalState(state))
    #     print("Successors:", problem.getSuccessors(state))
    #     print("Heuristic:", heuristic(state, problem) or 0)
    #     print("Cost of actions:", problem.getCostOfActions(actions))
    #     print("f_value:", cost + (heuristic(state, problem) or 0))
    #     print("Visited:", visited)
    #     print("Frontier:", frontier.heap)
    #     print("Frontier length:", len(frontier.heap))



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
