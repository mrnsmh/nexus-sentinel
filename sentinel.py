import os
import psutil
import subprocess
import json
import requests
from datetime import datetime

def get_system_vitals():
    return {
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "load": os.getloadavg()
    }

def proactive_cleanup():
    # Only clean if disk is above threshold
    if psutil.disk_usage('/').percent > 80:
        subprocess.run(["pm2", "flush"], capture_output=True)
        # Add more cleanup commands here
        return True
    return False

def smart_status():
    vitals = get_system_vitals()
    # Simple logic to determine "Health Score"
    score = 100
    if vitals['cpu'] > 80: score -= 20
    if vitals['ram'] > 85: score -= 30
    if vitals['disk'] > 90: score -= 40
    
    return {
        "score": max(0, score),
        "vitals": vitals,
        "recommendation": "All good" if score > 70 else "Optimization needed"
    }

if __name__ == "__main__":
    print(json.dumps(smart_status(), indent=2))
