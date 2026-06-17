from actions.action_executor import ActionExecutor

SCROLL_INTERVAL = 5

class GestureController:
    def __init__(self):
        self.executor = ActionExecutor()
        self.last_gesture = None
        self.scroll_counter = 0

    def process(self, hand):
        gesture_label = ""
        scroll_label = ""

        if hand.is_fist():
            gesture = "fist"
            gesture_label = "FIST - Paused"
        else:
            gesture = "open"
            dist = hand.calculate_distance(4, 8)
            percent = min(max(dist * 300, 0), 100)
            self.executor.set_volume(percent)
            gesture_label = f"OPEN - Vol: {int(percent)}%"

        if gesture != self.last_gesture:
            if gesture == "fist":
                self.executor.play_pause()
            self.last_gesture = gesture

        wrist_y = hand.get_wrist_y()
        self.scroll_counter += 1
        if self.scroll_counter >= SCROLL_INTERVAL:
            self.scroll_counter = 0
            if wrist_y < 0.33:
                self.executor.scroll(1)
                scroll_label = "SCROLL UP"
            elif wrist_y > 0.66:
                self.executor.scroll(-1)
                scroll_label = "SCROLL DOWN"

        return gesture, gesture_label, scroll_label
