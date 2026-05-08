import numpy as np

class SpatialMapper:
    def __init__(self, frame_dims, pitch_dims=(105, 68)):
        self.frame_width, self.frame_height = frame_dims
        self.pitch_length, self.pitch_width = pitch_dims
        
    def transform_to_pitch(self, bbox):
        x1, y1, x2, y2 = bbox
        center_x = (x1 + x2) / 2
        center_y = y2 
        norm_x = center_x / self.frame_width
        norm_y = center_y / self.frame_height
        return (norm_x * self.pitch_length, norm_y * self.pitch_width)

    def get_team_stats(self, players_on_pitch):
        if not players_on_pitch: return {}
        coords = np.array(players_on_pitch)
        center = np.mean(coords, axis=0)
        distances = np.linalg.norm(coords - center, axis=1)
        min_coords = np.min(coords, axis=0)
        max_coords = np.max(coords, axis=0)
        return {
            'center': center.tolist(),
            'compactness': float(np.mean(distances)),
            'width': float(max_coords[1] - min_coords[1]),
            'depth': float(max_coords[0] - min_coords[0])
        }
