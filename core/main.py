# Inside your main loop
if signal_detected:
    features = ml.features.extract_market_signature(candle, indicators)
    confidence = ml.gatekeeper.predict(features)
    
    if risk_manager.validate_new_trade(positions, confidence):
        # Place trade
        logger.log_event("ORDER_PLACED", "Entering Long Position", features)
    else:
        # Log the rejection as a data point for future AI training
        logger.log_event("TRADE_REJECTED", "AI or Risk Gatekeeper blocked trade", {
            "features": features,
            "confidence": confidence,
            "reason": "Low ML Confidence" if confidence < 0.6 else "Risk Limit"
        })