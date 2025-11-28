import streamlit as st
from streamlit.components.v1 import html

# Page config
st.set_page_config(
    page_title="Simple Interest Calculator",
    page_icon="💰",
    layout="centered"
)

# Custom CSS for modern UI/UX
st.markdown("""
    <style>
        body {
            background-color: #f5f7fa;
        }
        .main-title {
            font-size: 40px;
            font-weight: 700;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            color: #7f8c8d;
            font-size: 18px;
            margin-top: -10px;
            margin-bottom: 30px;
        }
        .card {
            background: white;
            padding: 30px;
            border-radius: 18px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            width: 100%;
        }
        .result-box {
            background: #2ecc71;
            color: white;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            font-size: 22px;
            font-weight: 600;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='main-title'>💰 Simple Interest Calculator</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>A clean and modern tool to calculate simple interest instantly</div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)

# Inputs arranged horizontally
col1, col2 = st.columns(2)
with col1:
    principal = st.number_input("💵 Principal Amount (P)", min_value=0.0, format="%.2f")
with col2:
    rate = st.number_input("📈 Rate of Interest (R %)", min_value=0.0, format="%.2f")

time = st.number_input("🕒 Time Period (T in years)", min_value=0.0, format="%.2f")

# Calculate button
calculate = st.button("Calculate Interest", type="primary")

# Show result
if calculate:
    si = (principal * rate * time) / 100

    st.markdown(
        f"<div class='result-box'>Simple Interest: ₹{si:.2f}</div>",
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <br><p style='text-align:center; color:#95a5a6;'>
    Made with ❤️ using Streamlit
    </p>
""", unsafe_allow_html=True)
