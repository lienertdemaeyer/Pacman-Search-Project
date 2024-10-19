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
from game import Directions
from typing import List

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




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
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
    stack = util.Stack() 
    start_state = problem.getStartState()
    stack.push((start_state, []))  
    visited = set()  

    while not stack.isEmpty(): 
        state, path = stack.pop()
        if problem.isGoalState(state): 
            return path
        if state not in visited: 
            visited.add(state) 
            for successor_state, action, stepCost in problem.getSuccessors(state):
                if successor_state not in visited:  
                    stack.push((successor_state, path + [action]))

    return [] 

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    queue = util.Queue() 
    start_state = problem.getStartState()
    queue.push((start_state, []))  
    visited = set()  

    while not queue.isEmpty(): 
        state, path = queue.pop() 
        if problem.isGoalState(state): 
            return path
        if state not in visited: 
            visited.add(state) 
            for successor_state, action, stepCost in problem.getSuccessors(state):
                if successor_state not in visited: 
                    queue.push((successor_state, path + [action])) 
    return []


def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    priority_queue = util.PriorityQueue()
    start_state = problem.getStartState()
    priority_queue.push((start_state, [], 0), 0)
    path_cost = {}  
    path_cost[start_state] = 0

    while not priority_queue.isEmpty():
        state, path, current_cost = priority_queue.pop()
        if problem.isGoalState(state):
            return path
        for successor_state, action, stepCost in problem.getSuccessors(state):
            new_cost = current_cost + stepCost
            if successor_state not in path_cost or new_cost < path_cost[successor_state]:
                path_cost[successor_state] = new_cost
                priority_queue.push((successor_state, path + [action], new_cost), new_cost)
        for item in priority_queue.heap:
            print(item)
    return []



def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    priority_queue = util.PriorityQueue()
    start_state = problem.getStartState()
    start_cost = 0
    priority_queue.push((start_state, [], start_cost), start_cost + heuristic(start_state, problem))
    path_cost = {}
    path_cost[start_state] = 0

    while not priority_queue.isEmpty():
        state, path, current_cost = priority_queue.pop()
        if current_cost > path_cost.get(state, float('inf')):
            continue
        if problem.isGoalState(state):
            return path
        for successor_state, action, stepCost in problem.getSuccessors(state):
            new_cost = current_cost + stepCost
            if new_cost < path_cost.get(successor_state, float('inf')):
                path_cost[successor_state] = new_cost
                priority = new_cost + heuristic(successor_state, problem)
                priority_queue.push((successor_state, path + [action], new_cost), priority)

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
