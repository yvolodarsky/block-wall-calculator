import streamlit as st
import matplotlib.pyplot as plt
import math

# Truck capacity
truck_capacity = 45500

# Updated block sizes and weights including all block types
block_sizes = {
    'V-Wedge Blocks': {
        '6x2x2': {'length': 6, 'height': 2, 'weight': 3500},
        '5x2x2': {'length': 5, 'height': 2, 'weight': 3000},
        '4x2x2': {'length': 4, 'height': 2, 'weight': 2500},
        '3x2x2': {'length': 3, 'height': 2, 'weight': 1750},
        '2x2x2': {'length': 2, 'height': 2, 'weight': 1200}
    },
    'Lego Blocks': {
        '5x2.5x2.5': {'length': 5, 'height': 2.5, 'weight': 4000},
        '60x30x30': {'length': 5, 'height': 2.5, 'weight': 4000},
        '2.5x2.5x2.5': {'length': 2.5, 'height': 2.5, 'weight': 2000},
        '30x30x30': {'length': 2.5, 'height': 2.5, 'weight': 2000},
        '6x2x2': {'length': 6, 'height': 2, 'weight': 3500},
        '3x2x2': {'length': 3, 'height': 2, 'weight': 1750}
    },
    'Knob Blocks': {
        '4x2x2': {'length': 4, 'height': 2, 'weight': 2500},
        '2x2x2': {'length': 2, 'height': 2, 'weight': 1200}
    },
    'Dome Blocks': {
        '6x2x2': {'length': 6, 'height': 2, 'weight': 3500},
        '4x2x2': {'length': 4, 'height': 2, 'weight': 2500}
    },
    'Castle (Benton) Blocks': {
        '6x2x2': {'length': 6, 'height': 2, 'weight': 3500},
        '3x2x2': {'length': 3, 'height': 2, 'weight': 1750}
    },
    'Flat Blocks': {
        '8x2x2': {'length': 8, 'height': 2, 'weight': 4500},
        '6x2x2': {'length': 6, 'height': 2, 'weight': 3500},
        '4x2x2': {'length': 4, 'height': 2, 'weight': 2500},
        '3x2x2': {'length': 3, 'height': 2, 'weight': 1750}
    }
}

st.title('Concrete Block Wall Calculator')

# Input fields
block_category = st.selectbox('Select Block Category:', list(block_sizes.keys()))
block_type = st.selectbox('Select Block Size:', list(block_sizes[block_category].keys()))
length = st.number_input('Wall Length (feet):', min_value=1)
height = st.number_input('Wall Height (feet):', min_value=1)
is_tapered = st.checkbox('Tapered Wall')
price_per_block = st.number_input('Price per Block:', min_value=0.0)

block_length = block_sizes[block_category][block_type]['length']
block_height = block_sizes[block_category][block_type]['height']
block_weight = block_sizes[block_category][block_type]['weight']
buried_height = 1

# Diagram function - Corrected tapered wall display for both sides
def plot_wall(total_blocks, rows, is_tapered):
    scale_factor = max(20, length / 10)
    fig, ax = plt.subplots(figsize=(scale_factor, 6))
    y = 0
    block_number = 1
    for row in range(rows):
        x = 0
        blocks_in_row = total_blocks[row]
        if is_tapered:
            x += block_length / 2 * row
        for b in range(blocks_in_row):
            ax.add_patch(plt.Rectangle((x, y), block_length, block_height, edgecolor='black', facecolor='lightgray'))
            ax.text(x + block_length / 2, y + block_height / 2, str(block_number), ha='center', va='center', fontsize=8, color='black')
            block_number += 1
            x += block_length
        # Correct the right side missing block issue
        if is_tapered and (blocks_in_row < total_blocks[0]):
            ax.add_patch(plt.Rectangle((x, y), block_length, block_height, edgecolor='black', facecolor='lightgray'))
            ax.text(x + block_length / 2, y + block_height / 2, str(block_number), ha='center', va='center', fontsize=8, color='black')
            block_number += 1
        y += block_height
    plt.xlim(0, max(length, block_length * max(total_blocks)))
    plt.ylim(0, block_height * rows)
    plt.title(f'Wall Diagram ({block_category} - {block_type})')
    plt.gca
