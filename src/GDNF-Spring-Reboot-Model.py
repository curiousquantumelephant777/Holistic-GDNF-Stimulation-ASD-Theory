import numpy as np
import matplotlib.pyplot as plt

def model_gdnf_temporal_reboot():
    # 1. Time Axis (Total 20 hours)
    t = np.linspace(0, 20, 3000)
    
    # 2. Defining the Phases (Time: Hours)
    t1, t2 = 3, 9
    freq = 2.0  
    
    # --- PHASE 1:Electromagnetic Decoherence (3 Hours) ---
    mask_before = t < t1
    y_before = np.exp(-0.05 * t[mask_before]) * np.sin(freq * t[mask_before]) + np.random.normal(0, 0.2, sum(mask_before))
    
    # --- PHASE 2: GDNF Receptor Blockade / Compression (6 Hours) ---
    mask_block = (t >= t1) & (t < t2)
    y_block = 0.4 * np.sin(25 * t[mask_block]) 
    
    # --- PHASE 3: Coherent Snap-Back / Integrated Childlike State ---
    mask_after = t >= t2
    y_after = 1.6 * np.sin(freq * (t[mask_after] - t2)) 

    # 3. VISUALIZATION
    purple_color = '#4B0082' # Indigo/Dark Purple for that whimsical feel
    
    plt.figure(figsize=(12, 6), facecolor='white')
    ax = plt.gca()
    
    # Plotting each phase
    plt.plot(t[mask_before], y_before, color='#FFBF00', lw=1.5, label="3hr: Electromagnetic Decoherence")
    plt.plot(t[mask_block], y_block, color='#800000', lw=2, label="6hr: Receptor Blockade (Compression)")
    plt.plot(t[mask_after], y_after, color='#FF69B4', lw=3, label="11hr: Childlike Coherence / Integrated Cognition")
    
    # Shading the 'Reboot' zone
    plt.axvspan(t1, t2, color='#800000', alpha=0.06)
    
    ax.set_xlim(0, 20) # This removes the gap at the origin
    ax.set_xmargin(0)
    
    # Whimsical Purple Text & Axes
    plt.title("Neural Phase Transition: The GDNF 'Running Reboot'", 
              fontsize=16, fontweight='bold', color=purple_color, family='sans-serif')
    plt.xlabel("Time (Hours)", fontsize=12, color=purple_color)
    plt.ylabel("Electromagnetic Coherence (μV)", fontsize=12, color=purple_color)
    
    # Styling the 'Ticks' and Spines in Purple
    ax.tick_params(axis='x', colors=purple_color)
    ax.tick_params(axis='y', colors=purple_color)
    ax.spines['bottom'].set_color(purple_color)
    ax.spines['left'].set_color(purple_color)
    
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.grid(axis='y', linestyle=':', alpha=0.3)
    plt.xticks(np.arange(0, 21, 1))
    
    legend = plt.legend(frameon=False, loc='upper left', fontsize=10)
    for text in legend.get_texts():
        text.set_color(purple_color) # Make legend text purple too
    
    plt.tight_layout()
    plt.show()

model_gdnf_temporal_reboot()
