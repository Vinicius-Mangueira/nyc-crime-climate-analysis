import requests, csv, os

# — CONFIGURAÇÃO —
TOKEN     = "sYfiszwGwpMAOqGhxqycfdFbDkoLnlLs"    # seu token
STATION   = "GHCND:USW00094728"                  # Central Park
START     = "2024-01-01"
END       = "2024-12-31"
LIMIT     = 1000                                 # máximo = 1000 registros por chamada
OUT_DIR   = "data/raw"
OUT_FILE  = os.path.join(OUT_DIR, "noaa_gsod_2024.csv")

os.makedirs(OUT_DIR, exist_ok=True)

headers = {"Token": TOKEN}
url     = "https://www.ncei.noaa.gov/cdo-web/api/v2/data"
params  = {
    "datasetid": "GSOD",
    "stationid": STATION,
    "startdate": START,
    "enddate": END,
    "limit": LIMIT,
    "offset": 1,
    "units": "metric"
}

all_rec = []
print("🔄 Iniciando download via API CDO…")
while True:
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    page = resp.json().get("results", [])
    if not page:
        break
    all_rec.extend(page)
    print(f"  📥  {len(page)} registros recebidos (offset={params['offset']})")
    params["offset"] += LIMIT

if not all_rec:
    print("⚠️  Nenhum registro retornado. Verifique token/período/estação.")
    exit(1)

print(f"💾 Gravando {len(all_rec)} registros em {OUT_FILE} …")
with open(OUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=all_rec[0].keys())
    writer.writeheader()
    writer.writerows(all_rec)

print("✅ Concluído!")
