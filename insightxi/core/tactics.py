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
        insights = {
            'strengths': [], 
            'weaknesses': [], 
            'style': "Balanced",
            'pressing_zones': [],
            'player_roles': {}
        }
        compactness = stats.get('compactness', 0)
        width = stats.get('width', 0)
        depth = stats.get('depth', 0)
        
        # 1. Individual Role & Position Detection
        # Mock role assignment based on pitch coordinates
        for i in range(1, 12):
            if i == 1: insights['player_roles'][f"Player {i}"] = "Sweeper Keeper"
            elif i <= 5: insights['player_roles'][f"Player {i}"] = "Ball-Winning Defender"
            elif i <= 9: insights['player_roles'][f"Player {i}"] = "Box-to-Box Midfielder"
            else: insights['player_roles'][f"Player {i}"] = "Target Forward"

        # 2. Pressing Intensity Mapping
        if depth > 35:
            insights['pressing_zones'].append("High-Press: Final Third")
        elif depth > 20:
            insights['pressing_zones'].append("Mid-Block: Central Third")
        else:
            insights['pressing_zones'].append("Low-Block: Defensive Third")

        # 3. Elite Style Detection
        if compactness < 12 and depth < 20:
            insights['style'] = "Park the Bus"
        elif compactness < 18 and depth > 35:
            insights['style'] = "Gegenpressing"
        elif width > 50 and compactness > 22:
            insights['style'] = "Tiki-Taka"
        else:
            insights['style'] = "Tactical Hybrid"
        
        # 4. Deep Flaw Detection
        if width < 30:
            insights['weaknesses'].append("Narrow Structural Bias: Attack is predictable.")
        if depth > 45:
            insights['weaknesses'].append("Counter-Attack Vulnerability: Defense is over-extended.")
        if compactness > 30:
            insights['weaknesses'].append("Broken Defensive Lines: Vertical gaps are dangerously large.")
            
        # 5. Strengths
        if compactness < 15:
            insights['strengths'].append("Elite Unit Cohesion")
        if width > 55:
            insights['strengths'].append("Superior Pitch Stretching")
            
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
