# Seville Agenda Chart

This GitHub repo shows the Seville Agenda for Collective Resilience using an interactive sunburst chart.

## Files

- `index.html`: Website with the embedded chart
- `RCDs in pandemic age (a).xlsx`: Data used to generate the chart
- `generate_sunburst.py`: Python script to generate the chart
- `README.md`: This file

## To regenerate:

```bash
pip install pandas plotly openpyxl
python generate_sunburst.py
```

Open `index.html` in your browser or host via GitHub Pages.
