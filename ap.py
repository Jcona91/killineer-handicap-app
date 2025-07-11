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

with st.expander("📋 Enter Player Names and Handicaps", expanded=True):
    st.markdown("### Team A")
    col1, col2 = st.columns(2)
    with col1:
        a1_name = st.text_input("Enter name for Team A - Player 1", placeholder="e.g. John")
        a1_hcp = st.number_input("Handicap for Player 1", min_value=-10.0, max_value=54.0, value=0.0, step=0.1, key="a1")
        a1_hcp = st.number_input("Handicap for Player 1", min_value=-10, max_value=54, value=0, step=1, key="a1")
    with col2:
        a2_name = st.text_input("Enter name for Team A - Player 2", placeholder="e.g. Sarah")
        a2_hcp = st.number_input("Handicap for Player 2", min_value=-10.0, max_value=54.0, value=0.0, step=0.1, key="a2")
        a2_hcp = st.number_input("Handicap for Player 2", min_value=-10, max_value=54, value=0, step=1, key="a2")

    st.markdown("### Team B")
    col3, col4 = st.columns(2)
    with col3:
        b1_name = st.text_input("Enter name for Team B - Player 1", placeholder="e.g. Mike")
        b1_hcp = st.number_input("Handicap for Player 1", min_value=-10.0, max_value=54.0, value=0.0, step=0.1, key="b1")
        b1_hcp = st.number_input("Handicap for Player 1", min_value=-10, max_value=54, value=0, step=1, key="b1")
    with col4:
        b2_name = st.text_input("Enter name for Team B - Player 2", placeholder="e.g. Emma")
        b2_hcp = st.number_input("Handicap for Player 2", min_value=-10.0, max_value=54.0, value=0.0, step=0.1, key="b2")
        b2_hcp = st.number_input("Handicap for Player 2", min_value=-10, max_value=54, value=0, step=1, key="b2")

if st.button("📊 Calculate Handicap Allowance"):
    team_a_total = a1_hcp + a2_hcp
@@ -66,3 +66,4 @@
        st.info("No strokes are given. Handicaps are equal or allowance is zero.")
else:
    st.info("Please enter all player names to calculate strokes.")

