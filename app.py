import streamlit as st
import matplotlib.pyplot as plt
import math

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

truck_capacity = 45500

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

# Diagram function
def plot_wall(full_blocks, half_blocks, rows):
    fig, ax = plt.subplots(figsize=(12, 6))
    y = 0
    for row in range(rows):
        x = 0
        for b in range(full_blocks):
            ax.add_patch(plt.Rectangle((x, y), block_length, block_height, edgecolor='black', facecolor='lightgray'))
            x += block_length
        y += block_height
    plt.xlim(0, length)
    plt.ylim(0, height)
    plt.title('Wall Diagram')
    st.pyplot(fig)

# Calculation and display
if st.button('Calculate'):
    adjusted_height = (height - buried_height) // block_height + 1
    full_blocks = math.ceil(length / block_length)
    rows = int(adjusted_height)
    half_blocks = 2 if not is_tapered and rows > 1 else 0
    total_weight = (full_blocks * block_weight) + (half_blocks * (block_weight / 2))
    total_price = (full_blocks * price_per_block) + (half_blocks * (price_per_block / 2))
    total_trucks = math.ceil(total_weight / truck_capacity)

    st.write(f'Total Blocks: {full_blocks + half_blocks}')
    st.write(f'Full Blocks: {full_blocks}')
    st.write(f'Half Blocks: {half_blocks}')
    st.write(f'Total Weight: {total_weight} lbs')
    st.write(f'Total Price: ${total_price:.2f}')
    st.write(f'Trucks Needed: {total_trucks}')

    plot_wall(full_blocks, half_blocks, rows)
