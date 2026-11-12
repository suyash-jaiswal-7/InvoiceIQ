import streamlit as st
from inferencing.predict_freight import predict_freight_cost
from inferencing.predict_invoice_flag import predict_invoice_flag


# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="INVOICE IQ",
    page_icon="📦",
    layout="wide"
)


# =========================================================
# Custom Styling (Aesthetics only)
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --primary: #4F46E5;
    --primary-dark: #3730A3;
    --accent: #0EA5E9;
    --teal: #14B8A6;
    --bg: #F5F7FB;
    --card: #FFFFFF;
    --text: #1E293B;
    --muted: #64748B;
    --border: #E2E8F0;
    --danger: #E11D48;
    --success: #059669;
}

html, body, [class*="css"], .stApp {
    font-family: 'Inter', sans-serif;
    color: var(--text);
}

.stApp {
    background:
        radial-gradient(circle at 10% 0%, #E0E7FF 0%, transparent 35%),
        radial-gradient(circle at 95% 10%, #CCFBF1 0%, transparent 30%),
        var(--bg);
}

/* Hide default Streamlit chrome */
#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent; }

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1150px;
}

/* ---------- Hero ---------- */
.hero {
    background: linear-gradient(135deg, #4F46E5 0%, #6366F1 45%, #0EA5E9 100%);
    border-radius: 24px;
    padding: 2.6rem 2.8rem;
    color: white;
    box-shadow: 0 20px 45px -15px rgba(79, 70, 229, 0.55);
    position: relative;
    overflow: hidden;
    margin-bottom: 1.6rem;
}
.hero::after {
    content: "";
    position: absolute;
    right: -60px; top: -60px;
    width: 260px; height: 260px;
    background: rgba(255,255,255,0.12);
    border-radius: 50%;
}
.hero::before {
    content: "";
    position: absolute;
    right: 120px; bottom: -90px;
    width: 200px; height: 200px;
    background: rgba(255,255,255,0.08);
    border-radius: 50%;
}
.hero h1 {
    font-size: 2.6rem;
    font-weight: 800;
    letter-spacing: -0.5px;
    margin: 0 0 0.3rem 0;
    color: white;
}
.hero p.sub {
    font-size: 1.15rem;
    font-weight: 500;
    opacity: 0.95;
    margin: 0 0 0.6rem 0;
}
.hero p.desc {
    font-size: 0.95rem;
    opacity: 0.85;
    margin: 0;
    max-width: 640px;
}

/* ---------- Feature cards ---------- */
.feature-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 1.3rem 1.4rem;
    box-shadow: 0 4px 14px -6px rgba(15, 23, 42, 0.08);
    height: 100%;
    transition: all 0.25s ease;
}
.feature-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 14px 28px -12px rgba(79, 70, 229, 0.3);
    border-color: #C7D2FE;
}
.feature-icon {
    width: 46px; height: 46px;
    border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.4rem;
    margin-bottom: 0.8rem;
    background: linear-gradient(135deg, #EEF2FF, #E0E7FF);
}
.feature-card h4 {
    margin: 0 0 0.25rem 0;
    font-size: 1.02rem;
    font-weight: 700;
    color: var(--text);
}
.feature-card p {
    margin: 0;
    font-size: 0.88rem;
    color: var(--muted);
    line-height: 1.5;
}

/* ---------- Section header ---------- */
.section-title {
    display: flex; align-items: center; gap: 0.7rem;
    font-size: 1.6rem; font-weight: 800;
    color: var(--text);
    margin: 0.4rem 0 0.2rem 0;
}
.section-title .pill {
    font-size: 0.7rem; font-weight: 700;
    background: #EEF2FF; color: var(--primary);
    padding: 0.25rem 0.7rem;
    border-radius: 999px;
    letter-spacing: 0.6px;
    text-transform: uppercase;
}
.objective-box {
    background: linear-gradient(90deg, #EEF2FF 0%, #F0FDFA 100%);
    border-left: 4px solid var(--primary);
    border-radius: 12px;
    padding: 1rem 1.2rem;
    margin: 0.8rem 0 1.4rem 0;
    color: #334155;
    font-size: 0.95rem;
    line-height: 1.55;
}
.objective-box b.label {
    color: var(--primary-dark);
    text-transform: uppercase;
    font-size: 0.75rem;
    letter-spacing: 0.8px;
    display: block;
    margin-bottom: 0.2rem;
}

/* ---------- Form card ---------- */
[data-testid="stForm"] {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 1.8rem 1.8rem 1.4rem 1.8rem;
    box-shadow: 0 10px 30px -14px rgba(15, 23, 42, 0.15);
}

/* Inputs */
[data-testid="stNumberInput"] label p {
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    color: #334155 !important;
}
[data-testid="stNumberInput"] input {
    border-radius: 10px;
    font-weight: 600;
    color: var(--text);
}
[data-testid="stNumberInput"] > div > div {
    border-radius: 12px !important;
    border: 1.5px solid var(--border) !important;
    background: #F8FAFC;
    transition: all 0.2s ease;
}
[data-testid="stNumberInput"] > div > div:focus-within {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.12);
    background: white;
}

/* Buttons */
.stButton > button, [data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg, #4F46E5, #6366F1);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.7rem 1.8rem;
    font-weight: 700;
    font-size: 0.98rem;
    letter-spacing: 0.2px;
    box-shadow: 0 8px 20px -8px rgba(79, 70, 229, 0.7);
    transition: all 0.2s ease;
}
.stButton > button:hover, [data-testid="stFormSubmitButton"] > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 24px -8px rgba(79, 70, 229, 0.8);
    background: linear-gradient(135deg, #4338CA, #4F46E5);
    color: white;
    border: none;
}

/* ---------- Metric ---------- */
[data-testid="stMetric"] {
    background: linear-gradient(135deg, #FFFFFF 0%, #F5F3FF 100%);
    border: 1px solid #DDD6FE;
    border-radius: 20px;
    padding: 1.5rem 1.8rem;
    box-shadow: 0 12px 30px -14px rgba(79, 70, 229, 0.35);
}
[data-testid="stMetricLabel"] p {
    font-size: 0.85rem !important;
    font-weight: 700 !important;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: var(--muted) !important;
}
[data-testid="stMetricValue"] {
    font-size: 2.8rem !important;
    font-weight: 800 !important;
    background: linear-gradient(135deg, #4F46E5, #0EA5E9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Alerts */
[data-testid="stAlert"] {
    border-radius: 14px;
    border: none;
    font-weight: 500;
}

/* Result cards (invoice flag) */
.result-card {
    display: flex; align-items: center; gap: 1.2rem;
    border-radius: 20px;
    padding: 1.5rem 1.8rem;
    margin-top: 1rem;
    border: 1px solid;
}
.result-card .icon {
    font-size: 2.2rem;
    width: 64px; height: 64px;
    border-radius: 16px;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
}
.result-card h3 { margin: 0; font-size: 1.3rem; font-weight: 800; }
.result-card p  { margin: 0.2rem 0 0 0; font-size: 0.92rem; opacity: 0.85; }
.result-danger {
    background: linear-gradient(135deg, #FFF1F2, #FFE4E6);
    border-color: #FECDD3; color: #9F1239;
    box-shadow: 0 12px 28px -14px rgba(225, 29, 72, 0.5);
}
.result-danger .icon { background: #FFE4E6; }
.result-safe {
    background: linear-gradient(135deg, #ECFDF5, #D1FAE5);
    border-color: #A7F3D0; color: #065F46;
    box-shadow: 0 12px 28px -14px rgba(5, 150, 105, 0.5);
}
.result-safe .icon { background: #D1FAE5; }

/* ---------- Sidebar ---------- */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1E1B4B 0%, #312E81 100%);
    border-right: none;
}
[data-testid="stSidebar"] * { color: #E0E7FF; }
[data-testid="stSidebar"] h1 {
    color: white !important;
    font-size: 1.35rem;
    font-weight: 800;
}
[data-testid="stSidebar"] hr { border-color: rgba(255,255,255,0.15); }
[data-testid="stSidebar"] [role="radiogroup"] label {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 12px;
    padding: 0.7rem 0.9rem;
    margin-bottom: 0.5rem;
    transition: all 0.2s ease;
    width: 100%;
}
[data-testid="stSidebar"] [role="radiogroup"] label:hover {
    background: rgba(255,255,255,0.15);
    transform: translateX(3px);
}
[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
    background: linear-gradient(135deg, #6366F1, #0EA5E9);
    border-color: transparent;
    box-shadow: 0 8px 18px -8px rgba(14, 165, 233, 0.7);
}
.impact-box {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.14);
    border-radius: 16px;
    padding: 1rem 1.1rem;
    margin-top: 1rem;
}
.impact-box .title {
    font-size: 0.75rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 1px;
    color: #A5B4FC; margin-bottom: 0.6rem;
}
.impact-box .item {
    font-size: 0.88rem; padding: 0.3rem 0;
    color: #E0E7FF;
}

/* Divider */
hr { border-color: var(--border); }
</style>
""", unsafe_allow_html=True)


# =========================================================
# Header Section
# =========================================================

st.markdown("""
<div class="hero">
    <h1>📦 INVOICE IQ</h1>
    <p class="sub">AI-Driven Freight Cost Prediction &amp; Invoice Risk Flagging</p>
    <p class="desc">
        An internal analytics portal that uses machine learning to streamline
        vendor invoice operations and protect your bottom line.
    </p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📈</div>
        <h4>Forecast freight costs</h4>
        <p>Accurate predictions to support budgeting and vendor negotiations.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🛡️</div>
        <h4>Detect risky invoices</h4>
        <p>Spot abnormal or suspicious vendor invoices before they're paid.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <h4>Reduce leakage &amp; workload</h4>
        <p>Cut financial leakage and automate manual review effort.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()


# =========================================================
# Sidebar
# =========================================================

st.sidebar.title("🔍 Model Selection")

selected_model = st.sidebar.radio(
    "Choose Prediction Module",
    [
        "Freight Cost Prediction",
        "Invoice Manual Approval Flag"
    ]
)

st.sidebar.markdown("""
<div class="impact-box">
    <div class="title">Business Impact</div>
    <div class="item">📉 Improved cost forecasting</div>
    <div class="item">🧾 Reduced invoice fraud &amp; anomalies</div>
    <div class="item">⚙️ Faster finance operations</div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# Freight Cost Prediction
# =========================================================

if selected_model == "Freight Cost Prediction":

    st.markdown("""
    <div class="section-title">🚚 Freight Cost Prediction <span class="pill">Regression</span></div>
    <div class="objective-box">
        <b class="label">Objective</b>
        Predict freight cost for a vendor invoice using <b>Invoice Dollars</b>
        to support budgeting, forecasting, and vendor negotiations.
    </div>
    """, unsafe_allow_html=True)

    with st.form("freight_form"):

        dollars = st.number_input(
            "💲 Invoice Dollars",
            min_value=1.0,
            value=18500.0
        )

        submit_freight = st.form_submit_button(
            "🔮 Predict Freight Cost"
        )

    if submit_freight:

        input_data = {
            "Dollars": [dollars]
        }

        prediction = predict_freight_cost(input_data)[
            "Predicted_Freight"
        ]

        st.success("Prediction completed successfully.")

        st.metric(
            label="📊 Estimated Freight Cost",
            value=f"${prediction.iloc[0]:,.2f}"
        )


# =========================================================
# Invoice Flag Prediction
# =========================================================

else:

    st.markdown("""
    <div class="section-title">🚨 Invoice Manual Approval Prediction <span class="pill">Classification</span></div>
    <div class="objective-box">
        <b class="label">Objective</b>
        Predict whether a vendor invoice should be <b>flagged for manual approval</b>
        based on invoice cost, freight, and purchase patterns.
    </div>
    """, unsafe_allow_html=True)

    with st.form("invoice_flag_form"):

        col1, col2, col3 = st.columns(3)

        with col1:

            invoice_quantity = st.number_input(
                "Invoice Quantity",
                min_value=1,
                value=50
            )

            freight = st.number_input(
                "Freight Cost",
                min_value=0.0,
                value=1.73
            )

        with col2:

            invoice_dollars = st.number_input(
                "Invoice Dollars",
                min_value=1.0,
                value=352.95
            )

            total_item_quantity = st.number_input(
                "Total Item Quantity",
                min_value=1,
                value=162
            )

        with col3:

            total_item_dollars = st.number_input(
                "Total Item Dollars",
                min_value=1.0,
                value=2476.0
            )

        submit_flag = st.form_submit_button(
            "🧠 Evaluate Invoice Risk"
        )

    if submit_flag:

        input_data = {
            "invoice_quantity": [invoice_quantity],
            "invoice_dollars": [invoice_dollars],
            "Freight": [freight],
            "total_item_quantity": [total_item_quantity],
            "total_item_dollars": [total_item_dollars]
        }

        flag_prediction = predict_invoice_flag(
            input_data
        )["Predicted_Flag"]

        is_flagged = bool(flag_prediction.iloc[0])

        if is_flagged:

            st.markdown("""
            <div class="result-card result-danger">
                <div class="icon">🚨</div>
                <div>
                    <h3>Invoice requires MANUAL APPROVAL</h3>
                    <p>This invoice shows patterns that warrant a closer review by the finance team.</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown("""
            <div class="result-card result-safe">
                <div class="icon">✅</div>
                <div>
                    <h3>Invoice is SAFE for Auto-Approval</h3>
                    <p>No abnormal patterns detected. This invoice can proceed automatically.</p>
                </div>
            </div>
            """, unsafe_allow_html=True)