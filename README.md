# Reservoir Property Mapping with Ordinary Kriging

A Python utility for generating interactive, high-quality reservoir property maps using **Ordinary Kriging** and **Plotly**. This module is designed to interpolate discrete spatial data (such as porosity, permeability, or pressure) into smooth, professional contour maps suitable for field analysis.

## 🚀 Features

* **Spatial Interpolation:** Implements Ordinary Kriging via the `pykrige` library for statistically robust spatial estimation.
* **Interactive Visuals:** Uses `plotly.graph_objects` to allow for zooming, panning, and detailed hover-data within the map.
* **Well Location Markers:** Automatically plots well coordinates with triangle-up symbols and associated text labels.
* **Aesthetic Styling:** Features a `spectral` colorscale, dark-themed templates, and smoothed contour lines with automatic labels.

---

## 🛠️ Installation

Ensure you have the necessary dependencies installed in your Python environment:

```bash
pip install numpy plotly pykrige
```

# Usage Guide: Reservoir Kriging Contours

This guide provides examples and details on how to implement the `create_kriging_contour` function within your reservoir engineering or data science workflows.

## 1. Basic Implementation

To generate a standard reservoir property map, ensure your data is organized into numerical arrays for coordinates and a list of strings for well names.

```python
import numpy as np
from contours import create_kriging_contour

# Define your field data
x_coords = np.array([500, 1200, 800, 1500, 2000])
y_coords = np.array([1000, 1100, 1500, 1800, 1200])
porosity = np.array([0.18, 0.12, 0.25, 0.08, 0.21])
well_labels = ["Main-01", "Edge-02", "Crest-01", "West-01", "South-02"]

# Generate the interactive Plotly figure
fig = create_kriging_contour(
    x=x_coords,
    y=y_coords,
    z=porosity,
    wells=well_labels,
    grid_res=400, # Higher resolution for smoother contours
    title="Top Reservoir Porosity Distribution (Phi)"
)

# Render in browser
fig.show()
