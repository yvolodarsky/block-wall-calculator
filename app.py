import streamlit as st
import matplotlib.pyplot as plt
import math

# Truck capacity
truck_capacity = 45500

# Updated block sizes and weights
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

# Diagram function - Improved visual representation of lying down blocks
def plot_wall(full_blocks, half_blocks, rows, is_tapered):
    # Adjust figure size based on wall length
    scale_factor = max(10, length / 20)
    fig, ax = plt.subplots(figsize=(scale_factor, 6))
    y = 0
    for row in range(rows):
        x = 0
        # Staggered pattern for each row, even if tapered
        if row % 2 == 1:
            x += block_length / 2
        blocks_in_row = full_blocks if not is_tapered else max(1, full_blocks - row)
        for b in range(blocks_in_row):
            ax.add_patch(plt.Rectangle((x, y), block_length, block_height, edgecolor='black', facecolor='lightgray'))
            x += block_length
        # Add half blocks at the ends if necessary
        if half_blocks and row % 2 == 1:
            ax.add_patch(plt.Rectangle((x, y), block_length / 2, block_height, edgecolor='black', facecolor='darkgray'))
        y += block_height
    plt.xlim(0, length)
    plt.ylim(0, height)
    plt.title('Wall Diagram (Lying Down, Scaled)')
    plt.gca().set_aspect('auto')
    st.pyplot(fig)

# Calculation and display
if st.button('Calculate'):
    adjusted_height = (height - buried_height) // block_height + 1
    full_blocks = math.ceil(length / block_length)
    half_blocks = 2 if not is_tapered else 0
    rows = int(adjusted_height)
    total_weight = full_blocks * block_weight
    total_price = full_blocks * price_per_block
    total_trucks = math.ceil(total_weight / truck_capacity)

    st.write(f'Total Blocks: {full_blocks}')
    st.write(f'Half Blocks: {half_blocks}')
    st.write(f'Total Weight: {total_weight} lbs')
    st.write(f'Total Price: ${total_price:.2f}')
    st.write(f'Trucks Needed: {total_trucks}')

    plot_wall(full_blocks, half_blocks, rows, is_tapered)
