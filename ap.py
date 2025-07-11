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
    if all(name.strip() for name in [a1_name, a2_name, b1_name, b2_name]):
        team_a_total = a1_hcp + a2_hcp
        team_b_total = b1_hcp + b2_hcp

        st.subheader("📊 Handicap Summary")
        st.markdown(f"**{a1_name} + {a2_name}**: {team_a_total} combined handicap")
        st.markdown(f"**{b1_name} + {b2_name}**: {team_b_total} combined handicap")

        if team_a_total == team_b_total:
            st.info("Handicaps are equal. No strokes are given.")
        else:
            higher_team = "Team A" if team_a_total > team_b_total else "Team B"
            stroke_team = [a1_name, a2_name] if higher_team == "Team A" else [b1_name, b2_name]
            diff = abs(team_a_total - team_b_total)
            strokes = round((3 / 8) * diff)

            stroke_holes = [hole for hole, _ in holes_by_index[:strokes]]

            st.success(f"🎯 {higher_team} receives **{strokes} stroke(s)**")
            st.markdown(f"These strokes are applied to the following holes:")
            st.markdown(", ".join(f"Hole {h}" for h in stroke_holes))
            st.markdown(f"Players receiving strokes: **{stroke_team[0]}** and **{stroke_team[1]}**")
    else:
        st.warning("Please enter all player names to calculate strokes.")




