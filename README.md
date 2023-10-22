# Genetic-Algorithm
Here we are solving the 8 puzzle problem using a genetic algorithm. Using heuristic - (1): Manhattan distance (2): Number of misplaced tiles

Simulated Annealing is a probabilistic optimization algorithm widely used for finding a good approximation to the global optimum of a complex problem. Its effectiveness is influenced by several key factors:

1. **Initial Solution:** The starting point significantly impacts how quickly the algorithm converges and the quality of the final solution. A good initial solution promotes faster convergence and better outcomes, but random initial solutions are used when no suitable starting point is available.

2. **Objective Function:** The objective function, representing the problem's characteristics and constraints, must accurately evaluate solutions. It guides the algorithm toward optimal solutions.

3. **Neighbor Generation:** Efficient generation of neighboring solutions is vital. The balance between exploration and exploitation during solution space traversal is crucial. Poor neighbor generation methods might trap the algorithm in local optima.

4. **Temperature Schedule:** The cooling schedule, determining how temperature decreases, is pivotal. It allows exploration at higher temperatures and exploitation at lower temperatures, affecting convergence. Proper cooling rates are essential for effective exploration and exploitation.

5. **Acceptance Probability:** The heuristic used to accept worse solutions affects the exploration-exploitation trade-off. Methods like the Metropolis criterion influence how the algorithm explores the solution space by considering cost differences and current temperature.

6. **Stopping Criteria:** Determining when to stop the algorithm is critical. Appropriate criteria prevent excessive resource usage. Common approaches include reaching a predefined temperature or running a set number of iterations.

7. **Temperature Initialization:** The initial temperature impacts convergence speed. Too high a temperature might lead to slow convergence due to accepting many worse solutions, while too low a temperature might trap the algorithm in local optima.

8. **Randomization:** Simulated Annealing uses randomness. Random factors, such as initial solutions and accepting worse solutions, influence the algorithm's behavior and diversity of explored solutions.

Considering and fine-tuning these factors is essential for the successful application of Simulated Annealing to various optimization problems.

By comparing the two heuristics provided (h1 and h2) for a simulated annealing, the heuristic h2 (Total Manhattan Distance) is likely to perform better. This is because h2 provides a more accurate estimate of the distance of the current state from the goal state, and simulated annealing benefits from having a more informative heuristic to  guide the search. Sometimes performance is also varying depending on the problem instance, the implementation of the simulated annealing algorithm, and the parameters used such as the cooling schedule and initial temperature. 
