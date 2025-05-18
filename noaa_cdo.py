import requests
import csv
import os
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# — CONFIGURATION —
TOKEN      = "sYfiszwGwpMAOqGhxqycfdFbDkoLnlLs"  # your NOAA CDO token
STATION    = "GHCND:USW00094728"                # Central Park
START      = "2024-01-01"
END        = "2024-12-31"
LIMIT      = 500                                # >366 days, so one request
OUT_DIR    = "data/raw"
OUT_FILE   = os.path.join(OUT_DIR, "noaa_gsod_2024.csv")

os.makedirs(OUT_DIR, exist_ok=True)

# — BUILD A SESSION WITH RETRIES —
session = requests.Session()
session.trust_env = False
retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retries))

# — SETUP REQUEST —
url = "https://www.ncei.noaa.gov/cdo-web/api/v2/data"
headers = {"Token": TOKEN}
params = {
    "datasetid":  "GSOD",
    "stationid":  STATION,
    "startdate":  START,
    "enddate":    END,
    "limit":      LIMIT,
    # no offset needed since LIMIT>number of days
    "units":      "metric"
}

print("🔄 Downloading 2024 GSOD data in one request…")

resp = session.get(url, headers=headers, params=params, timeout=60)
resp.raise_for_status()
results = resp.json().get("results", [])

if not results:
    print("⚠️  No data returned. Check token, dates or station.")
    exit(1)

print(f"✅  Retrieved {len(results)} records. Writing CSV…")

# — WRITE TO CSV —
with open(OUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print(f"💾  Done! File saved to {OUT_FILE}")
