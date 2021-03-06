from common import *

from analyze_photos import *
from pagerank import *

def get_top_cameras(n):
    camera_scores_combined = aggregate_camera_scores()
    top_cameras = {}
    for category, camera_scores in camera_scores_combined.iteritems():
        sorted_scores = sorted(camera_scores.items(), key = lambda x: x[1], reverse = True)
        top_cameras[category] = sorted_scores[:n]

    return top_cameras

def weighted_camera_scores(combined_camera_scores, **kwargs):
    """Calculates the weighted camera scores. The keyword arguments should
    be of the form category = weight."""

    weighted_camera_scores = defaultdict(float)
    for category in kwargs:
        if category not in combined_camera_scores:
            return None
        
        weight = kwargs[category]
        for camera, camera_score in combined_camera_scores[category]:
            weighted_camera_scores[camera] += weight * camera_score

    sorted_camera_scores = sorted(weighted_camera_scores.items(), key = lambda x: x[1], reverse = True)
    return sorted_camera_scores

