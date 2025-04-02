import streamlit as st
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

truck_capacity = 45500  # Max weight per truck in lbs

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

# Calculate number of blocks
def calculate_blocks():
    adjusted_height = (height - buried_height) // block_height + 1
    total_full_blocks = 0
    total_half_blocks = 0

    for row in range(int(adjusted_height)):
        blocks_in_row = -(-length // block_length)  # Ceiling division
        if is_tapered:
            blocks_in_row = max(1, blocks_in_row - row * 2)
        if not is_tapered and row % 2 == 1:  # Staggered non-tapered rows
            total_half_blocks += 2
        total_full_blocks += blocks_in_row

    total_blocks = total_full_blocks + total_half_blocks
    total_weight = (total_full_blocks * block_weight) + (total_half_blocks * (block_weight / 2))
    total_price = (total_full_blocks * price_per_block) + (total_half_blocks * (price_per_block / 2))
    total_trucks = math.ceil(total_weight / truck_capacity)
    return total_blocks, total_full_blocks, total_half_blocks, total_weight, total_price, total_trucks

if st.button('Calculate'):
    total_blocks, full_blocks, half_blocks, total_weight, total_price, total_trucks = calculate_blocks()
    st.write(f'Total Blocks: {total_blocks}')
    st.write(f'Full Blocks: {full_blocks}')
    st.write(f'Half Blocks: {half_blocks}')
    st.write(f'Total Weight: {total_weight} lbs')
    st.write(f'Total Price: ${total_price:.2f}')
    st.write(f'Trucks Needed: {total_trucks}')
