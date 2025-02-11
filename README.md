# A* Alphabet: Pathfinding Through Letters

## Overview

**A* Alphabet** is an implementation of the **A* search algorithm** applied to a graph where nodes represent letters of the alphabet. The goal is to find the optimal path from a starting letter to a target letter, leveraging heuristic functions to guide the search efficiently.

A* (A-star) is a best-first search algorithm that finds the shortest path in a weighted graph using a combination of:

\[ f(n) = g(n) + h(n) \]

where:
- **g(n)** is the cost from the start node to the current node.
- **h(n)** is the heuristic estimate of the cost from the current node to the goal.
- **f(n)** is the total estimated cost of the cheapest path.

This project explores different heuristic choices and path structures to optimize traversal through the alphabet.

## Features

- **Graph-Based Alphabet Representation**: Models the alphabet as a connected graph with custom edge weights.
- **Multiple Heuristic Functions**:
  - Euclidean Distance
  - Manhattan Distance
  - Custom Letter-Based Distance Functions
- **Dynamic Path Visualization**: Provides insights into A*'s decision-making process.
- **Customizable Parameters**: Modify heuristics and node connections for experimentation.

## Installation

Ensure you have **Python 3.7+** installed.

```bash
# Clone the repository
git clone https://github.com/kirillsimin/astar_alphabet.git
cd astar_alphabet

# Install dependencies
pip install -r requirements.txt
```

## Usage

Run the script with the default configuration:
```bash
python main.py
```

Or specify custom parameters:
```bash
python main.py --start A --goal Z --heuristic manhattan
```

### Command-Line Arguments

| Argument         | Description                                     | Default |
|-----------------|-------------------------------------------------|---------|
| `--start`       | Starting letter for pathfinding                | `A`     |
| `--goal`        | Target letter                                  | `Z`     |
| `--heuristic`   | Heuristic function (`euclidean`, `manhattan`) | `euclidean` |
| `--verbose`     | Enable detailed output                         | `False`  |

## Algorithm Implementation

The **A* search** operates as follows:

1. Initialize the **open list** with the starting node.
2. Maintain a **closed list** to track visited nodes.
3. Iterate until the goal is reached or the open list is empty:
   - Select the node with the lowest `f(n) = g(n) + h(n)`.
   - Expand its neighbors and compute their tentative costs.
   - Update paths if a better route is found.
   - Repeat until the target node is reached.

### Graph Representation

Each letter is treated as a **graph node**. The adjacency rules can be customized, but the default setup assumes:

- Letters are **connected sequentially** (`A → B → C ... → Z`).
- Bi-directional edges with a base weight of **1**.
- Additional graph structures can be introduced (e.g., diagonal movements).

### Heuristic Functions

| Heuristic   | Formula | Usage |
|-------------|---------------------------------------------------------|--------------------------|
| Euclidean   | \[ h(n) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} \] | Straight-line distance |
| Manhattan   | \[ h(n) = |x_2 - x_1| + |y_2 - y_1| \] | Grid-based movement |
| Custom      | Letter distance based on ASCII values | Experimental |

## Example Output

```
Starting A* search from A to Z using Euclidean heuristic...
Expanded nodes: 15
Optimal path found: A → C → F → K → M → Z
Total cost: 9.8
```

## Performance Considerations

- **Time Complexity**: Worst-case **O(|E| + |V| log |V|)**, where `V` is nodes and `E` is edges.
- **Memory Usage**: Proportional to the size of the open and closed lists.
- **Heuristic Choice**: Manhattan is better suited for grid-like graphs, while Euclidean works for continuous spaces.
