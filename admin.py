import streamlit as st
import json
import os

def load_data():
    if not os.path.exists('data.json'):
        return {
            "name": "EduReach Foundation", 
            "story": "Our journey began in 2015...", 
            "mission": "Empowering the next generation...", 
            "vision": "A world where every child can lead...", 
            "values": ["Inclusivity", "Transparency"], 
            "programs": [], 
            "team": []
        }
    with open('data.json', 'r') as f:
        return json.load(f)

def save_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

st.set_page_config(page_title="NGO Admin Panel", layout="wide")

# --- GLOBAL TEXT FIX ---
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    
    /* Force ALL headers and text to Dark Slate */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, .stText {
        color: #1e293b !important;
    }

    .admin-header {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border-bottom: 4px solid #007bff;
        margin-bottom: 30px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }

    /* Input Styling */
    .stTextInput input, .stTextArea textarea {
        background-color: #ffffff !important;
        color: #1e293b !important;
        border: 1px solid #cbd5e1 !important;
    }

    /* Expander Headers Fix */
    .streamlit-expanderHeader p {
        color: #1e293b !important;
        font-weight: 600 !important;
    }

    /* Tab Label Fix */
    button[data-baseweb="tab"] p {
        color: #1e293b !important;
    }
    
    .stButton>button {
        background-color: #007bff;
        color: white !important;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

data = load_data()

st.markdown(f'<div class="admin-header"><h1>🛠️ {data.get("name")} Admin</h1><p>Update website content instantly</p></div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["📖 Story & Vision", "💎 Core Values", "🚀 Programs", "👥 Team"])

with tab1:
    st.subheader("Edit Fundamentals")
    data['name'] = st.text_input("NGO Name", data.get('name', ''))
    data['story'] = st.text_area("Our Journey Text", data['story'], height=200)
    data['mission'] = st.text_input("Mission Statement", data['mission'])
    data['vision'] = st.text_input("Vision Statement", data['vision'])
    if st.button("Save Basic Info"):
        save_data(data)
        st.success("Basics updated!")

with tab2:
    st.subheader("Manage Core Values")
    for i, val in enumerate(data['values']):
        c1, c2 = st.columns([5, 1])
        data['values'][i] = c1.text_input(f"Value {i+1}", val, key=f"val_{i}")
        if c2.button("🗑️", key=f"del_v_{i}"):
            data['values'].pop(i)
            save_data(data); st.rerun()
    new_v = st.text_input("Add New Value")
    if st.button("Add Value"):
        if new_v: data['values'].append(new_v); save_data(data); st.rerun()

with tab3:
    st.subheader("Our Programs")
    for i, prog in enumerate(data['programs']):
        with st.expander(f"📦 {prog['name']}"):
            data['programs'][i]['name'] = st.text_input("Title", prog['name'], key=f"pn_{i}")
            data['programs'][i]['desc'] = st.text_area("Description", prog['desc'], key=f"pd_{i}")
            if st.button(f"Delete {prog['name']}", key=f"btn_p_{i}"):
                data['programs'].pop(i); save_data(data); st.rerun()
    st.markdown("#### ➕ Add New")
    np_name = st.text_input("Program Name")
    np_desc = st.text_area("Program Description")
    if st.button("Save New Program"):
        if np_name and np_desc: data['programs'].append({"name": np_name, "desc": np_desc}); save_data(data); st.rerun()

with tab4:
    st.subheader("Team Members")
    for i, m in enumerate(data['team']):
        with st.expander(f"👤 {m['name']}"):
            data['team'][i]['name'] = st.text_input("Name", m['name'], key=f"tn_{i}")
            data['team'][i]['role'] = st.text_input("Role", m['role'], key=f"tr_{i}")
            if st.button(f"Remove {m['name']}", key=f"btn_t_{i}"):
                data['team'].pop(i); save_data(data); st.rerun()
    nt_name = st.text_input("Member Name")
    nt_role = st.text_input("Member Role")
    if st.button("Save Team"):
        if nt_name and nt_role: data['team'].append({"name": nt_name, "role": nt_role}); save_data(data); st.rerun()
