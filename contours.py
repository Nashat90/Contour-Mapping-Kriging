import numpy as np
import plotly.graph_objects as go
from pykrige.ok import OrdinaryKriging

def create_kriging_contour(x, y, z,wells, grid_res=300, title="Reservoir Property Mapping"):
    """
    Creates a Plotly contour plot using Ordinary Kriging.
    
    Parameters:
    - x, y, z: Arrays of your data points
    - grid_res: Number of points for the interpolation grid (higher = smoother)
    """
    
    # 1. Define the grid range
    grid_x = np.linspace(min(x), max(x), grid_res)
    grid_y = np.linspace(min(y), max(y), grid_res)
    
    # 2. Perform Ordinary Kriging
    # variogram_model can be 'linear', 'power', 'gaussian', 'spherical'
    OK = OrdinaryKriging(
        x, y, z, 
        variogram_model='spherical',
        verbose=False, 
        enable_plotting=False
    )
    
    # z_interp is the predicted values, sigmasq is the variance (uncertainty)
    z_interp, coefs = OK.execute('grid', grid_x, grid_y)

    # Create the Plotly Figure
    fig = go.Figure(data=go.Contour(
        z=z_interp,
        x=grid_x,
        y=grid_y,
        colorscale='spectral',ncontours=30,line_smoothing=1.3,
        contours=dict(
            showlabels=True,
            labelfont=dict(size=8, color='white')
        ),
        colorbar=dict(title="Z Value")
    ))

    # Add Well Data Points as Markers + Well Names
    fig.add_trace(go.Scatter(
        x=x, y=y, 
        mode='markers+text',
        marker=dict(color='black', size=5, line=dict(width=1, color='black'),symbol="triangle-up"),
        name='Data Points', text=wells, textfont=dict(size=8,color="black")
    ))

    fig.update_layout(
        title=title,
        xaxis_title="X Coordinates",
        yaxis_title="Y Coordinates",
        template="plotly_dark"
    )

    return fig

# --- Example Usage ---
# x_data = np.random.uniform(0, 10, 20)
# y_data = np.random.uniform(0, 10, 20)
# z_data = np.sin(x_data) + np.cos(y_data)
# fig = create_kriging_contour(x_data, y_data, z_data)
# fig.show()