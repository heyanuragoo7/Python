import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import json

# Generate sample data for api_logs.csv
np.random.seed(42)
random.seed(42)

# Number of rows
n = 10000

# Timestamps: random dates in 2023
start_date = datetime(2023, 1, 1)
timestamps = [start_date + timedelta(seconds=random.randint(0, 365*24*3600)) for _ in range(n)]
timestamps_iso = [t.isoformat() for t in timestamps]

# IP addresses: random IPs
ips = [f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}" for _ in range(n)]

# Endpoints
endpoints = ['/login', '/checkout', '/api/users', '/api/orders', '/health', '/api/products', '/logout']
endpoint_list = [random.choice(endpoints) for _ in range(n)]

# Status codes: mostly 200, some errors
status_codes = np.random.choice([200, 201, 400, 404, 500], size=n, p=[0.8, 0.1, 0.03, 0.05, 0.02])

# Response times: normal around 100ms, some outliers
response_times = np.random.normal(100, 50, n)
response_times = np.clip(response_times, 10, 2000)  # clip to reasonable range

# User agents: some missing
user_agents = [f"User-Agent-{random.randint(1,100)}" for _ in range(n)]
for i in random.sample(range(n), int(0.1*n)):  # 10% missing
    user_agents[i] = np.nan

# Create DataFrame
df = pd.DataFrame({
    'timestamp': timestamps_iso,
    'ip_address': ips,
    'endpoint': endpoint_list,
    'status_code': status_codes,
    'response_time_ms': response_times,
    'user_agent': user_agents
})

# Save to CSV
df.to_csv('api_logs.csv', index=False)

# Generate endpoint_metadata.json
metadata = {
    "/login": "auth_service",
    "/checkout": "payment_service",
    "/api/users": "user_service",
    "/api/orders": "order_service",
    "/health": "health_service",
    "/api/products": "product_service",
    "/logout": "auth_service"
}

with open('endpoint_metadata.json', 'w') as f:
    json.dump(metadata, f, indent=4)

print("Data files generated successfully!")