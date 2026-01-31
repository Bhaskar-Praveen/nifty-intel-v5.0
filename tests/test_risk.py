import pytest
from core.risk_manager import RiskManager

def test_circuit_breaker_logic():
    # Mock configuration
    config = {'RISK_MANAGEMENT': {'MAX_DAILY_LOSS_INR': -5000}}
    rm = RiskManager(config)
    
    # Test 1: P&L within limits should pass
    assert rm.check_daily_limit(-2000) == True
    
    # Test 2: P&L at or below limit should trigger (False)
    assert rm.check_daily_limit(-5001) == False