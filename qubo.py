import numpy as np

def build_qubo(mean_returns, cov_matrix):
    lambda_risk = 0.5
    Q = cov_matrix.values
    qubo = lambda_risk * Q - np.diag(mean_returns)
    return qubo
