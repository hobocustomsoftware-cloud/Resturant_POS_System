import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(16, 12))
ax.set_xlim(0, 16)
ax.set_ylim(0, 12)
ax.axis('off')

# Title
ax.text(8, 11.5, 'Restaurant POS System - Architecture Flow', ha='center', va='center', fontsize=20, fontweight='bold')

# Client Apps
web = FancyBboxPatch((1, 9), 3, 1, boxstyle="round,pad=0.1", facecolor='#e3f2fd', edgecolor='#1976d2')
ax.add_patch(web)
ax.text(2.5, 9.5, 'Web App\nReact/Vite', ha='center', va='center', fontsize=9)

mob = FancyBboxPatch((5, 9), 3, 1, boxstyle="round,pad=0.1", facecolor='#f3e5f5', edgecolor='#7b1fa2')
ax.add_patch(mob)
ax.text(6.5, 9.5, 'Mobile App\nReact Native', ha='center', va='center', fontsize=9)

desk = FancyBboxPatch((9, 9), 3, 1, boxstyle="round,pad=0.1", facecolor='#e8f5e9', edgecolor='#388e3c')
ax.add_patch(desk)
ax.text(10.5, 9.5, 'Desktop App\nElectron', ha='center', va='center', fontsize=9)

# Backend
api = FancyBboxPatch((4.5, 6.5), 4, 1.2, boxstyle="round,pad=0.1", facecolor='#fff3e0', edgecolor='#f57c00')
ax.add_patch(api)
ax.text(6.5, 7.1, 'Django REST API\n+ JWT Auth', ha='center', va='center', fontsize=10, fontweight='bold')

ws = FancyBboxPatch((9.5, 6.5), 2.5, 1.2, boxstyle="round,pad=0.1", facecolor='#fce4ec', edgecolor='#c2185b')
ax.add_patch(ws)
ax.text(10.75, 7.1, 'WebSocket\nChannels', ha='center', va='center', fontsize=9)

# Data Layer
db = FancyBboxPatch((2, 4), 2.5, 1, boxstyle="round,pad=0.1", facecolor='#efebe9', edgecolor='#6d4c41')
ax.add_patch(db)
ax.text(3.25, 4.5, 'PostgreSQL', ha='center', va='center', fontsize=9)

redis = FancyBboxPatch((5.5, 4), 2.5, 1, boxstyle="round,pad=0.1", facecolor='#ffcdd2', edgecolor='#d32f2f')
ax.add_patch(redis)
ax.text(6.75, 4.5, 'Redis', ha='center', va='center', fontsize=9)

media = FancyBboxPatch((9, 4), 2.5, 1, boxstyle="round,pad=0.1", facecolor='#e0f2f1', edgecolor='#00796b')
ax.add_patch(media)
ax.text(10.25, 4.5, 'Media Storage', ha='center', va='center', fontsize=9)

# Features
feat1 = FancyBboxPatch((1, 1.5), 2.5, 0.8, boxstyle="round,pad=0.05", facecolor='#f1f8e9', edgecolor='#689f38')
ax.add_patch(feat1)
ax.text(2.25, 1.9, 'POS & Orders', ha='center', va='center', fontsize=8)

feat2 = FancyBboxPatch((4, 1.5), 2.5, 0.8, boxstyle="round,pad=0.05", facecolor='#f1f8e9', edgecolor='#689f38')
ax.add_patch(feat2)
ax.text(5.25, 1.9, 'KDS Real-time', ha='center', va='center', fontsize=8)

feat3 = FancyBboxPatch((7, 1.5), 2.5, 0.8, boxstyle="round,pad=0.05", facecolor='#f1f8e9', edgecolor='#689f38')
ax.add_patch(feat3)
ax.text(8.25, 1.9, 'Inventory', ha='center', va='center', fontsize=8)

feat4 = FancyBboxPatch((10, 1.5), 2.5, 0.8, boxstyle="round,pad=0.05", facecolor='#f1f8e9', edgecolor='#689f38')
ax.add_patch(feat4)
ax.text(11.25, 1.9, 'Billing & Trial', ha='center', va='center', fontsize=8)

feat5 = FancyBboxPatch((13, 1.5), 2, 0.8, boxstyle="round,pad=0.05", facecolor='#f1f8e9', edgecolor='#689f38')
ax.add_patch(feat5)
ax.text(14, 1.9, 'Reports', ha='center', va='center', fontsize=8)

# Arrows
arrow_props = dict(arrowstyle='->', lw=1.5, color='#424242')
plt.annotate('', xy=(3.25, 9), xytext=(3.25, 8.2), arrowprops=arrow_props)
plt.annotate('', xy=(6.5, 9), xytext=(6.5, 7.7), arrowprops=arrow_props)
plt.annotate('', xy=(9.75, 9), xytext=(9, 7.7), arrowprops=arrow_props)
plt.annotate('', xy=(5.5, 6.5), xytext=(4, 5), arrowprops=arrow_props)
plt.annotate('', xy=(6.5, 6.5), xytext=(6.75, 5), arrowprops=arrow_props)
plt.annotate('', xy=(7.5, 6.5), xytext=(9, 5), arrowprops=arrow_props)
plt.annotate('', xy=(10.75, 6.5), xytext=(10.75, 5), arrowprops=arrow_props)

plt.savefig('/workspace/app/architecture_diagram.png', dpi=300, bbox_inches='tight', facecolor='white')
print('Done')
