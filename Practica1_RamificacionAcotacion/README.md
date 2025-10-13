# 🧩 Practice 1 — Search Strategies: Branch and Bound

## 🧠 Overview

This first lab assignment aims to **implement and analyze different search strategies** on graphs, including:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- **Branch and Bound (Uniform Cost Search)**
- **Branch and Bound with Underestimation (A* Search)**

The problem domain used is the **Romania map**, a classic benchmark from *Artificial Intelligence: A Modern Approach (AIMA)*.

---

## ⚙️ Code Structure

src/
 ├── run.py         # Main execution script
 ├── search.py      # Search algorithms implementation
 ├── utils.py       # Supporting data structures and utilities
results/
 └── comparison.txt  # Experimental results

---

## 🧩 Implementation Details

### 1. PriorityQueue Class

In `utils.py`, a **PriorityQueue** class was implemented to handle node ordering based on cost or heuristic:

import operator

class PriorityQueue(Queue):
    def __init__(self, f=lambda x: x, lt=operator.lt):
        self.A = []
        self.f = f
        self.lt = lt

    def append(self, item):
        self.A.append(item)
        self.A.sort(key=self.f, reverse=True)

    def __len__(self):
        return len(self.A)

    def pop(self):
        return self.A.pop()

This ensures that nodes are always selected in order of increasing cost (`path_cost`), enabling optimal-path search.

---

### 2. Branch and Bound Algorithm

Implemented in `search.py`:

def branch_and_bound(problem):
    """Search strategy that always expands the lowest-cost node first."""
    return graph_search(problem, PriorityQueue(lambda node: node.path_cost))

This uses the same core `graph_search` function as BFS/DFS but with a **priority queue** instead of a FIFO or stack.

---

### 3. Enhanced `graph_search` Function

Modified to **return additional statistics** for better evaluation:

def graph_search(problem, fringe):
    closed = {}
    fringe.append(Node(problem.initial))
    generated, visited = 0, 0

    while fringe:
        node = fringe.pop()
        visited += 1
        if problem.goal_test(node.state):
            return node, generated, visited
        if node.state not in closed:
            closed[node.state] = True
            new_nodes = node.expand(problem)
            generated += len(new_nodes)
            fringe.extend(new_nodes)
    return None, generated, visited

This allows comparing algorithms by total generated and visited nodes.

---

### 4. Example Execution

In `run.py`:

import search

ab = search.GPSProblem('A', 'B', search.romania)

result, generated, visited = search.branch_and_bound(ab)
print("Path found:", [n.state for n in result.path()])
print("Total cost:", result.path_cost)
print(f"Nodes generated: {generated}, visited: {visited}")

---

## 📊 Experimental Results

| Search Strategy | Path | Total Cost | Generated Nodes | Visited Nodes |
|------------------|------|-------------|----------------|----------------|
| Breadth-First Search | A–S–R–P–B | 418 | 15 | 10 |
| Depth-First Search | A–S–F–B | 450 | 12 | 8 |
| Branch and Bound | A–S–R–P–B | 418 | 11 | 8 |
| Branch and Bound + Heuristic | A–S–R–P–B | 418 | 9 | 7 |

✅ **Observation:**  
All algorithms eventually reach the optimal path, but **Branch and Bound with heuristic (A\*)** achieves it more efficiently, generating and visiting fewer nodes.

---

## 🧾 Conclusions

- Uninformed strategies (BFS, DFS) find correct solutions but are computationally expensive.  
- Branch and Bound optimizes the exploration order by cost.  
- Adding a heuristic (A\*) greatly reduces search effort while maintaining optimality.  
- The code structure allows easy extension to other strategies (Greedy, Best-First, etc.).

---

## 👨‍💻 Author

**Raul Reguera Bravo**  
University of Salamanca / University of Las Palmas de Gran Canaria  
Course: *Fundamentals of Intelligent Systems*

