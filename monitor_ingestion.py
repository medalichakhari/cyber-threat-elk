"""
Monitor Logstash ingestion progress
"""
import requests
import time
import sys

es_url = "http://localhost:9200"
index_name = "cybersecurity-threats"

print("Monitoring Elasticsearch Ingestion Progress")
print("=" * 60)
print("Press Ctrl+C to stop monitoring\n")

previous_count = 0
start_time = time.time()

try:
    while True:
        response = requests.get(f"{es_url}/{index_name}/_count", timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            current_count = data['count']
            elapsed = time.time() - start_time
            
            # Calculate rate
            if previous_count > 0:
                rate = (current_count - previous_count) / 5  # docs per second
                print(f"Count: {current_count:,} | "
                      f"Rate: {rate:,.0f} docs/sec | "
                      f"Elapsed: {elapsed:.0f}s")
            else:
                print(f"Count: {current_count:,} | Elapsed: {elapsed:.0f}s")
            
            previous_count = current_count
        else:
            print(f"Error: {response.status_code}")
        
        time.sleep(5)
        
except KeyboardInterrupt:
    print("\n\nMonitoring stopped")
    print(f"Final count: {previous_count:,} documents")
    sys.exit(0)
