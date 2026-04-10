import matplotlib.pyplot as plt

def plot_results(q, c):
    plt.bar(range(len(q)), q, alpha=0.6, label="Quantum")
    plt.bar(range(len(c)), c, alpha=0.6, label="Classical")
    plt.legend()
    plt.title("Portfolio Comparison")
    plt.show()
