
# NYC Crime vs. Climate Analysis

An interactive, comprehensive Jupyter-based project exploring the relationship between New York City crime patterns and daily climate variables. Dive into temporal trends, spatial hotspots, correlation metrics, and dynamic dashboards powered by Plotly and Folium.

---

## 🚀 Table of Contents

1. [Project Overview](#project-overview)  
2. [Key Features](#key-features)  
3. [Tech Stack](#tech-stack)  
4. [Repository Structure](#repository-structure)  
5. [Installation & Setup](#installation--setup)  
6. [Data Sources](#data-sources)  
7. [Usage](#usage)  
8. [Utilities](#utilities)  
9. [Contributing](#contributing)  
10. [License](#license)  
11. [Contact](#contact)

---

## 📝 Project Overview

This analysis investigates how climate factors—such as temperature and precipitation—affect crime frequency and distribution in New York City. By merging NYPD crime data with NOAA weather records and visualizing with interactive tools, this project delivers insights for data-driven public safety decisions.

**Research Questions:**  
- How does average daily temperature correlate with total crime count?  
- Does precipitation influence specific crime types?  
- Which NYC boroughs and seasons exhibit the highest crime hotspots?

---

## ✨ Key Features

- **Temporal Analysis:** Interactive Plotly charts showing daily, weekly, and seasonal crime trends.  
- **Spatial Analysis:** Folium choropleth maps and heatmaps to highlight crime density across boroughs.  
- **Correlation Metrics:** Pearson correlation coefficients between crime counts and weather variables.  
- **Dynamic Dashboard:** Date range, season, and offense-type filters via ipywidgets.  
- **End-to-End Workflow:** Organized Jupyter notebooks from ingestion to final report.

---

## 🛠 Tech Stack

- **Python 3.8+**  
- **Jupyter Notebook / JupyterLab**  
- **Pandas**, **NumPy**, **GeoPandas**  
- **Plotly Express**  
- **Folium**  
- **SciPy** (statistical analysis)  
- **ipywidgets** (interactive controls)

---

## 📁 Repository Structure

```text
nyc-crime-climate-analysis/
├── data/                      # All raw and processed data files
│   ├── crime.csv              # Raw NYPD crime data
│   ├── weather.csv            # Raw NOAA weather data
│   ├── nyc_boroughs.geojson   # GeoJSON boundaries for boroughs
│   ├── crime_clean.csv        # Cleaned crime data (processed)
│   └── weather_clean.csv      # Cleaned weather data (processed)
├── notebooks/                 # Jupyter notebooks in execution order
│   ├── 01_ingest_explore.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_temporal_analysis.ipynb
│   ├── 04_spatial_analysis.ipynb
│   ├── 05_correlation_analysis.ipynb
│   ├── 06_interactive_dashboard.ipynb
│   └── 07_final_report.ipynb
├── outputs/                   # Exported dashboards and snapshots
│   └── dashboard_snapshot.png
├── split_nypd_quarters.py     # Utility script to partition crime data by fiscal quarter
├── requirements.txt           # Project dependencies
├── .gitignore
├── LICENSE
└── README.md
````

---

## 🔧 Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Vinicius-Mangueira/nyc-crime-climate-analysis.git
   cd nyc-crime-climate-analysis
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   .venv\Scripts\activate      # Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Place raw data files** in the `data/` directory:

   * `crime.csv` (NYPD crime)
   * `weather.csv` (NOAA weather)
   * `nyc_boroughs.geojson`

5. **Launch JupyterLab:**

   ```bash
   jupyter lab
   ```

---

## 📊 Data Sources

* **NYPD Crime Data:** [NYC Open Data](https://data.cityofnewyork.us)
* **NOAA Weather Data:** [National Centers for Environmental Information](https://www.ncei.noaa.gov)
* **NYC Boroughs GeoJSON:** NYC Open Data portal

---

## 🎬 Usage

1. **Execute notebooks sequentially:**

   * 01\_ingest\_explore.ipynb
   * 02\_data\_cleaning.ipynb
   * 03\_temporal\_analysis.ipynb
   * 04\_spatial\_analysis.ipynb
   * 05\_correlation\_analysis.ipynb
   * 06\_interactive\_dashboard.ipynb
   * 07\_final\_report.ipynb
2. **Interact with dashboard** in notebook 06 for custom analysis.
3. **Export HTML** of dashboards using:

   ```bash
   jupyter nbconvert 06_interactive_dashboard.ipynb --to html --output outputs/dashboard.html
   ```

---

## 🛠 Utilities

* `split_nypd_quarters.py`: Python script to split raw crime data into fiscal quarters for analysis.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/my-feature`).
3. Commit your changes (`git commit -m 'feat: add analysis'`).
4. Push to the branch (`git push origin feature/my-feature`).
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

**Vinicius Mangueira**

* GitHub: [Vinicius-Mangueira](https://github.com/Vinicius-Mangueira)
* LinkedIn: [linkedin.com/in/vinicius-mangueira](https://linkedin.com/in/vinicius-mangueira)

Questions or feedback? Feel free to reach out!

