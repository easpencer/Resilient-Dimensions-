
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

# Load the Excel data
df = pd.read_excel("RCDs in pandemic age (a).xlsx")
df = df.dropna(subset=["Resilient Community Dimension", "Threshold Transition (Positive Change)", "Sub-dimensions & Indicators"])

labels = ["Resilient Community"]
parents = [""]
values = [0]

for i, row in df.iterrows():
    dim = row["Resilient Community Dimension"].strip()
    trans = row["Threshold Transition (Positive Change)"].strip()
    sub = row["Sub-dimensions & Indicators"].strip()

    if dim not in labels:
        labels.append(dim)
        parents.append("Resilient Community")
        values.append(1)
    if trans not in labels:
        labels.append(trans)
        parents.append(dim)
        values.append(1)

    labels.append(sub)
    parents.append(trans)
    values.append(1)

fig = go.Figure(go.Sunburst(
    labels=labels,
    parents=parents,
    values=values,
    branchvalues="total",
    maxdepth=3,
    insidetextfont=dict(color="white"),
    outsidetextfont=dict(color="white"),
))

fig.update_layout(
    margin=dict(t=0, l=0, r=0, b=0),
    paper_bgcolor='black',
    plot_bgcolor='black'
)

# Save to HTML
html = fig.to_html(full_html=False, include_plotlyjs='cdn')
Path("chart.html").write_text(html)
print("Chart saved as chart.html")
