import speech_recognition as sr
import threading
from microphone.voice_data import VoiceData

class VoiceService:
    def __init__(self, on_command):
        self.on_command = on_command  # callback function
        self.recognizer = sr.Recognizer()
        self.running = False

    def start(self):
        self.running = True
        thread = threading.Thread(target=self._listen_loop, daemon=True)
        thread.start()

    def stop(self):
        self.running = False

    def _listen_loop(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("המיקרופון פעיל - דבר כדי לשלוט!")
            while self.running:
                try:
                    audio = self.recognizer.listen(source, timeout=3, phrase_time_limit=4)
                    text = self.recognizer.recognize_google(audio, language="he-IL")
                    print(f"זוהה: {text}")
                    voice_data = VoiceData(text)
                    command = voice_data.get_command()
                    if command:
                        self.on_command(command)
                except sr.WaitTimeoutError:
                    pass
                except sr.UnknownValueError:
                    pass
