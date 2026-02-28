import requests
import os
from artifact import Artifact
from case import Case


API_URL = "https://my.api.mockaroo.com/ironclad-soc-case-artifacts"

headers = {
    "X-API-Key": os.environ.get("MOCKAROO_API_KEY")
}
##HTTP request
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

#Removed if statment to print the values for Field Records in Step 2.

#Creating an artifact object, updating with case input.
cases = {}

for record in data:
    if not isinstance(record, dict):
        continue

    artifact = Artifact(record)
    cid = artifact.case_id

    if cid not in cases:
        cases[cid] = Case(cid)

    cases[cid].add_artifact(artifact)

# print all cases
print("\n=== Case Summaries ===")
for case in cases.values():
    print(case.summary())
   
    

    
    
