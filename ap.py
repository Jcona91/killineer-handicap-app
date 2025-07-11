import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="Killineer Handicap Calculator", layout="centered")

# Load and display logo
logo = Image.open("logo.png")
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
    with col1:
        a1_name = st.text_input("Enter name for Team A - Player 1", placeholder="e.g. John")
        a1_hcp = st.number_input("Handicap for Player 1", min_value=-3, max_value=25, value=0, step=1, key="a1")
    with col2:
        a2_name = st.text_input("Enter name for Team A - Player 2", placeholder="e.g. Sarah")
        a2_hcp = st.number_input("Handicap for Player 2", min_value=-3, max_value=25, value=0, step=1, key="a2")

    st.markdown("### Team B")
    col3, col4 = st.columns(2)
    with col3:
        b1_name = st.text_input("Enter name for Team B - Player 1", placeholder="e.g. Mike")
        b1_hcp = st.number_input("Handicap for Player 1", min_value=-3, max_value=25, value=0, step=1, key="b1")
    with col4:
        b2_name = st.text_input("Enter name for Team B - Player 2", placeholder="e.g. Emma")
        b2_hcp = st.number_input("Handicap for Player 2", min_value=-3, max_value=25, value=0, step=1, key="b2")

# Calculate and display strokes
if st.button("📊 Calculate Handicap Allowance"):
    players = {
        a1_name: a1_hcp,
        a2_name: a2_hcp,
        b1_name: b1_hcp,
        b2_name: b2_hcp
    }

    if all(name.strip() for name in players.keys()):
        min_handicap = min(players.values())
        st.subheader("📊 Stroke Allocation")

        for name, hcap in players.items():
            strokes_given = hcap - min_handicap
            if strokes_given > 0:
                stroke_holes = [hole for hole, _ in holes_by_index[:strokes_given]]
                st.markdown(f"**{name}** receives **{strokes_given} stroke(s)** on:")
                st.markdown(", ".join(f"Hole {h}" for h in stroke_holes))
            else:
                st.markdown(f"**{name}** is the scratch player and receives **no strokes**.")
    else:
        st.warning("Please enter all player names to calculate strokes.")



