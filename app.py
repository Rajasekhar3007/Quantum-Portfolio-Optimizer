import streamlit as st
import numpy as np
from data import get_data
from qubo import build_qubo
from qaoa_solver import solve_qaoa
from classical_solver import solve_classical
import matplotlib.pyplot as plt

st.set_page_config(page_title="Quantum Portfolio Optimizer", layout="centered")

st.title("🚀 Quantum Portfolio Optimizer")
st.write("Compare Quantum vs Classical Portfolio Optimization")

# Button to run
if st.button("Run Optimization"):

    with st.spinner("Fetching Data & Running Models..."):
        mean_returns, cov_matrix = get_data()
        qubo = build_qubo(mean_returns, cov_matrix)

        quantum_result = solve_qaoa(qubo)
        classical_result = solve_classical(cov_matrix)

    st.success("Optimization Complete!")

    # Show results
    st.subheader("⚛️ Quantum Result")
    st.write(quantum_result)

    st.subheader("📊 Classical Result")
    st.write(classical_result)

    # Plot comparison
    st.subheader("📈 Comparison Graph")

    fig, ax = plt.subplots()
    ax.bar(range(len(quantum_result)), quantum_result, alpha=0.6, label="Quantum")
    ax.bar(range(len(classical_result)), classical_result, alpha=0.6, label="Classical")
    ax.legend()
    ax.set_title("Portfolio Comparison")

    st.pyplot(fig)
