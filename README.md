

### Core Applications:
- **Exotic Pricing:** Accurate valuation of path-dependent options (Barriers, Asians).
- **Risk Management:** Generation of model-consistent Greeks ($\Delta$, $\Gamma$, $\nu$).
- **Calibration:** Fitting high-frequency market data in negative-rate environments.
To help your project stand out, here is a professional, high-impact `README.md` designed specifically for quantitative finance repositories. It combines clear installation steps with the mathematical rigor that recruiters and collaborators look for.

---

# 💹 Hybrid SABR-Local Volatility Calibration Engine

An institutional-grade volatility engine that bridges the gap between SABR's market-realistic smiles and Dupire's exact surface calibration. Perfect for pricing complex path-dependent exotics with a live, interactive dashboard that works straight out of the box.

## 🌟 Key Features

* **Shifted SABR Calibration:** Native support for negative interest rate environments (e.g., EUR/JPY) via the Shifted SABR model.
* **Exact Local Vol Mapping:** Implements Dupire’s equation to map the model surface exactly to market quotes for exotic pricing.
* **Live Market Data:** Automated fetching of real-time option chains for Equities, FX, and Crypto using `yfinance`.
* **Interactive Analytics:** A Streamlit-based dashboard featuring 3D surface visualizations and parameter sensitivity metrics.

## 🚀 Quick Start

### 1. One-Click Launch (Recommended)

You can view the live engine immediately without any local installation via Streamlit Community Cloud:
[](https://www.google.com/search?q=https://share.streamlit.io/your-username/your-repo-name/app.py)

### 2. Local Installation

Ensure you have Python 3.9+ installed, then run:

```bash
# Clone the repository
git clone https://github.com/your-username/sabr-lv-engine.git
cd sabr-lv-engine

# Install required dependencies
pip install -r requirements.txt

# Launch the dashboard
streamlit run app.py

```

---

## 📐 Mathematical Background

This engine reconciles the "best of both worlds" in volatility modeling:

### Stochastic Layer (SABR)

We utilize the Shifted SABR extension to handle negative rates. The dynamics are governed by:


### Precision Layer (Dupire)

Once the SABR skeleton is calibrated, we apply the Dupire Mapping to generate a Local Volatility surface  that re-prices market vanillas with zero error:


---

## 🛠️ Industrial Use Cases

* **Exotic Option Pricing:** Provides the high-fidelity local vol grid required for Barrier, Asian, and Lookback options.
* **Market Making:** Enables tighter spreads by identifying divergences between stochastic dynamics and market noise.
* **Risk Management:** Generates model-consistent Greeks () even in highly skewed market regimes.

## 📚 Documentation

For a deep dive into the mathematical derivations and model dynamics, read the full white paper:
👉 **[Download Technical White Paper (PDF)](SABR.pdf)**


**Visual Demo**
<img width="3024" height="1964" alt="Screenshot 2026-02-13 at 4 56 01 PM" src="https://github.com/user-attachments/assets/c2d72347-fe64-4bba-9ecb-f7a5d462ae80" />
<img width="3024" height="1964" alt="Screenshot 2026-02-13 at 4 55 46 PM" src="https://github.com/user-attachments/assets/35b6ab2d-3090-493d-b68e-7ff9586dc305" />


---
