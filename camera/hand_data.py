class HandData:
    def __init__(self, landmarks):
        self.landmarks = landmarks
        self.history = []

    def calculate_distance(self, point1_idx, point2_idx):
        p1 = self.landmarks[point1_idx]
        p2 = self.landmarks[point2_idx]
        dist = ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

        self.history.append(dist)
        if len(self.history) > 5:
            self.history.pop(0)

        return sum(self.history) / len(self.history)

    def get_landmark(self, index):
        return self.landmarks[index]

    def get_wrist_y(self):
        return self.landmarks[0].y

    def is_fist(self):
        finger_tips  = [8, 12, 16, 20]
        finger_bases = [6, 10, 14, 18]
        return all(
            self.landmarks[tip].y > self.landmarks[base].y
            for tip, base in zip(finger_tips, finger_bases)
        )
