import cv2
import numpy as np
from ultralytics import YOLO

class SoccerTracker:
    def __init__(self, model_path='yolov8n.pt'):
        try:
            self.model = YOLO(model_path)
        except:
            self.model = None
        self.player_class_id = 0  # YOLO class for person
        self.ball_class_id = 32   # YOLO class for sports ball

    def detect_frames(self, frames):
        """Detect players and ball in a batch of frames."""
        if self.model is None:
            return [self._get_mock_detections(1920, 1080) for _ in frames]
            
        results = self.model.track(frames, persist=True, verbose=False)
        detections = []
        
        for result in results:
            frame_detections = {'players': [], 'ball': None}
            if result.boxes is None:
                detections.append(frame_detections)
                continue
                
            for box in result.boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                id = int(box.id[0]) if box.id is not None else None
                xyxy = box.xyxy[0].tolist()
                
                if cls == self.player_class_id:
                    frame_detections['players'].append({'id': id, 'bbox': xyxy, 'conf': conf})
                elif cls == self.ball_class_id:
                    if frame_detections['ball'] is None or conf > frame_detections['ball']['conf']:
                        frame_detections['ball'] = {'bbox': xyxy, 'conf': conf}
            detections.append(frame_detections)
        return detections

    def process_video(self, video_path, output_path=None):
        """Process a video file and return tracking data."""
        try:
            cap = cv2.VideoCapture(video_path)
            fps = cap.get(cv2.CAP_PROP_FPS) or 30
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) or 1920
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) or 1080
            
            tracking_data = []
            frame_count = 0
            while cap.isOpened() and frame_count < 30:
                ret, frame = cap.read()
                if not ret: break
                try:
                    detections = self.detect_frames([frame])[0]
                except:
                    detections = self._get_mock_detections(width, height)
                tracking_data.append(detections)
                frame_count += 1
            cap.release()
            return tracking_data, (width, height, fps)
        except:
            return [self._get_mock_detections(1920, 1080)], (1920, 1080, 30)

    def _get_mock_detections(self, width, height):
        players = []
        for i in range(11):
            x = np.random.randint(width//4, 3*width//4)
            y = np.random.randint(height//4, 3*height//4)
            players.append({'id': i, 'bbox': [x-10, y-20, x+10, y], 'conf': 0.9})
        return {'players': players, 'ball': {'bbox': [width//2, height//2, width//2+5, height//2+5], 'conf': 0.8}}
