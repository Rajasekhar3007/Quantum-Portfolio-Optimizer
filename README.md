# 🚀 Quantum Portfolio Optimization

An interactive **quantum-inspired portfolio optimization system** built using Qiskit and Streamlit.
This project demonstrates how quantum computing concepts can be applied to financial decision-making by comparing quantum-based solutions with classical optimization.

---

## 📌 Features

* ⚛️ Quantum-inspired portfolio selection using quantum circuits
* 📊 Classical portfolio optimization for comparison
* 📈 Interactive visualization of results
* 🌐 Web app interface using Streamlit
* 📉 Real-world financial data using Yahoo Finance

---

## 🧠 Project Overview

Portfolio optimization is a fundamental problem in finance.

This project combines:

* **Quantum-inspired approach** (superposition & probabilistic sampling)
* **Classical optimization** (baseline comparison)

The goal is to explore how quantum computing techniques can assist in solving real-world optimization problems.

---

## 🏗️ Tech Stack

* Python
* Qiskit
* Streamlit
* NumPy
* Pandas
* Matplotlib
* yFinance

---

## 📂 Project Structure

quantum-portfolio/
│── app.py                # Streamlit UI
│── main.py               # Runs full pipeline
│── data.py               # Fetch stock data
│── qubo.py               # Build optimization model
│── qaoa_solver.py        # Quantum-inspired solver
│── classical_solver.py   # Classical optimization
│── requirements.txt

---

## ⚙️ Installation

```bash
# Clone repository
git clone https://github.com/Rajasekhar3007/quantum-portfolio.git
cd quantum-portfolio

# Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Run Python Script

```bash
python main.py
```

### Run Web App

```bash
streamlit run app.py
```

---

## 📊 Sample Output

Quantum Result: [1 0 0 0]
Classical Result: [0.25 0.25 0.25 0.25]

Graph visualization compares both approaches.

---

## 📸 Screenshots

Add screenshots in a folder like:

screenshots/ui.png
screenshots/graph.png

Then include:

```markdown
![UI](screenshots/ui.png)
![Graph](screenshots/graph.png)
```

---

## 🚀 Future Improvements

* Implement full QAOA algorithm
* Run on real quantum hardware (IBM Quantum)
* Add advanced portfolio constraints
* Integrate machine learning models

---

## 💼 Resume Description

Quantum Portfolio Optimization (Interactive Web App)

* Built a quantum-inspired optimization system using Qiskit for portfolio selection
* Developed an interactive Streamlit app to visualize quantum vs classical results
* Designed hybrid workflows combining financial data with quantum simulation

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and improve.

---

