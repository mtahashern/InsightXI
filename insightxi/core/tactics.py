class TacticalInsightEngine:
    def __init__(self):
        pass

    def get_tactical_intelligence(self, team_a_stats, team_b_stats, formation_a, formation_b):
        """
        Dual-team competitive intelligence engine.
        Analyzes the interaction between two teams.
        """
        intel = {
            'team_a': self._analyze_single_team(team_a_stats, formation_a),
            'team_b': self._analyze_single_team(team_b_stats, formation_b),
            'matchup_verdict': "",
            'recovery_protocols': []
        }
        
        # Matchup Analysis
        if team_a_stats.get('compactness', 0) < team_b_stats.get('compactness', 0):
            intel['matchup_verdict'] = "Team A is winning the structural battle with superior compactness."
        else:
            intel['matchup_verdict'] = "Team B is controlling the space more effectively."
            
        # Recovery Logic
        if intel['team_a']['weaknesses']:
            intel['recovery_protocols'].append({
                'team': 'Team A',
                'issue': intel['team_a']['weaknesses'][0],
                'mitigation': "Shift to a 4-4-2 mid-block to reduce vertical gaps."
            })
            
        return intel

    def _analyze_single_team(self, stats, formation):
        insights = {'strengths': [], 'weaknesses': [], 'style': "Balanced"}
        
        # Style Detection
        compactness = stats.get('compactness', 0)
        if compactness < 15: insights['style'] = "High-Intensity Low Block"
        elif compactness > 25: insights['style'] = "Expansive Possession"
        
        # Flaw Detection
        if stats.get('width', 0) < 30:
            insights['weaknesses'].append("Critical Lack of Width: Attack is easily funneled.")
        if stats.get('depth', 0) > 40:
            insights['weaknesses'].append("Excessive Vertical Stretch: Midfield is isolated.")
            
        return insights

    def aggregate_batch_reports(self, reports):
        """
        Combine multiple clip analyses into a single comprehensive game verdict.
        """
        total_verdict = {
            'overall_performance': "Analyzing...",
            'persistent_weaknesses': [],
            'tactical_evolution': [],
            'final_coaching_report': ""
        }
        
        all_weaknesses = []
        for r in reports:
            all_weaknesses.extend(r['weaknesses'])
            
        # Identify recurring issues
        from collections import Counter
        counts = Counter(all_weaknesses)
        total_verdict['persistent_weaknesses'] = [w for w, count in counts.items() if count > 1]
        
        if not total_verdict['persistent_weaknesses']:
            total_verdict['overall_performance'] = "Consistent Structural Integrity"
            total_verdict['final_coaching_report'] = "The team maintained its shape well across all analyzed segments. Focus on individual creative freedom."
        else:
            total_verdict['overall_performance'] = "Structural Instability Detected"
            total_verdict['final_coaching_report'] = f"The system identified recurring issues: {', '.join(total_verdict['persistent_weaknesses'])}. Immediate tactical adjustment required."
            
        return total_verdict
