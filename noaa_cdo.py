import requests
import csv
import os
from datetime import date, timedelta

# — CONFIGURATION —
TOKEN      = "sYfiszwGwpMAOqGhxqycfdFbDkoLnlLs"  # your NOAA CDO token
STATION    = "GHCND:USW00094728"                # Central Park station
YEAR       = 2024
LIMIT      = 1000                               # max per request
OUT_DIR    = "data/raw"
OUT_FILE   = os.path.join(OUT_DIR, "noaa_gsod_2024.csv")

# Create output folder
os.makedirs(OUT_DIR, exist_ok=True)

# Prepare session (ignore system proxy + simple retries)
session = requests.Session()
session.trust_env = False
adapter = requests.adapters.HTTPAdapter(max_retries=3)
session.mount("https://", adapter)

# CDO API endpoint & headers
API_URL = "https://www.ncei.noaa.gov/cdo-web/api/v2/data"
headers = {"Token": TOKEN}

def month_ranges(year):
    """Yield (start_date, end_date) for each month of the given year."""
    for m in range(1, 13):
        start = date(year, m, 1)
        # month end = next month first minus one day
        if m == 12:
            end = date(year, 12, 31)
        else:
            end = date(year, m+1, 1) - timedelta(days=1)
        yield start.isoformat(), end.isoformat()

all_records = []

print(f"→ Pulling GSOD {YEAR} in monthly chunks…")
for start_date, end_date in month_ranges(YEAR):
    params = {
        "datasetid": "GSOD",
        "stationid": STATION,
        "startdate": start_date,
        "enddate": end_date,
        "limit": LIMIT,
        "offset": 1,
        "units": "metric"
    }

    print(f"  • Fetching {start_date} → {end_date} …", end="", flush=True)
    month_data = []
    while True:
        resp = session.get(API_URL, headers=headers, params=params, timeout=30)
        resp.raise_for_status()
        page = resp.json().get("results", [])
        if not page:
            break
        month_data.extend(page)
        params["offset"] += LIMIT

    print(f" {len(month_data)} records")
    all_records.extend(month_data)

if not all_records:
    print("⚠️  No data returned for 2024. Check token/station.")
    exit(1)

# Write combined CSV
print(f"→ Writing {len(all_records)} total records to {OUT_FILE} …")
with open(OUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=all_records[0].keys())
    writer.writeheader()
    writer.writerows(all_records)

print("✅  Done!")  
