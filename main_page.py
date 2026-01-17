import streamlit as st
import json

def load_data():
    try:
        with open('data.json', 'r') as f:
            return json.load(f)
    except Exception:
        return {"name": "EduReach", "story": "Loading...", "mission": "Loading...", "vision": "Loading...", "programs": [], "team": []}

data = load_data()
ngo_name = data.get("name", "EduReach Foundation")

st.set_page_config(page_title=ngo_name, layout="wide")

# --- ADVANCED GLOBAL VISIBILITY FIX ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #fcfdfd; }}

    /* FORCE ALL HEADERS TO BE VISIBLE SLATE COLOR */
    h1, h2, h3, h4, p, span, label {{
        color: #1e293b !important;
        font-family: 'Helvetica Neue', sans-serif;
    }}

    .hero-section {{
        background: linear-gradient(to right, #ffffff, #f0fdf4);
        padding: 60px;
        border-radius: 24px;
        border: 1px solid #dcfce7;
        text-align: center;
        margin-bottom: 40px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
    }}

    .program-card {{
        background-color: #ffffff;
        padding: 30px;
        border-radius: 16px;
        border-bottom: 4px solid #22c55e;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        min-height: 200px;
    }}

    .team-box {{
        background: #ffffff;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #f1f5f9;
    }}

    .cta-box {{
        background-color: #1e293b;
        padding: 50px;
        border-radius: 24px;
        text-align: center;
        margin-top: 60px;
    }}
    /* Ensure footer text stays white because the box is dark */
    .cta-box h3, .cta-box p {{ color: white !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- TOP NAV ---
st.markdown(f"## 🏛️ {ngo_name}")
st.divider()

# --- HERO ---
st.markdown(f"""
    <div class="hero-section">
        <h1 style="color: #166534 !important;">{data['mission']}</h1>
        <p style="font-size: 1.2rem; color: #475569 !important;"><b>Our Vision:</b> {data['vision']}</p>
    </div>
    """, unsafe_allow_html=True)

# --- STORY ---
col_s1, col_s2 = st.columns([2, 1])
with col_s1:
    st.markdown("### 📖 Our Journey")
    st.write(data['story'])
with col_s2:
    st.success(f"**Action matters.** {ngo_name} has been serving the community since 2015.")

# --- CORE VALUES ---
st.write("---")
st.write("## 💎 Our Core Values")
if data.get('values'):
    v_cols = st.columns(len(data['values']))
    for i, value in enumerate(data['values']):
        with v_cols[i]:
            st.markdown(f'<div style="background-color: #f8fafc; padding: 20px; border-radius: 15px; text-align: center; border: 1px dashed #cbd5e1; height: 100%;"><div style="font-size: 24px;">✨</div><div style="font-weight: bold; color: #1e293b;">{value}</div></div>', unsafe_allow_html=True)

# --- PROGRAMS ---
st.write("---")
st.write("## 🚀 Key Programs")
if data['programs']:
    cols = st.columns(3)
    for idx, prog in enumerate(data['programs']):
        with cols[idx % 3]:
            st.markdown(f'<div class="program-card"><h4 style="margin-top:0;">{prog["name"]}</h4><p>{prog["desc"]}</p></div>', unsafe_allow_html=True)

# --- TEAM ---
st.write("---")
st.write("## 👥 Our Leadership")
if data['team']:
    t_cols = st.columns(4)
    for idx, m in enumerate(data['team']):
        with t_cols[idx % 4]:
            st.markdown(f'<div class="team-box"><div style="font-size:30px;">👤</div><div style="font-weight: bold; color:#0f172a;">{m["name"]}</div><div style="color: #64748b; font-size: 0.9rem;">{m["role"]}</div></div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown(f'<div class="cta-box"><h3>Become a part of the {ngo_name} family</h3><p>Your contribution changes lives through education.</p></div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns([1, 1, 1])
with c2:
    bs1, bs2 = st.columns(2)
    bs1.button("❤️ Donate", use_container_width=True, type="primary")
    bs2.button("🤝 Volunteer", use_container_width=True)
