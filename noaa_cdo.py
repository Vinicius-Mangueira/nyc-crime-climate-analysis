import requests
import csv
import os

# — CONFIGURATION —
TOKEN     = "sYfiszwGwpMAOqGHxqycFdFbDkoLnlLs"  # your NOAA CDO API token
STATION   = "GHCND:USW00094728"                # Central Park station ID
START     = "2024-01-01"
END       = "2024-12-31"
LIMIT     = 1000                               # max records per request
OUTPUT_DIR  = "data/raw"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "noaa_gsod_2024.csv")

# Create the output folder if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Prepare a requests session that ignores any system proxy
session = requests.Session()
session.trust_env = False  # do not use proxy settings from the environment

# API endpoint and headers
API_URL = "https://www.ncei.noaa.gov/cdo-web/api/v2/data"
headers = {
    "Token": TOKEN
}

# Query parameters
params = {
    "datasetid":  "GSOD",
    "stationid":  STATION,
    "startdate":  START,
    "enddate":    END,
    "limit":      LIMIT,
    "offset":     1,
    "units":      "metric"
}

# Container for all records
all_records = []

print("Starting download via NOAA CDO API...")

# Loop through pages until no more results
while True:
    response = session.get(API_URL, headers=headers, params=params, timeout=30)
    response.raise_for_status()
    page = response.json().get("results", [])
    if not page:
        break
    all_records.extend(page)
    print(f"  Retrieved {len(page)} records (offset={params['offset']})")
    params["offset"] += LIMIT

if not all_records:
    print("Warning: No data returned for the specified period/station.")
    exit(1)

# Write to CSV
print(f"Writing {len(all_records)} records to {OUTPUT_FILE}...")
with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=all_records[0].keys())
    writer.writeheader()
    writer.writerows(all_records)

print("Download and CSV export complete!")
