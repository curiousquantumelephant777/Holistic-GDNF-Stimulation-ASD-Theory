import matplotlib.pyplot as plt
import numpy as np

def draw_dendrite(x, y, angle, length, depth, noise_factor):
    if depth == 0:
        return
    
    # Calculate new coordinates based on angle and length
    x_new = x + length * np.cos(angle)
    y_new = y + length * np.sin(angle)
    
    # Draw the "segment"
    plt.plot([x, x_new], [y, y_new], color='#556B2F', alpha=0.6, lw=depth*0.5)
    
    # Stochastic branching (The "coherence" variability)
    new_length = length * 0.75
    spread = 0.5 + (np.random.rand() * noise_factor)
    
    # Recursive branches
    draw_dendrite(x_new, y_new, angle + spread, new_length, depth - 1, noise_factor)
    draw_dendrite(x_new, y_new, angle - spread, new_length, depth - 1, noise_factor)

# Visualization of plot
fig = plt.figure(figsize=(8, 8), facecolor='white', edgecolor='white')
plt.axis('off')

# We can start at the "Soma" (0,0) and grow upwards
# We can change 'depth' to simulate "Re-arborization" (e.g., 4 is decoherent/stochioastic noise, 8 is rebooted or childlike state)
draw_dendrite(0, 0, np.pi/2, 10, depth=10, noise_factor=0.2)

plt.title("Holistic Dendritic Re-arborization (GDNF Reboot)", color='purple')
plt.show()
