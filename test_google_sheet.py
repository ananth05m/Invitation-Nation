import os
from datetime import datetime
import requests

GOOGLE_SCRIPT_URL = os.getenv("GOOGLE_SCRIPT_URL")

def log_result(test_case, status, execution_time, failure_reason=""):
    if not GOOGLE_SCRIPT_URL:
        raise RuntimeError("Set GOOGLE_SCRIPT_URL before running.")

    data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "test_case": test_case,
        "status": status,
        "execution_time": execution_time,
        "failure_reason": failure_reason,
    }

    print("Sending data to Google Sheets...")
    response = requests.post(GOOGLE_SCRIPT_URL, json=data, timeout=30)

    print("HTTP Status:", response.status_code)
    print("Response:", response.text)
    response.raise_for_status()

if __name__ == "__main__":
    log_result("Google Sheet Connection Test", "PASS", "1.00 seconds")
    print("Google Sheet logging test completed.")
