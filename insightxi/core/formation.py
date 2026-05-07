import numpy as np
from sklearn.cluster import KMeans

class FormationDetector:
    def detect_formation(self, player_coords):
        if len(player_coords) < 7: return "Unknown"
        x_coords = np.array([p[0] for p in player_coords]).reshape(-1, 1)
        try:
            kmeans = KMeans(n_clusters=3, random_state=42, n_init=10).fit(x_coords)
            counts = np.bincount(kmeans.labels_)
            cluster_means = kmeans.cluster_centers_.flatten()
            sorted_indices = np.argsort(cluster_means)
            ordered_counts = [counts[i] for i in sorted_indices]
            return "-".join(map(str, ordered_counts))
        except:
            return "4-3-3"
