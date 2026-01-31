import logging
import json
import os
from datetime import datetime

class TradingLogger:
    def __init__(self, log_dir="logs"):
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        self.logger = logging.getLogger("NiftyAI_v5")
        self.logger.setLevel(logging.DEBUG)
        
        # 1. Console Handler (For you to see in VS Code)
        c_handler = logging.StreamHandler()
        c_handler.setLevel(logging.INFO)
        c_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        
        # 2. File Handler (JSON for ML and SRE Audit)
        f_handler = logging.FileHandler(f"{log_dir}/trading_audit.json")
        f_handler.setLevel(logging.DEBUG)
        
        self.logger.addHandler(c_handler)
        self.logger.addHandler(f_handler)

    def log_event(self, event_type, message, metadata=None):
        """
        Captures structured data. 
        Example metadata: {'rsi': 72, 'pnl': -1500, 'confidence': 0.88}
        """
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "event": event_type,
            "message": message,
            "metadata": metadata or {}
        }
        # Logs the JSON string for future parsing
        self.logger.debug(json.dumps(log_entry))
        if event_type in ["CRITICAL", "ERROR"]:
            self.logger.error(message)
        else:
            self.logger.info(message)