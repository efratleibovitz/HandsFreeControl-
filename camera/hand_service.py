from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from camera.hand_data import HandData

class HandService:
    def __init__(self):
        base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
        options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=1)
        self.detector = vision.HandLandmarker.create_from_options(options)

    def process_frame(self, mp_image):
        results = self.detector.detect(mp_image)
        if results.hand_landmarks:
            return HandData(results.hand_landmarks[0])
        return None
