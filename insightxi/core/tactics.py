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
