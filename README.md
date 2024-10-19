# Pacman Search Project

This project implements several search algorithms to control Pacman in a variety of mazes. The goal is to navigate Pacman efficiently through the maze using different search strategies, such as Depth-First Search (DFS), Breadth-First Search (BFS), Uniform-Cost Search (UCS), and A* search. These algorithms help Pacman find paths to reach food or escape ghosts.

## Table of Contents
- [Overview](#overview)
- [Implemented Algorithms](#implemented-algorithms)
- [How to Run the Project](#how-to-run-the-project)
- [Results](#results)
- [Files and Directories](#files-and-directories)
- [Autograder](#autograder)
- [Acknowledgments](#acknowledgments)

## Overview
In this project, Pacman is placed in various maze environments, where the task is to guide him to the goal (usually a piece of food or exit) using different search strategies. The project is designed to test and explore how these algorithms perform in different scenarios.

Pacman’s world is made up of walls, empty spaces, food, and sometimes ghosts. The search algorithms need to find the optimal or near-optimal paths in this world while navigating obstacles.

## Implemented Algorithms
This project includes the following search algorithms, all implemented in Python:
- **Depth-First Search (DFS)**: Explores the deepest nodes in the search tree first.
- **Breadth-First Search (BFS)**: Explores the shallowest nodes first, ensuring the shortest path.
- **Uniform-Cost Search (UCS)**: Expands the least-cost node first.
- **A Search (A\*)**: Combines UCS with a heuristic to improve search efficiency.
  
Each algorithm is implemented in the `search.py` file, and the agents controlling Pacman are in the `searchAgents.py` file.

## Results
The table below summarizes the performance of the A* search algorithm on _Eating all the dots_ for different maze layouts:

| Layout         | Search Nodes Expanded | Total Cost | Time Taken (seconds) |
| -------------- | --------------------- | ---------- | -------------------- |
| trickySearch   | 719                   | 60         | 7.9                  |
| tinySearch     | 911                   | 27         | 2.3                  |

You can reproduce these results by running the following commands:

```bash
python pacman.py -l trickySearch -p AStarFoodSearchAgent
 ```

```bash
python pacman.py -l tinySearch -p AStarFoodSearchAgent
```

## How to Run the Project
To run this project on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/lienertdemaeyer/Pacman-Search-Project
   ```

2. Navigate to the project directory:
   ```bash
   cd Pacman-Search-Project
   ```

3. Run Pacman with different search algorithms by using the following commands:

   ### Depth-First Search (DFS):
   Depth-First Search explores the deepest nodes in the search tree first.

   To run Pacman using DFS on the tinyMaze layout, run:
   ```bash
   python pacman.py -l tinyMaze -p SearchAgent -a fn=depthFirstSearch
   ```

   ### Breadth-First Search (BFS):
   Breadth-First Search explores the shallowest nodes first, ensuring the shortest path in terms of the number of steps.

   To run Pacman using BFS on the mediumMaze layout, run:
   ```bash
   python pacman.py -l mediumMaze -p SearchAgent -a fn=breadthFirstSearch
   ```

   ### Uniform-Cost Search (UCS):
   Uniform-Cost Search expands the least-cost node first, prioritizing paths with the smallest cost.

   To run Pacman using UCS on the bigMaze layout, run:
   ```bash
   python pacman.py -l bigMaze -p SearchAgent -a fn=uniformCostSearch
   ```

   ### A* Search (A*):
   A* search combines the cost of a path (like UCS) with a heuristic to estimate the remaining cost to the goal.

   To run Pacman using A* search on the bigMaze layout with the Manhattan distance heuristic, run:
   ```bash
   python pacman.py -l bigMaze -p SearchAgent -a fn=aStarSearch,heuristic=manhattanHeuristic
   ```

   You can experiment with different layouts and algorithms by changing the `-l` (layout) and `-a` (algorithm) arguments.

   ### Example Layouts:
   - **tinyMaze**: A small, simple maze.
   - **mediumMaze**: A slightly larger and more complex maze.
   - **bigMaze**: A large maze that requires more efficient search strategies.

   ### Example Algorithms:
   - **Depth-First Search**: `depthFirstSearch`
   - **Breadth-First Search**: `breadthFirstSearch`
   - **Uniform-Cost Search**: `uniformCostSearch`
   - **A\* Search**: `aStarSearch`

4. To check if your implementation is correct, you can run the autograder:
   ```bash
   python autograder.py
   ```
   This will run tests for each search algorithm to verify correctness and performance.

### What Each Command Does:
- **`python pacman.py`**: Runs the Pacman game.
- **`-l tinyMaze`**: Specifies the layout/maze Pacman will navigate.
- **`-p SearchAgent`**: Specifies the type of agent controlling Pacman. In this case, the `SearchAgent` which uses search algorithms.
- **`-a fn=depthFirstSearch`**: Specifies the search function to use (DFS, BFS, UCS, or A*).
  - For A*, you can also specify a **heuristic** (e.g., `manhattanHeuristic`), which helps estimate the cost to reach the goal.


## Files and Directories
- **`search.py`**: Contains the implementations of search algorithms.
- **`searchAgents.py`**: Contains the agents that use the search algorithms to control Pacman.
- **`pacman.py`**: The main file to run the game.
- **`autograder.py`**: Autograder for testing the correctness of your implementations.

## Autograder
To run the autograder and check if your implementations are correct, use:
```bash
python autograder.py
```

## Acknowledgments
This project was developed as part of the AI course at UC Berkeley. The Pacman AI projects were created by John DeNero and Dan Klein. Autograding was added by Brad Miller, Nick Hay, and Pieter Abbeel.
