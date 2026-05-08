import numpy as np

class PerformanceEngine:
    def analyze_player(self, player_id, trajectories, pitch_dims):
        if not trajectories: return None
        coords = np.array(trajectories)
        activity = float(np.sum(np.linalg.norm(np.diff(coords, axis=0), axis=1)) / len(coords)) if len(coords) > 1 else 0.5
        y_coords = coords[:, 1]
        width_usage = float((np.max(y_coords) - np.min(y_coords)) / pitch_dims[1])
        
        strengths, weaknesses = [], []
        if activity > 0.8: strengths.append("High Intensity Movement")
        elif activity < 0.3: weaknesses.append("Low Tactical Engagement")
        if width_usage > 0.6: strengths.append("Excellent Width Support")
        
        return {
            'player_id': player_id,
            'avg_position': np.mean(coords, axis=0).tolist(),
            'activity_score': activity,
            'strengths': strengths,
            'weaknesses': weaknesses
        }
