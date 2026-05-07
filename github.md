# InsightXI - GitHub Setup Guide

Copy the contents below into their respective files in your GitHub repository.

---

## 📄 File 1: requirements.txt
**Location:** Root directory (`/`)

```text
opencv-python-headless
ultralytics
numpy
pandas
streamlit
matplotlib
fpdf
```

---

## 📄 File 2: .streamlit/config.toml
**Location:** `.streamlit/config.toml`

```toml
[theme]
primaryColor="#00ff00"
backgroundColor="#0e1117"
secondaryBackgroundColor="#161b22"
textColor="#ffffff"
font="sans serif"

[server]
headless = true
enableCORS = false
enableXsrfProtection = false
```

---

## 📄 File 3: insightxi/app.py
**Location:** `insightxi/app.py`

```python
import streamlit as st
import cv2
import numpy as np
import tempfile
import os
import matplotlib.pyplot as plt
from core.tracking import SoccerTracker
from core.mapping import SpatialMapper
from core.formation import FormationDetector
from core.analysis import PerformanceEngine
from core.tactics import TacticalInsightEngine
from utils.visualization import draw_pitch, plot_positions
from utils.report_generator import TacticalReportGenerator

st.set_page_config(page_title="InsightXI | Elite Tactical Suite", layout="wide")

st.markdown("""
<style>
    .main { background-color: #0e1117; color: white; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; border-radius: 10px; }
    .recovery-card { background-color: #1c2128; border-left: 5px solid #f85149; padding: 20px; border-radius: 8px; margin: 10px 0; }
    .style-badge { background-color: #238636; padding: 5px 10px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.title("⚽ InsightXI ELITE")
st.markdown("### *Autonomous Dual-Team Intelligence & Recovery Engine*")

engines = {
    'tracker': SoccerTracker(),
    'formation': FormationDetector(),
    'performance': PerformanceEngine(),
    'tactics': TacticalInsightEngine()
}

uploaded_file = st.file_uploader("Upload Match Footage", type=['mp4', 'avi', 'mov'])

if uploaded_file:
    with st.spinner("Executing Dual-Team Intelligence Pipeline..."):
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())
        
        tracking_data, (width, height, fps) = engines['tracker'].process_video(tfile.name)
        mapper = SpatialMapper((width, height))
        
        analysis_frame = tracking_data[0]
        players = analysis_frame['players']
        team_a_players = [mapper.transform_to_pitch(p['bbox']) for p in players[:len(players)//2]]
        team_b_players = [mapper.transform_to_pitch(p['bbox']) for p in players[len(players)//2:]]
        
        stats_a = mapper.get_team_stats(team_a_players)
        stats_b = mapper.get_team_stats(team_b_players)
        
        intel = engines['tactics'].get_tactical_intelligence(stats_a, stats_b, "4-3-3", "4-4-2")
        
        st.divider()
        st.subheader("⚔️ Competitive Matchup Analysis")
        st.info(f"**AI Verdict:** {intel['matchup_verdict']}")
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"#### Team A <span class='style-badge'>{intel['team_a']['style']}</span>", unsafe_allow_html=True)
            st.metric("Compactness", f"{stats_a.get('compactness', 0):.1f}m")
            for w in intel['team_a']['weaknesses']:
                st.error(f"⚠️ {w}")
                
        with c2:
            st.markdown(f"#### Team B <span class='style-badge'>{intel['team_b']['style']}</span>", unsafe_allow_html=True)
            st.metric("Compactness", f"{stats_b.get('compactness', 0):.1f}m")
            for w in intel['team_b']['weaknesses']:
                st.error(f"⚠️ {w}")
                
        st.divider()
        st.subheader("📊 Official Tactical Export")
        if st.button("Generate Professional Scouting Report (PDF)"):
            report_gen = TacticalReportGenerator(intel)
            report_path = "Tactical_Report_InsightXI.pdf"
            report_gen.generate_report(report_path)
            with open(report_path, "rb") as f:
                st.download_button("⬇️ Download Official Report", f, file_name="InsightXI_Scouting_Report.pdf")
            
        st.divider()
        st.subheader("📍 Interactive Tactical Board")
        fig, ax = plt.subplots(figsize=(12, 8))
        draw_pitch(ax, theme='dark')
        plot_positions(team_a_players, "Team A", ax, color='#00ff00')
        plot_positions(team_b_players, "Team B", ax, color='#ff0000')
        st.pyplot(fig, use_container_width=True)
        
        os.unlink(tfile.name)
```

---

## 📄 File 4: insightxi/core/tactics.py
**Location:** `insightxi/core/tactics.py`

```python
class TacticalInsightEngine:
    def __init__(self):
        pass

    def get_tactical_intelligence(self, team_a_stats, team_b_stats, formation_a, formation_b):
        intel = {
            'team_a': self._analyze_single_team(team_a_stats, formation_a),
            'team_b': self._analyze_single_team(team_b_stats, formation_b),
            'matchup_verdict': "",
            'recovery_protocols': []
        }
        
        if team_a_stats.get('compactness', 0) < team_b_stats.get('compactness', 0):
            intel['matchup_verdict'] = "Team A is winning the structural battle with superior compactness."
        else:
            intel['matchup_verdict'] = "Team B is controlling the space more effectively."
            
        if intel['team_a']['weaknesses']:
            intel['recovery_protocols'].append({
                'team': 'Team A',
                'issue': intel['team_a']['weaknesses'][0],
                'mitigation': "Shift to a 4-4-2 mid-block to reduce vertical gaps."
            })
            
        return intel

    def _analyze_single_team(self, stats, formation):
        insights = {'strengths': [], 'weaknesses': [], 'style': "Balanced"}
        compactness = stats.get('compactness', 0)
        width = stats.get('width', 0)
        depth = stats.get('depth', 0)
        
        if compactness < 12 and depth < 20:
            insights['style'] = "Park the Bus (Deep Low Block)"
        elif compactness < 18 and depth > 35:
            insights['style'] = "Gegenpressing (High Intensity)"
        elif width > 50 and compactness > 22:
            insights['style'] = "Tiki-Taka (Expansive Possession)"
        else:
            insights['style'] = "Balanced Hybrid"
        
        if width < 30:
            insights['weaknesses'].append("Narrow Structural Bias: Attack is predictable.")
        if depth > 45:
            insights['weaknesses'].append("Counter-Attack Vulnerability: Defense is over-extended.")
        if compactness > 30:
            insights['weaknesses'].append("Broken Defensive Lines: Vertical gaps are too large.")
            
        if compactness < 15:
            insights['strengths'].append("Elite Unit Cohesion: Extremely hard to break down.")
        if width > 55:
            insights['strengths'].append("Superior Pitch Stretching: Creating massive interior gaps.")
            
        return insights
```

*(Note: I have also included the remaining core files in the actual 'github' file on your desktop for you to copy.)*
