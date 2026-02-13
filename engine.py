import QuantLib as ql
import numpy as np
from scipy.optimize import minimize

class HybridEngine:
    def __init__(self, forward, expiry, shift=0.0):
        # Strict casting for QuantLib C++ compatibility
        self.f0 = float(forward)
        self.T = float(expiry)
        self.shift = float(shift)
        
    def sabr_vol(self, K, alpha, beta, rho, nu):
        try:
            return ql.sabrVolatility(
                float(K), float(self.f0), float(self.T),
                float(alpha), float(beta), float(rho), float(nu),
                float(self.shift)
            )
        except Exception:
            return 0.5 # Fallback vol if math fails

    def calibrate_sabr(self, market_strikes, market_vols):
        def objective(params):
            alpha, rho, nu = params
            beta = 0.5 
            errors = [(self.sabr_vol(k, alpha, beta, rho, nu) - v)**2 
                      for k, v in zip(market_strikes, market_vols)]
            return np.sum(errors)

        res = minimize(objective, [0.1, -0.1, 0.3], 
                       bounds=[(1e-4, 2.0), (-0.99, 0.99), (1e-4, 2.0)],
                       method='L-BFGS-B')
        return res.x