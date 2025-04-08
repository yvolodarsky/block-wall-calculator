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

# Select calculation mode
mode = st.selectbox('Choose Input Mode:', ['Wall Dimensions', 'Total Block Count'])

# Block selection
block_category = st.selectbox('Select Block Category:', list(block_sizes.keys()))
block_type = st.selectbox('Select Block Size:', list(block_sizes[block_category].keys()))
price_per_block = st.number_input('Price per Block:', min_value=0.0)

block_length = block_sizes[block_category][block_type]['length']
block_height = block_sizes[block_category][block_type]['height']
block_weight = block_sizes[block_category][block_type]['weight']
truck_capacity = 45500

if mode == 'Wall Dimensions':
    length = st.number_input('Wall Length (feet):', min_value=1)
    height = st.number_input('Wall Height (feet):', min_value=1)
    is_tapered = st.checkbox('Tapered Wall')

    if st.button('Calculate'):
        adjusted_height = math.ceil(height / block_height)
        full_blocks = math.ceil(length / block_length)
        rows = int(adjusted_height)
        total_blocks = []

        for row in range(rows):
            if is_tapered:
                tapered_blocks = max(1, full_blocks - 2 * row)
                total_blocks.append(tapered_blocks)
            else:
                total_blocks.append(full_blocks)

        total_full_blocks = sum(total_blocks)
        total_weight = total_full_blocks * block_weight
        total_price = total_full_blocks * price_per_block
        total_trucks = math.ceil(total_weight / truck_capacity)

        st.write(f'Total Blocks: {total_full_blocks}')
        st.write(f'Total Rows: {rows}')
        st.write(f'Total Weight: {total_weight} lbs')
        st.write(f'Total Price: ${total_price:.2f}')
        st.write(f'Trucks Needed: {total_trucks}')

elif mode == 'Total Block Count':
    block_count = st.number_input('Enter Total Number of Blocks:', min_value=1)
    if st.button('Calculate Total Price'):
        total_weight = block_count * block_weight
        total_price = block_count * price_per_block
        total_trucks = math.ceil(total_weight / truck_capacity)

        st.write(f'Total Blocks: {block_count}')
        st.write(f'Total Weight: {total_weight} lbs')
        st.write(f'Total Price: ${total_price:.2f}')
        st.write(f'Trucks Needed: {total_trucks}')
