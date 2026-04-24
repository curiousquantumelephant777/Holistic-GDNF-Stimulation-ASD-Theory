import numpy as np
import matplotlib.pyplot as plt
from rdkit import Chem
from rdkit.Chem import AllChem

# Using the ibogaine molecule
smiles = "CCC1CC2CC3C1N(C2)CCC4=C3C=C(C=C4)OC"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())

# Function to simulate electron density (e.g., as sum of Gaussians around atom centers)
def simulate_electron_density(x, y, atom_positions, sigma=0.5):
    density = np.zeros_like(x, dtype=float)
    for pos in atom_positions:
        r_sq = (x - pos[0])**2 + (y - pos[1])**2
        density += np.exp(-r_sq / (2 * sigma**2))
    return density

# Create Grid for Visualization (re-using parameters from previous cells)
res = 100
x_range = np.linspace(-5, 5, res)
y_range = np.linspace(-5, 5, res)
X, Y = np.meshgrid(x_range, y_range)

# Extract 2D coordinates from the 3D conformer (simplified projection)
conf = mol.GetConformer()
atom_positions = [[conf.GetAtomPosition(i).x, conf.GetAtomPosition(i).y] for i in range(mol.GetNumAtoms())]

# Generate the simulated electron density
rho = simulate_electron_density(X, Y, atom_positions)

# Calculate the gradient of the electron density
# np.gradient returns a tuple (gradient_y, gradient_x)
grad_y, grad_x = np.gradient(rho, y_range[1]-y_range[0], x_range[1]-x_range[0])

fig, ax = plt.subplots(figsize=(10, 8), facecolor='#301934') # Set figure background to dark purple

# Set the axes facecolor (the plot area with the dots) to navy blue
ax.set_facecolor('#000033')

# Plot the electron density contours in the background
contour_plot = ax.contourf(X, Y, rho, levels=50, cmap='magma', alpha=0.8) # Reverted colormap to magma
cbar = fig.colorbar(contour_plot, ax=ax) # Capture colorbar object
cbar.set_label('Electron Density (ρ)', color='#FFD1DC') # Set colorbar label color
cbar.ax.tick_params(colors='#FFD1DC') # Set colorbar tick label color

# Plot the gradient vector field using quiver
# We thin out the arrows for better visualization
skip = 7 # Plot every 'skip' arrow
ax.quiver(X[::skip, ::skip], Y[::skip, ::skip], grad_x[::skip, ::skip], grad_y[::skip, ::skip],
           color='#FFD1DC', alpha=0.7, scale=50, width=0.003, headwidth=3, headlength=4) # Quiver color remains

ax.set_title('Simulated Electron Density and its Gradient Vector Field (Ibogaine)', color='#FFD1DC') # Title color remains
ax.set_xlabel('X-coordinate', color='#FFD1DC') # X-label color remains
ax.set_ylabel('Y-coordinate', color='#FFD1DC') # Y-label color remains
ax.set_aspect('equal') # Ensure aspect ratio is equal
# Removed plt.axis('off') to show labels
plt.show()
