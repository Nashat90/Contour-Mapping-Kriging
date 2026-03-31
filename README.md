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
