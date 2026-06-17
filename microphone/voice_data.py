class VoiceData:
    def __init__(self, text):
        self.text = text.strip()

    def get_command(self):
        if "תגביה" in self.text:
            return "volume_up"
        if "תנמיך" in self.text:
            return "volume_down"
        if "תעצור" in self.text:
            return "stop"
        if "תמשיך" in self.text:
            return "continue"
        if "גלול כלפי מעלה" in self.text:
            return "scroll_up"
        if "גלול כלפי מטה" in self.text:
            return "scroll_down"
        return None
