import numpy as np
from scipy.optimize import minimize

def solve_classical(cov_matrix):
    n = len(cov_matrix)

    def risk(weights):
        return weights.T @ cov_matrix @ weights

    constraints = ({'type': 'eq', 'fun': lambda w: sum(w)-1})
    bounds = [(0,1)]*n

    initial = np.ones(n)/n

    result = minimize(risk, initial, bounds=bounds, constraints=constraints)
    return result.x
