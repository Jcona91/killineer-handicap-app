import streamlit as st

# Killineer stroke index mapping
stroke_index = {
    1: 18, 2: 5, 3: 13, 4: 3, 5: 17, 6: 6, 7: 7, 8: 9, 9: 11,
    10: 8, 11: 12, 12: 10, 13: 4, 14: 14, 15: 1, 16: 15, 17: 16, 18: 2
}

# Sort holes by stroke index (lowest first)
holes_by_index = sorted(stroke_index.items(), key=lambda x: x[1])

st.set_page_config(page_title="Killineer Handicap Calculator", layout="centered")
st.title("🏌️ Killineer Doubles Match Play Handicap Calculator")

st.markdown("Enter the handicaps for each player on both teams:")

# Team A
st.header("Team A")
a1 = st.number_input("Team A - Player 1 Handicap", min_value=0, max_value=54, value=12, key="a1")
a2 = st.number_input("Team A - Player 2 Handicap", min_value=0, max_value=54, value=12, key="a2")

# Team B
st.header("Team B")
b1 = st.number_input("Team B - Player 1 Handicap", min_value=0, max_value=54, value=4, key="b1")
b2 = st.number_input("Team B - Player 2 Handicap", min_value=0, max_value=54, value=4, key="b2")

if st.button("Calculate Handicap Allowance"):
    team_a_total = a1 + a2
    team_b_total = b1 + b2
    diff = abs(team_a_total - team_b_total)
    allowance = round((3 / 8) * diff)

    if team_a_total > team_b_total:
        receiving_team = "Team B"
    elif team_b_total > team_a_total:
        receiving_team = "Team A"
    else:
        receiving_team = None

    st.subheader("📊 Results")
    st.write(f"**Team A Total Handicap:** {team_a_total}")
    st.write(f"**Team B Total Handicap:** {team_b_total}")
    st.write(f"**Handicap Difference:** {diff}")
    st.write(f"**3/8 of Difference (Rounded):** {allowance}")

    if receiving_team and allowance > 0:
        st.success(f"✅ {receiving_team} receives **{allowance} stroke(s)**.")
        stroke_holes = [hole for hole, _ in holes_by_index[:allowance]]
        st.write("Apply strokes on the following holes (lowest stroke index):")
        st.write(", ".join(f"Hole {h}" for h in stroke_holes))
    else:
        st.info("No strokes are given. Handicaps are equal or allowance is zero.")
