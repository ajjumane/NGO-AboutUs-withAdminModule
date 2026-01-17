import streamlit as st
from supabase_client import supabase

# -------------------- DATA HELPERS --------------------

def load_data():
    res = supabase.table("ngo_content").select("*").eq("id", 1).execute()

    if not res.data:
        default_data = {
            "id": 1,
            "name": "EduReach Foundation",
            "story": "",
            "mission": "",
            "vision": "",
            "values": [],
            "programs": [],
            "team": []
        }
        supabase.table("ngo_content").insert(default_data).execute()
        return default_data

    d = res.data[0]

    # SAFETY: handle NULLs from Supabase
    d["values"] = d.get("values") or []
    d["programs"] = d.get("programs") or []
    d["team"] = d.get("team") or []

    return d


def save_data(data):
    supabase.table("ngo_content").update({
        "name": data["name"],
        "story": data["story"],
        "mission": data["mission"],
        "vision": data["vision"],
        "values": data["values"],
        "programs": data["programs"],
        "team": data["team"]
    }).eq("id", 1).execute()


# -------------------- STREAMLIT SETUP --------------------

st.set_page_config(page_title="NGO Admin Panel", layout="wide")

if "data" not in st.session_state:
    st.session_state.data = load_data()

data = st.session_state.data

# -------------------- STYLES --------------------

st.markdown("""
<style>
.stApp { background-color: #f8fafc; }
h1, h2, h3, h4, h5, h6, p, label {
    color: #1e293b !important;
}
.admin-header {
    background: white;
    padding: 20px;
    border-radius: 12px;
    border-bottom: 4px solid #2563eb;
    margin-bottom: 25px;
}
.stButton>button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------

st.markdown(
    f"<div class='admin-header'><h1>🛠️ {data['name']} Admin</h1>"
    f"<p>Update website content</p></div>",
    unsafe_allow_html=True
)

tabs = st.tabs(["📖 Story & Vision", "💎 Values", "🚀 Programs", "👥 Team"])

# -------------------- TAB 1 --------------------

with tabs[0]:
    st.subheader("Basic Information")

    data["name"] = st.text_input("NGO Name", data["name"])
    data["story"] = st.text_area("Our Journey", data["story"], height=200)
    data["mission"] = st.text_input("Mission", data["mission"])
    data["vision"] = st.text_input("Vision", data["vision"])

    if st.button("Save Basics"):
        save_data(data)
        st.success("Saved successfully")

# -------------------- TAB 2 --------------------

with tabs[1]:
    st.subheader("Core Values")

    for i, val in enumerate(data["values"]):
        cols = st.columns([6, 1])
        data["values"][i] = cols[0].text_input(
            f"Value {i+1}", val, key=f"value_{i}"
        )
        if cols[1].button("❌", key=f"del_value_{i}"):
            data["values"].pop(i)
            save_data(data)
            st.rerun()

    new_value = st.text_input("Add New Value")
    if st.button("Add Value"):
        if new_value.strip():
            data["values"].append(new_value.strip())
            save_data(data)
            st.rerun()

# -------------------- TAB 3 --------------------

with tabs[2]:
    st.subheader("Programs")

    for i, prog in enumerate(data["programs"]):
        with st.expander(prog.get("name", f"Program {i+1}")):
            prog["name"] = st.text_input(
                "Program Name", prog.get("name", ""), key=f"prog_name_{i}"
            )
            prog["desc"] = st.text_area(
                "Description", prog.get("desc", ""), key=f"prog_desc_{i}"
            )
            if st.button("Delete Program", key=f"del_prog_{i}"):
                data["programs"].pop(i)
                save_data(data)
                st.rerun()

    st.markdown("### ➕ Add Program")
    pn = st.text_input("Name")
    pd = st.text_area("Description")

    if st.button("Add Program"):
        if pn and pd:
            data["programs"].append({"name": pn, "desc": pd})
            save_data(data)
            st.rerun()

# -------------------- TAB 4 --------------------

with tabs[3]:
    st.subheader("Team Members")

    for i, m in enumerate(data["team"]):
        with st.expander(m.get("name", f"Member {i+1}")):
            m["name"] = st.text_input(
                "Name", m.get("name", ""), key=f"team_name_{i}"
            )
            m["role"] = st.text_input(
                "Role", m.get("role", ""), key=f"team_role_{i}"
            )
            if st.button("Remove Member", key=f"del_team_{i}"):
                data["team"].pop(i)
                save_data(data)
                st.rerun()

    tn = st.text_input("New Member Name")
    tr = st.text_input("New Member Role")

    if st.button("Add Member"):
        if tn and tr:
            data["team"].append({"name": tn, "role": tr})
            save_data(data)
            st.rerun()
