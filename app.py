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

# Diagram function - Horizontal Orientation, Staggered or Tapered
def plot_wall(full_blocks, half_blocks, rows, is_tapered):
    fig, ax = plt.subplots(figsize=(12, 6))
    y = 0
    for row in range(rows):
        x = 0
        if row % 2 == 1 and not is_tapered:  # Staggered row
            x += block_length / 2  # Start with half block shift
        for b in range(full_blocks):
            ax.add_patch(plt.Rectangle((x, y), block_length, block_height, edgecolor='black', facecolor='lightgray'))
            x += block_length
        if row % 2 == 1 and not is_tapered:  # End with half block on staggered rows
            ax.add_patch(plt.Rectangle((x, y), block_length / 2, block_height, edgecolor='black', facecolor='darkgray'))
        y += block_height
    plt.xlim(0, length)
    plt.ylim(0, height)
    plt.title('Wall Diagram (Lying Down, Staggered/Tapered)')
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
