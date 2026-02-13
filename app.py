import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from datetime import datetime
from engine import HybridEngine  # Ensure engine.py is in the same folder

st.set_page_config(page_title="SABR-LV Engine", layout="wide")
st.title("💹 Hybrid SABR-Local Volatility Engine")

# --- DATA FETCHING ---
ticker_symbol = st.sidebar.selectbox("Select Asset", ["AAPL", "SPY", "TSLA", "BTC-USD"])
shift_val = st.sidebar.slider("Shift (Negative Rates)", 0.0, 0.05, 0.0, 0.01)

def get_market_data(symbol):
    t = yf.Ticker(symbol)
    if not t.options:
        return None
    
    # Use the first available expiry
    target_expiry = t.options[0]
    opts = t.option_chain(target_expiry)
    
    # Handle different price locations in yfinance
    try:
        price = t.fast_info['last_price']
    except:
        price = opts.calls['strike'].median()
        
    d1 = datetime.strptime(target_expiry, '%Y-%m-%d')
    t_exp = max((d1 - datetime.now()).days / 365.0, 0.01)
    
    return {"calls": opts.calls, "spot": price, "t": t_exp, "expiry": target_expiry}

data_bundle = get_market_data(ticker_symbol)

if data_bundle:
    df = data_bundle["calls"].query("volume > 1").head(25)
    strikes, vols = df['strike'].values, df['impliedVolatility'].values
    
    st.success(f"Connected: {ticker_symbol} | Spot: {data_bundle['spot']:.2f}")

    # Calibration
    eng = HybridEngine(data_bundle["spot"], data_bundle["t"], shift_val)
    alpha, rho, nu = eng.calibrate_sabr(strikes, vols)

    # Tabs for Visuals
    tab1, tab2 = st.tabs(["SABR Smile", "3D Vol Surface"])
    
    with tab1:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=strikes, y=vols, mode='markers', name='Market'))
        k_line = np.linspace(min(strikes), max(strikes), 50)
        v_line = [eng.sabr_vol(k, alpha, 0.5, rho, nu) for k in k_line]
        fig.add_trace(go.Scatter(x=k_line, y=v_line, name='SABR Fit', line=dict(color='red')))
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        # Generate 3D Surface
        s_grid = np.linspace(data_bundle["spot"]*0.8, data_bundle["spot"]*1.2, 20)
        t_grid = np.linspace(0.1, 1.5, 15)
        z = [[HybridEngine(data_bundle["spot"], ty, shift_val).sabr_vol(sx, alpha, 0.5, rho, nu) 
              for sx in s_grid] for ty in t_grid]
        
        fig3d = go.Figure(data=[go.Surface(z=z, x=s_grid, y=t_grid, colorscale='Plasma')])
        fig3d.update_layout(scene=dict(xaxis_title='Strike', yaxis_title='Time', zaxis_title='Vol'))
        st.plotly_chart(fig3d, use_container_width=True)
else:
    st.error("Market data unavailable for this ticker. Try 'SPY' or 'AAPL' during market hours.")