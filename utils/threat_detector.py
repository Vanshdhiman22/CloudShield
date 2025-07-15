import json
from datetime import datetime

def parse_logs(filepath, start_date=None, end_date=None):
    with open(filepath, 'r') as f:
        logs = json.load(f)

    filtered_logs = []
    for entry in logs:
        timestamp = entry.get("timestamp")
        if timestamp:
            try:
                entry_time = datetime.fromisoformat(timestamp)
            except ValueError:
                continue  # Skip malformed timestamps

            if start_date and entry_time < start_date:
                continue
            if end_date and entry_time > end_date:
                continue

        filtered_logs.append(entry)

    # Count threat types from filtered logs
    threat_counts = {
        "IAM Abuse": 0,
        "S3 Access": 0,
        "Login Failure": 0,
        "Normal": 0
    }

    for entry in filtered_logs:
        event = entry.get("eventName", "")
        error = entry.get("errorMessage", "")

        if event == "ConsoleLogin" and "Failed" in error:
            threat_counts["Login Failure"] += 1
        elif event == "ConsoleLogin" and "Success" in error:
            threat_counts["IAM Abuse"] += 1
        elif event in ["PutObject", "GetObject"]:
            threat_counts["S3 Access"] += 1
        else:
            threat_counts["Normal"] += 1

    return {
        "threat_counts": threat_counts,
        "logs": filtered_logs
    }

