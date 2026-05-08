import matplotlib.pyplot as plt
import numpy as np

def draw_pitch(ax=None, pitch_dims=(105, 68), theme='dark'):
    if ax is None: fig, ax = plt.subplots(figsize=(12, 8))
    line_color = '#ffffff' if theme == 'dark' else '#000000'
    pitch_color = '#0e1117' if theme == 'dark' else '#ffffff'
    grass_color = '#1a1d23' if theme == 'dark' else '#f0f2f6'
    
    ax.set_facecolor(pitch_color)
    length, width = pitch_dims
    
    # Grass Pattern (Zoning)
    for i in range(0, int(length), 10):
        color = grass_color if (i//10) % 2 == 0 else pitch_color
        ax.axvspan(i, min(i+10, length), color=color, alpha=0.3, zorder=0)

    # Pitch Outline
    ax.plot([0, 0, length, length, 0], [0, width, width, 0, 0], color=line_color, lw=3, zorder=1)
    ax.plot([length/2, length/2], [0, width], color=line_color, lw=3, zorder=1)
    
    # Centre Circle
    centre_circle = plt.Circle((length/2, width/2), 9.15, color=line_color, fill=False, lw=3, zorder=1)
    ax.add_patch(centre_circle)
    centre_spot = plt.Circle((length/2, width/2), 0.5, color=line_color, zorder=1)
    ax.add_patch(centre_spot)
    
    # Penalty Areas
    ax.plot([0, 16.5, 16.5, 0], [width/2-20, width/2-20, width/2+20, width/2+20], color=line_color, lw=3, zorder=1)
    ax.plot([length, length-16.5, length-16.5, length], [width/2-20, width/2-20, width/2+20, width/2+20], color=line_color, lw=3, zorder=1)
    
    # Goal Areas
    ax.plot([0, 5.5, 5.5, 0], [width/2-9, width/2-9, width/2+9, width/2+9], color=line_color, lw=2, zorder=1)
    ax.plot([length, length-5.5, length-5.5, length], [width/2-9, width/2-9, width/2+9, width/2+9], color=line_color, lw=2, zorder=1)

    ax.set_xlim(-2, length+2)
    ax.set_ylim(-2, width+2)
    ax.set_aspect('equal')
    ax.axis('off')
    return ax

def plot_positions(player_coords, team_name="Team", ax=None, color='#00ff00'):
    if ax is None: ax = draw_pitch()
    coords = np.array(player_coords)
    ax.scatter(coords[:, 0], coords[:, 1], color=color, s=200, edgecolors='white', zorder=5, label=team_name)
    for i, (x, y) in enumerate(player_coords):
        ax.annotate(str(i+1), (x, y), color='white', weight='bold', ha='center', va='center', zorder=6)
    return ax
