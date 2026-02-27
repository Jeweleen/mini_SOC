import requests
import os

API_URL = "https://my.api.mockaroo.com/ironclad-soc-case-artifacts"

headers = {
    "X-API-Key": os.environ.get("MOCKAROO_API_KEY")
}

response = requests.get(API_URL,headers=headers, timeout=10)
print("Status:", response.status_code)

if response.status_code != 200:
    print("Request failed:", response.text[:200])
    raise SystemExit

data = response.json()
print("JSON type:", type(data))
print("Records:", len(data) if isinstance(data, list) else "N/A")

# Preview first record
if isinstance(data, list) and data:
    print("First record preview:")
    print(data[0])
else:
    print("Unexpected JSON structure. Expected a list of records.")
    raise SystemExit

if isinstance(data[0], dict):
    print("\nFields in record:")
    for k in data[0].keys():
        print("-", k)