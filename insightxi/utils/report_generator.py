import fpdf
import datetime

class TacticalReportGenerator:
    def __init__(self, intel):
        self.intel = intel
        self.pdf = fpdf.FPDF()
        
    def generate_report(self, output_path):
        self.pdf.add_page()
        self.pdf.set_font("Arial", 'B', 20)
        self.pdf.cell(0, 10, "InsightXI ELITE - Tactical Intelligence Report", ln=True, align='C')
        self.pdf.set_font("Arial", '', 10)
        self.pdf.cell(0, 10, f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True, align='C')
        self.pdf.ln(10)
        
        # Matchup Verdict
        self.pdf.set_font("Arial", 'B', 14)
        self.pdf.cell(0, 10, "1. Competitive Matchup Verdict", ln=True)
        self.pdf.set_font("Arial", '', 12)
        self.pdf.multi_cell(0, 10, self.intel['matchup_verdict'])
        self.pdf.ln(5)
        
        # Team Analysis
        for team_key in ['team_a', 'team_b']:
            team_name = "TEAM A" if team_key == 'team_a' else "TEAM B"
            self.pdf.set_font("Arial", 'B', 14)
            self.pdf.cell(0, 10, f"2. {team_name} Profile", ln=True)
            self.pdf.set_font("Arial", 'I', 12)
            self.pdf.cell(0, 10, f"Detected Style: {self.intel[team_key]['style']}", ln=True)
            self.pdf.set_font("Arial", '', 12)
            self.pdf.cell(0, 10, "Strengths:", ln=True)
            for s in self.intel[team_key]['strengths'] or ["No specific strengths identified."]:
                self.pdf.cell(0, 10, f"- {s}", ln=True)
            self.pdf.cell(0, 10, "Weaknesses:", ln=True)
            for w in self.intel[team_key]['weaknesses'] or ["No specific weaknesses identified."]:
                self.pdf.cell(0, 10, f"- {w}", ln=True)
            self.pdf.ln(5)
            
        # Recovery Protocols
        self.pdf.set_font("Arial", 'B', 14)
        self.pdf.cell(0, 10, "3. Tactical Recovery Protocols", ln=True)
        self.pdf.set_font("Arial", '', 12)
        for protocol in self.intel['recovery_protocols']:
            self.pdf.multi_cell(0, 10, f"[{protocol['team']}] ISSUE: {protocol['issue']}\nPLAN: {protocol['mitigation']}")
            self.pdf.ln(2)
            
        self.pdf.output(output_path)
        return output_path
