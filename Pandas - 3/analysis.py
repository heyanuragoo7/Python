import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from datetime import datetime

# Load the CSV file
df = pd.read_csv('api_logs.csv')

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Column names
print("\nColumn names:")
print(df.columns.tolist())

# Data types
print("\nData types:")
print(df.dtypes)

# Total number of rows
print(f"\nTotal number of rows: {len(df)}")

# Extract response_time_ms as Series
response_times = df['response_time_ms']

# Calculate statistics
mean_rt = response_times.mean()
median_rt = response_times.median()
p95_rt = response_times.quantile(0.95)

print(f"Mean response time: {mean_rt:.2f} ms")
print(f"Median response time: {median_rt:.2f} ms")
print(f"95th percentile response time: {p95_rt:.2f} ms")

# Add new column response_time_sec
df['response_time_sec'] = df['response_time_ms'] / 1000

print("\nDataFrame with new column:")
print(df[['response_time_ms', 'response_time_sec']].head())

# Load JSON file
with open('endpoint_metadata.json', 'r') as f:
    metadata = json.load(f)

# Convert to DataFrame
metadata_df = pd.DataFrame(list(metadata.items()), columns=['endpoint', 'service_name'])

print("Endpoint metadata:")
print(metadata_df)

# Merge with logs DataFrame
df = df.merge(metadata_df, on='endpoint', how='left')

print("\nMerged DataFrame (first 5 rows):")
print(df.head())

# Identify missing values
print("Missing values per column:")
print(df.isnull().sum())

# Fill missing user_agent with 'unknown'
df['user_agent'] = df['user_agent'].fillna('unknown')

# Drop rows where response_time_ms is missing
df = df.dropna(subset=['response_time_ms'])

print(f"\nAfter cleaning, total rows: {len(df)}")

# Explanation
print("\nExplanation:")
print("Use fillna when the missing values can be reasonably imputed (e.g., categorical data like user_agent).")
print("Use dropna when missing values are critical and cannot be imputed (e.g., response_time_ms for analysis).")

# Filter requests with status_code >= 400
error_requests = df[df['status_code'] >= 400]
print(f"Error requests (status >= 400): {len(error_requests)}")

# Filter logs for /login and /checkout
login_checkout = df[df['endpoint'].isin(['/login', '/checkout'])]
print(f"Login/Checkout requests: {len(login_checkout)}")

# Filter requests with response_time_ms > 500
slow_requests = df[df['response_time_ms'] > 500]
print(f"Slow requests (>500ms): {len(slow_requests)}")

print("\nSample slow requests:")
print(slow_requests[['endpoint', 'response_time_ms', 'status_code']].head())

# Sort by response_time_ms descending
sorted_df = df.sort_values('response_time_ms', ascending=False)

# Display top 10 slowest API calls
print("Top 10 slowest API calls:")
print(sorted_df[['endpoint', 'response_time_ms', 'status_code', 'ip_address']].head(10))

# Group by endpoint
endpoint_stats = df.groupby('endpoint').agg(
    avg_response_time=('response_time_ms', 'mean'),
    total_requests=('endpoint', 'count')
)
print("Endpoint statistics:")
print(endpoint_stats)

# Group by status_code
status_counts = df.groupby('status_code').size()
print("\nStatus code counts:")
print(status_counts)

# Find endpoint with highest average latency
highest_latency_endpoint = endpoint_stats['avg_response_time'].idxmax()
highest_latency = endpoint_stats['avg_response_time'].max()
print(f"\nEndpoint with highest average latency: {highest_latency_endpoint} ({highest_latency:.2f} ms)")

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract date and hour
df['date'] = df['timestamp'].dt.date
df['hour'] = df['timestamp'].dt.hour

# Create request_hour column
df['request_hour'] = df['timestamp'].dt.floor('H')

print("DataFrame with datetime columns:")
print(df[['timestamp', 'date', 'hour', 'request_hour']].head())

# Calculate requests per hour
requests_per_hour = df.groupby('request_hour').size()
print("Requests per hour:")
print(requests_per_hour)

# Find peak traffic hour
peak_hour = requests_per_hour.idxmax()
peak_count = requests_per_hour.max()
print(f"\nPeak traffic hour: {peak_hour} with {peak_count} requests")

# Plot request volume per hour
plt.figure(figsize=(10, 6))
requests_per_hour.plot(kind='bar')
plt.title('Request Volume per Hour')
plt.xlabel('Hour')
plt.ylabel('Number of Requests')
plt.xticks(rotation=45)
plt.savefig('request_volume_per_hour.png')
plt.show()

# Overall average latency
overall_avg = df['response_time_ms'].mean()
print(f"Overall average latency: {overall_avg:.2f} ms")

# 90th and 99th percentiles
p90 = df['response_time_ms'].quantile(0.90)
p99 = df['response_time_ms'].quantile(0.99)
print(f"90th percentile latency: {p90:.2f} ms")
print(f"99th percentile latency: {p99:.2f} ms")

# Average latency per endpoint
avg_latency_per_endpoint = df.groupby('endpoint')['response_time_ms'].mean().sort_values(ascending=False)
print("\nAverage latency per endpoint:")
print(avg_latency_per_endpoint)

# Create minute column
df['request_minute'] = df['timestamp'].dt.floor('T')

# Calculate requests per minute
throughput_per_minute = df.groupby('request_minute').size()

# Average throughput
avg_throughput = throughput_per_minute.mean()
print(f"Average throughput: {avg_throughput:.2f} requests per minute")

# Peak throughput minute
peak_minute = throughput_per_minute.idxmax()
peak_throughput = throughput_per_minute.max()
print(f"Peak throughput minute: {peak_minute} with {peak_throughput} requests")

print("\nThroughput per minute (sample):")
print(throughput_per_minute.head(10))

# Top 10 IP addresses by request count
top_ips = df.groupby('ip_address').size().sort_values(ascending=False).head(10)
print("Top 10 IP addresses by request count:")
print(top_ips)

# Detect suspicious IPs (>1000 requests)
suspicious_ips = df.groupby('ip_address').size()
suspicious_ips = suspicious_ips[suspicious_ips > 1000]
print(f"\nSuspicious IPs (>1000 requests): {len(suspicious_ips)}")
if len(suspicious_ips) > 0:
    print(suspicious_ips)
else:
    print("No IPs with >1000 requests found.")

# Insights & Interpretation

print("### Which endpoints are performance bottlenecks?")
print(f"Based on the analysis, the endpoint with the highest average latency is {highest_latency_endpoint} with {highest_latency:.2f} ms.")
print("Endpoints with high latency should be investigated for optimization.")

print("\n### At what time does traffic spike the most?")
print(f"Traffic spikes at {peak_hour} with {peak_count} requests.")

print("\n### Are errors correlated with high response times?")
error_correlation = df[df['status_code'] >= 400]['response_time_ms'].mean()
success_correlation = df[df['status_code'] < 400]['response_time_ms'].mean()
print(f"Average response time for errors: {error_correlation:.2f} ms")
print(f"Average response time for successful requests: {success_correlation:.2f} ms")
if error_correlation > success_correlation:
    print("Errors tend to have higher response times, indicating correlation.")
else:
    print("No clear correlation between errors and response times.")

print("\n### What recommendations would you give to backend teams?")
print("1. Optimize the high-latency endpoint:", highest_latency_endpoint)
print("2. Monitor traffic during peak hours:", peak_hour)
print("3. Investigate error-prone requests to reduce failures.")
print("4. Implement rate limiting for suspicious IPs.")
print("5. Consider caching for frequently accessed endpoints.")