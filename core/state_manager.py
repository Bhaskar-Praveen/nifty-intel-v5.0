import json
import os

class StateManager:
    def __init__(self, file_path="data/system_state.json"):
        self.file_path = file_path
        self.state = self.load_state()

    def load_state(self):
        """Loads the last known state of the bot."""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                return json.load(f)
        return {"active_trades": {}, "daily_pnl": 0.0, "last_run": None}

    def save_state(self, updated_data):
        """Persists state to disk immediately after any trade action."""
        self.state.update(updated_data)
        with open(self.file_path, "w") as f:
            json.dump(self.state, f, indent=4)

    def is_already_in_trade(self, symbol):
        return symbol in self.state["active_trades"]