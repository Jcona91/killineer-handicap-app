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

# Handicap options from -3 to 25 with display labels
handicap_options = list(range(-3, 26))
handicap_labels = [f"Plus {abs(h)}" if h < 0 else str(h) for h in handicap_options]
handicap_dict = dict(zip(handicap_labels, handicap_options))

with st.expander("📋 Enter Player Names and Handicaps", expanded=True):
    st.markdown("### Team A")
    col1, col2 = st.columns(2)
    with col1:
        a1_name = st.text_input("Enter name for Team A - Player 1", placeholder="e.g. John")
        a1_label = st.selectbox("Handicap for Player 1", handicap_labels, index=handicap_options.index(0), key="a1")
        a1_hcp = handicap_dict[a1_label]
    with col2:
        a2_name = st.text_input("Enter name for Team A - Player 2", placeholder="e.g. Sarah")
        a2_label = st.selectbox("Handicap for Player 2", handicap_labels, index=handicap_options.index(0), key="a2")
        a2_hcp = handicap_dict[a2_label]

    st.markdown("### Team B")
    col3, col4 = st.columns(2)
    with col3:
        b1_name = st.text_input("Enter name for Team B - Player 1", placeholder="e.g. Mike")
        b1_label = st.selectbox("Handicap for Player 1", handicap_labels, index=handicap_options.index(0), key="b1")
        b1_hcp = handicap_dict[b1_label]
    with col4:
        b2_name = st.text_input("Enter name for Team B - Player 2", placeholder="e.g. Emma")
        b2_label = st.selectbox("Handicap for Player 2", handicap_labels, index=handicap_options.index(0), key="b2")
        b2_hcp = handicap_dict[b2_label]

if st.button("📊 Calculate Handicap Allowance"):
    team_a_total = a1_hcp + a2_hcp
    team_b_total = b1_hcp + b2_hcp
    diff = abs(team_a_total - team_b_total)
    allowance = round((3 / 8) * diff)

    if team_a_total > team_b_total:
        receiving_team = "Team A"
        receiving_players = f"{a1_name} & {a2_name}"
    elif team_b_total > team_a_total:
        receiving_team = "Team B"
        receiving_players = f"{b1_name} & {b2_name}"
    else:
        receiving_team = None

    st.markdown("---")
    st.subheader("📈 Match Summary")
    st.write(f"**{a1_name} + {a2_name} Handicap Total:** {team_a_total}")
    st.write(f"**{b1_name} + {b2_name} Handicap Total:** {team_b_total}")
    st.write(f"**Handicap Difference:** {diff}")
    st.write(f"**3/8 of Difference (Rounded):** {allowance}")

    if receiving_team and allowance > 0:
        st.success(f"✅ {receiving_team} ({receiving_players}) receives **{allowance} stroke(s)**.")
        stroke_holes = [hole for hole, _ in holes_by_index[:allowance]]
        st.markdown("**Apply strokes on these holes (lowest stroke index):**")
        st.markdown(", ".join(f"Hole {h}" for h in stroke_holes))
    else:
        st.info("No strokes are given. Handicaps are equal or allowance is zero.")




