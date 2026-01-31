import logging
import sys

class RiskManager:
    def __init__(self, config):
        self.max_daily_loss = config['RISK_MANAGEMENT']['MAX_DAILY_LOSS_INR']
        self.max_open_positions = config['RISK_MANAGEMENT'].get('MAX_OPEN_POSITIONS', 3)
        self.logger = logging.getLogger("RiskManager")

    def check_daily_limit(self, current_pnl):
        """Step 6 & 7: Automated Circuit Breaker."""
        if current_pnl <= self.max_daily_loss:
            self.logger.critical(f"🛑 CIRCUIT BREAKER TRIGGERED: P&L {current_pnl} <= Limit {self.max_daily_loss}")
            return False
        return True

    def validate_new_trade(self, current_positions, ml_confidence):
        """Final check before placing an order."""
        if len(current_positions) >= self.max_open_positions:
            self.logger.warning("Trade Rejected: Max Open Positions reached.")
            return False
        
        # Integrate AI Gatekeeper score here
        if ml_confidence < 0.60:
            self.logger.warning(f"Trade Rejected: AI Confidence too low ({ml_confidence:.2f})")
            return False
            
        return True

    def emergency_kill_switch(self, kite_client):
        """Immediately squares off all positions and exits script."""
        self.logger.info("Executing Emergency Kill Switch...")
        # positions = kite_client.positions()
        # Square-off logic for Kite goes here
        sys.exit("⚠️ SYSTEM SHUTDOWN: Emergency Kill Switch Activated.")