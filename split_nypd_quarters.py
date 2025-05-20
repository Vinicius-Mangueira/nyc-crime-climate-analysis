import os, math

# input & output paths
INFILE = "data/raw/nypd_crime_2024_onwards.csv"
OUTDIR = "data/raw"

# read everything
with open(INFILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

header, body = lines[0], lines[1:]
n = len(body)

# compute quarter boundaries
end1 = math.ceil(   n * 1/4 )
end2 = math.ceil(   n * 2/4 )
end3 = math.ceil(   n * 3/4 )

# define your 4 output files
quarters = [
    ("nypd_1.csv",     body[           : end1]),
    ("nypd_2.csv",     body[end1      : end2]),
    ("nypd_3.csv",     body[end2      : end3]),
    ("nypd_4.csv",     body[end3      :       ]),
]

os.makedirs(OUTDIR, exist_ok=True)

# write them out
for fname, chunk in quarters:
    outpath = os.path.join(OUTDIR, fname)
    with open(outpath, "w", encoding="utf-8", newline="") as f:
        f.write(header)
        f.writelines(chunk)
    print(f"Wrote {len(chunk)} rows → {outpath}")
