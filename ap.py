import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="Killineer Handicap Calculator", layout="centered")

# Load and display logo
logo = Image.open("logo.png")  # Ensure 'logo.png' is in the same directory
st.image(logo, width=200)

# Title
st.title("🏌️ Killineer Doubles Match Play Handicap Calculator")

# Killineer stroke index mapping
stroke_index = {
    1: 18, 2: 5, 3: 13, 4: 3, 5: 17, 6: 6, 7: 7, 8: 9, 9: 11,
    10: 8, 11: 12, 12: 10, 13: 4, 14: 14, 15: 1, 16: 15, 17: 16, 18: 2
}

# Sort holes by stroke index (lowest first)
holes_by_index = sorted(stroke_index.items(), key=lambda x: x[1])

# Player input section
with st.expander("📋 Enter Player Names and Handicaps", expanded=True):
    st.markdown("### Team A")
    col1, col2 = st.columns(2)
    player_a1 = col1.text_input("Player A1 Name")
    handicap_a1 = col1.number_input("Player A1 Handicap", min_value=0, max_value=54, value=0)
    player_a2 = col2.text_input("Player A2 Name")
    handicap_a2 = col2.number_input("Player A2 Handicap", min_value=0, max_value=54, value=0)

    st.markdown("### Team B")
    col3, col4 = st.columns(2)
    player_b1 = col3.text_input("Player B1 Name")
    handicap_b1 = col3.number_input("Player B1 Handicap", min_value=0, max_value=54, value=0)
    player_b2 = col4.text_input("Player B2 Name")
    handicap_b2 = col4.number_input("Player B2 Handicap", min_value=0, max_value=54, value=0)

# Handicap calculation logic (placeholder)
# You can add your logic here to calculate strokes given based on lowest handicap, etc.
