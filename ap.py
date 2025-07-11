import streamlit as st
from PIL import Image

# Load and display logo
logo = Image.open("logo.png")  # Ensure 'logo.png' is in the same directory
st.set_page_config(page_title="Killineer Handicap Calculator", layout="centered")
st.image(logo, width=200)
st.title("🏌️ Killineer Doubles Match Play Handicap Calculator")

# Killineer stroke index mapping
stroke_index = {
    1: 18, 2: 5, 3: 13, 4: 3, 5: 17, 6: 6, 7: 7, 8: 9, 9: 11,
    10: 8, 11: 12, 12: 10, 13: 4, 14: 14, 15: 1, 16: 15, 17: 16, 18: 2
}

# Sort holes by stroke index (lowest first)
holes_by_index = sorted(stroke_index.items(), key=lambda x: x[1])

# Format handicap for display
def format_handicap(hcp):
    return f"Plus {abs(hcp)}" if hcp < 0 else str(hcp)

with st.expander("📋 Enter Player Names and Handicaps", expanded=True):
    st.markdown("### Team A")
    col1, col2 = st.columns(2)
    with col1:
        a1_name = st.text_input("Enter name for Team A - Player 1", placeholder="e.g. John")
        a1_hcp = st.number_input("Handicap for Player 1", min_value=-3, max_value=25, value=0, step=1, key="a
