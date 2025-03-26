# This script loads Excel data and builds the Seville Agenda sunburst chart.
import pandas as pd
import plotly.graph_objects as go

df = pd.read_excel("RCDs in pandemic age (a).xlsx")

labels = ['Resilient Community']
parents = ['']
values = [0]

for i, row in df.dropna(subset=["Resilient Community Dimension", "Threshold Transition (Positive Change)", "Sub-dimensions & Indicators"]).iterrows():
    dim = row['Resilient Community Dimension'].strip()
    trans = row['Threshold Transition (Positive Change)'].strip()
    sub = row['Sub-dimensions & Indicators'].strip()
    if dim not in labels:
        labels.append(dim)
        parents.append('Resilient Community')
        values.append(1)
    if trans not in labels:
        labels.append(trans)
        parents.append(dim)
        values.append(1)
    labels.append(sub)
    parents.append(trans)
    values.append(1)

fig = go.Figure(go.Sunburst(labels=labels, parents=parents, values=values, branchvalues='total'))
fig.show()