import streamlit as st
import yaml
from pathlib import Path
from PIL import Image

st.set_page_config(
    page_title="Md Robin Jamal",
    page_icon="🌒",
    layout="wide")

# Font Awesome for icons
st.markdown("<link href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css' rel='stylesheet'>", unsafe_allow_html=True)

# Load YAML config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Load profile image
image_path = Path("assets/profile.jpg")
profile_pic = Image.open(image_path) if image_path.exists() else None

# Dark Theme & Animations
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: #c9d1d9;
}
h1, h2, h3, h4 {
    color: #58a6ff;
}
.card {
    background-color: #161b22;
    padding: 1rem;
    margin-bottom: 1rem;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(255,255,255,0.05);
    transition: all 0.3s ease-in-out;
}
.card:hover {
    transform: scale(1.01);
    box-shadow: 0 0 15px rgba(255,255,255,0.1);
}
.skills span {
    background: #21262d;
    color: #58a6ff;
    padding: 0.4rem 0.8rem;
    border-radius: 20px;
    display: inline-block;
    margin: 0.25rem;
    font-size: 0.85rem;
}
.metric-tile {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    padding: 1rem;
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 0 15px rgba(0,0,0,0.25);
    transition: all 0.3s ease;
}
.metric-tile:hover {
    transform: scale(1.03);
}
</style>
""", unsafe_allow_html=True)

# Sidebar Info
with st.sidebar:
    if profile_pic:
        st.image(profile_pic, width=180)
    st.title(config['name'])
    st.markdown(f"**{config['title']}**")
    st.markdown(f"📍 {config['location']}")
    st.markdown(f"📧 {config['email']}")
    st.markdown(f"[🔗 LinkedIn ↗]({config['linkedin']})")

# Metrics Section
st.markdown("## 🚀 Dashboard")
col1, col2, col3 = st.columns(3)
col1.markdown("<div class='metric-tile'><h3>3+</h3><p><i class='fa-solid fa-briefcase'></i> Years of Experience</p></div>", unsafe_allow_html=True)
col2.markdown(f"<div class='metric-tile'><h3>{len(config['experience'])}</h3><p><i class='fa-solid fa-user-tie'></i> Key Roles</p></div>", unsafe_allow_html=True)
col3.markdown(f"<div class='metric-tile'><h3>{len(config['certifications'])}</h3><p><i class='fa-solid fa-award'></i> Certifications</p></div>", unsafe_allow_html=True)

# Tabbed Interface
tab1, tab2, tab3, tab4 = st.tabs(["🧑‍💼 About", "📚 Experience", "💼 Skills", "📬 Contact"])

with tab1:
    st.header("👋 About Me")
    st.markdown(f"### {config['name']} – {config['title']}")
    st.write(config['about'])

    st.subheader("🎓 Education")
    for edu in config['education']:
        st.markdown(f"<div class='card'><b>{edu['degree']}</b><br/>{edu['institution']} – {edu['year']}</div>", unsafe_allow_html=True)

    st.subheader("📜 Certifications")
    st.markdown("<ul>" + "".join([f"<li>{c}</li>" for c in config['certifications']]) + "</ul>", unsafe_allow_html=True)

with tab2:
    st.header("📚 Work Experience")
    for job in config['experience']:
        with st.expander(f"**{job['role']}** — {job['company']} ({job['date']})"):
            for point in job['details']:
                st.markdown(f"- {point}")

with tab3:
    st.header("💼 Skills Overview")
    st.markdown("<div class='skills'>" + "".join([f"<span>{s}</span>" for s in config['skills']]) + "</div>", unsafe_allow_html=True)

with tab4:
    st.header("📬 Let's Connect")
    st.markdown(f"📧 Email: {config['email']}")
    st.markdown(f"[🔗 LinkedIn]({config['linkedin']})")
