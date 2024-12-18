Summary of the Project
1. Overview of Stochastic Programming
Definition: Stochastic Programming involves decision variables (controlled by decision-makers) and random variables (representing uncertainties such as demand, price, or weather).
The goal is to optimize decision variables by considering possible scenarios of random variables.
Applications: Widely used in finance, transportation, energy optimization, etc.
2. Approach
1-SLP (One-Stage Stochastic Linear Programming): Optimization is based on probabilistic constraints and predefined random scenarios.
2-SLP (Two-Stage Stochastic Linear Programming):
Stage 1: Make initial decisions before the realization of random variables.
Stage 2: Adjust decisions based on observed information after uncertainty is resolved.
3. Problem 1: Production Planning
Model:
Stage 1: Determine the quantity of raw materials to pre-order.
Stage 2: Adjust production based on actual market demand.
Objective: Minimize pre-order and production costs while maximizing profits.
Solution Tools: Python with the Gamspy library, leveraging linear programming optimization techniques.
4. Problem 2: Evacuation Planning
Objective: Identify the optimal routes for evacuating people during disasters.
Model:
Stage 1: Create an initial evacuation plan based on available paths.
Stage 2: Adjust the plan considering real-time conditions, such as changing road capacities or travel times.
Solution Method:
Use Lagrangian relaxation to decompose the problem into smaller subproblems.
Apply the Successive Shortest Path algorithm to find the minimum-cost flow for evacuation routes.
5. Conclusion
Both problems employ stochastic programming to optimize decision-making in uncertain environments.
The methods and tools used demonstrate effectiveness in addressing real-world challenges, such as industrial production and disaster response.
