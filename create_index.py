import requests
import json

es_url = "http://localhost:9200"
index_name = "cybersecurity-threats"

with open("elasticsearch_mapping.json", "r") as f:
    mapping = json.load(f)

print(f"Creating Elasticsearch index: {index_name}")
print("=" * 60)

delete_response = requests.delete(f"{es_url}/{index_name}")
if delete_response.status_code == 200:
    print(f"Deleted existing index: {index_name}")
elif delete_response.status_code == 404:
    print(f"ℹNo existing index to delete")

response = requests.put(
    f"{es_url}/{index_name}",
    headers={"Content-Type": "application/json"},
    json=mapping
)

if response.status_code == 200:
    print(f"\nIndex '{index_name}' created successfully!")
    print(f"\nResponse:")
    print(json.dumps(response.json(), indent=2))
    
    verify_response = requests.get(f"{es_url}/{index_name}/_mapping")
    print(f"\nVerifying mapping...")
    print(json.dumps(verify_response.json(), indent=2)[:500] + "...")
else:
    print(f"\nError creating index:")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
