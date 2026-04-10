from data import get_data
from qubo import build_qubo
from qaoa_solver import solve_qaoa
from classical_solver import solve_classical
from visualization import plot_results

print("Fetching stock data...")
mean_returns, cov_matrix = get_data()

print("Building QUBO model...")
qubo = build_qubo(mean_returns, cov_matrix)

print("Running Quantum Optimization (QAOA)...")
quantum_result = solve_qaoa(qubo)

print("Running Classical Optimization...")
classical_result = solve_classical(cov_matrix)

print("\n--- RESULTS ---")
print("Quantum:", quantum_result)
print("Classical:", classical_result)

plot_results(quantum_result, classical_result)
