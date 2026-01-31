import numpy as np

def extract_market_signature(candle_data, indicators):
    """
    Converts raw market data into a 'Signature' the AI can understand.
    """
    return {
        # Momentum Features
        "rsi_14": indicators['rsi'],
        "rsi_slope": indicators['rsi'] - indicators['prev_rsi'],
        
        # Volatility & Regime Features
        "vix_level": indicators['vix'],
        "atr_relative": indicators['atr'] / candle_data['close'],
        
        # Trend Microstructure
        "ema_gap_pct": (candle_data['close'] - indicators['ema_200']) / indicators['ema_200'],
        "body_to_wick_ratio": abs(candle_data['close'] - candle_data['open']) / (candle_data['high'] - candle_data['low']),
        
        # Time-based Context (Captures market open/close volatility)
        "minutes_since_open": indicators['current_minute']
    }