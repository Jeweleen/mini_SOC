import requests
import os
from enum import Enum

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

'''if isinstance(data[0], dict):
    print("\nFields in record:")
    for k in data[0].keys():
       print("-", k)'''

##Create Enum for Severity and Status

class Severity(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class CaseStatus(Enum):
    NEW = "NEW"
    INVESTIGATING = "INVESTIGATING"
    RESOLVED = "RESOLVED"
    FALSE_POSITIVE = "FALSE_POSITIVE"
from artifact import Artifact
#Creating an artifact object
if isinstance(data[0], dict):
    test_artifact = Artifact(data[0])
    print(test_artifact)
