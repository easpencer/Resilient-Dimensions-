
# Seville Agenda Chart + White Paper Website

This repository contains:

- `index.html`: The full website with interactive Plotly chart and white paper
- `generate_sunburst.py`: Python script to regenerate the chart from Excel
- `RCDs in pandemic age (a).xlsx`: Original data source for the chart

## How to Use

1. Open `index.html` to view the full site.
2. To regenerate the chart:

```bash
pip install pandas plotly openpyxl
python generate_sunburst.py
```

This will output `chart.html` with an updated chart you can embed.

## Credits

- Science Summit: https://sciencesummitnyc.org
- Resilient Collective: https://resilient.ucsd.edu
